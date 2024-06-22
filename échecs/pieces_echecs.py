from kandinsky import fill_rect as draw, draw_string as draw_txt, set_pixel as draw_px
from math import cos, sin, pi
from time import *

COLOR_CASE_NOIR = (222, 89, 0)
COLOR_CASE_BLANC = (255, 219, 132)
COLOR_PIECE_NOIR = (0, 0, 0)
COLOR_PIECE_BLANC = (255, 255, 255)
COLOR_SELECT = (165, 166, 165)

sens = {-1: (1,1), 0: (1,1), 1: (-1,1), "x": 0, "y": 0, "inv": 1}

is_in = lambda val: -1 < val < 8
col_is_diff = lambda un,de: True if un and de and (un.couleur and not de.couleur or not un.couleur and de.couleur) else False

def get_ver_coords(x, y):
  if sens["x"]:
    x = 7 - x
  if sens["y"]:
    y = 7 - y
  x, y = [x, y][::sens["inv"]]
  return [round(60 + y * 25), round(20 + x * 25)]

def rond(x, y, rayon=5, col=None, ver=True):
  if ver:
    x, y = get_ver_coords(x, y)
  x += 13
  y += 13
  if col is None:
    col = COLOR_SELECT
  for i in range(91):
    c = cos((i*pi)/180) * rayon
    s = sin((i*pi)/180) * rayon
    draw(int(x-c), int(y-s), int(2*c), int(2*s), col)

def select(x, y, cote=25, ver=True):
  if ver:
    x, y = get_ver_coords(x, y)
  tt = 0
  for i in range(cote):
    if cote % 2:
      t = tt
    for j in range(cote):
      if t:
        draw_px(x+i, y+j, COLOR_SELECT)
        t = 0
      else:
        t = 1
    if tt:
      tt = 0
    else:
      tt = 1

def mouvement(x, y, piece_bouffe=None):
  return {"x": x, "y": y, "pb": piece_bouffe}

class Case:
  dessin = []
  def __init__(self, game=None, x=-1, y=-1, couleur=-1):
    self.game, self.x, self.y, self.couleur = game, x, y, couleur
    self.selected = False
  def __bool__(self):
    return False if self.couleur == -1 else True
  def __repr__(self):
    return ""
  def draw(self, is_select=False, psens=None, col=None, pos=None, just_bkg=False, decy=0):
    psens = psens or sens[self.couleur]
    x, y = pos or get_ver_coords(self.x, self.y)
    y += decy
    if col is None:
      if self.selected:
        draw(x, y, 25, 25, COLOR_SELECT)
      else:
        draw(x, y, 25, 25, [COLOR_CASE_NOIR, COLOR_CASE_BLANC][(self.x + self.y) % 2])
    else:
      draw(x, y, 25, 25, col)
    if is_select:
      select(self.x, self.y)
    if not just_bkg:
      for xbase,i in enumerate(self.dessin[::psens[0]]):
        for ybase,j in enumerate("{0:21b}".format(i)):
          xx, yy = [xbase, ybase][::psens[1]]
          if j == "1":
            draw_px(xx+2+x, yy+2+y, COLOR_PIECE_BLANC if self.couleur else COLOR_PIECE_NOIR)

class Piece(Case):
  notation = ""
  point = 0
  mouvs = ()
  def __init__(self, *args, simul=False, config=None, **kwargs):
    self.simul = simul
    super().__init__(*args, **kwargs)
    if config:
      self.set_config(config)
  def __repr__(self):
    all_attr = set(dir(self))
    return (self.notation.upper() if self.couleur else self.notation) + ("," if all_attr else "") + ",".join([str(getattr(self, i)) for i in set(dir(self)).difference(["x","y","couleur"]) if type(getattr(self,i)) is int])
  def set_config(self, config):
    self.go_fast = int(config[0])
  def test_good_mouv(self, x, y):
    if self.simul:
      return True
    roi = self.game.rois[self.couleur]
    xx, yy = self.x, self.y
    self.game.plateau[self.x][self.y] = Case(self.game, self.x, self.y)
    self.game.plateau[x][y], pc_av = self, self.game.plateau[x][y]
    self.x, self.y = x, y
    if roi.est_en_echec():
      rep = False
    else:
      rep = True
    self.game.plateau[xx][yy] = self
    self.game.plateau[x][y] = pc_av
    self.x, self.y = xx, yy
    return rep
  def get_mouvs(self, poss=((1,0),(-1,0),(0,1),(0,-1))):
    mouvs = []
    for i,j in self.mouvs:
      av = 1
      while is_in(self.x + av*i) and is_in(self.y + av*j):
        case_test = self.game.plateau[self.x+av*i][self.y+av*j]
        if not case_test:
          if self.test_good_mouv(self.x+av*i, self.y+av*j):
            mouvs.append(mouvement(self.x+av*i, self.y+av*j))
        else:
          if col_is_diff(case_test, self) and self.test_good_mouv(self.x+av*i, self.y+av*j):
            mouvs.append(mouvement(self.x+av*i, self.y+av*j, case_test))
          break
        av += 1
    return mouvs
  def bouger(self, mouv, save=True):
    if save:
      self.game.partie += str(self.x)+str(self.y)+":"+str(mouv["x"])+str(mouv["y"])
    self.game.verif_bouf(mouv, save)
    self.game.plateau[mouv["x"]][mouv["y"]] = self
    new_case = Case(self.game, self.x, self.y)
    self.game.plateau[self.x][self.y] = new_case
    self.x, self.y = mouv["x"], mouv["y"]
    self.draw()
    new_case.draw()
    return new_case, self
  def draw(self, *args, **kwargs):
    av, sens["inv"] = sens["inv"], 1 if int(self.y) != self.y else sens["inv"]
    super().draw(*args, **kwargs)
    sens["inv"] = av

class Pion(Piece):
  notation = "p"
  point = 1
  dessin = [
    0b000000000000000000000,
    0b000000000000000000000,
    0b000000000000000000000,
    0b000000000000000000000,
    0b000000000000000000000,
    0b000000000000000000000,
    0b000000000000000000000,
    0b000000001111100000000,
    0b000000011111110000000,
    0b000000111111111000000,
    0b000000111111111000000,
    0b000000111111111000000,
    0b000000111111111000000,
    0b000000011111110000000,
    0b000000001111100000000,
    0b000000000111000000000,
    0b000000000111000000000,
    0b000000001111100000000,
    0b000000111111111000000,
    0b000011111111111110000,
    0b000011111111111110000
  ]
  def __init__(self, *args, **kwargs):
    self.go_fast = -1
    super().__init__(*args, **kwargs)
  def get_mouvs(self):
    mouvs = []
    av = 1 if self.couleur else -1
    if av == -1 and not self.y or av == 1 and self.y == 7:
      return mouvs
    if not self.game.plateau[self.x][self.y+av]:
      if self.test_good_mouv(self.x, self.y+av):
        mouvs.append(mouvement(self.x, self.y+av))
      if self.couleur and self.y == 1 or not self.couleur and self.y == 6:
        if not self.game.plateau[self.x][self.y+2*av] and self.test_good_mouv(self.x, self.y+2*av):
          mouvs.append(mouvement(self.x, self.y+2*av))
    for i in -1,1:
      if is_in(self.x+i):
        pc_test = self.game.plateau[self.x+i][self.y+av]
        if col_is_diff(self, pc_test) and self.test_good_mouv(self.x+i, self.y+av):
            mouvs.append(mouvement(self.x+i, self.y+av, pc_test))
        if self.couleur and self.y == 4 or not self.couleur and self.y == 3:
          pseudo_pion = self.game.plateau[self.x+i][self.y]
          if type(pseudo_pion) is Pion and pseudo_pion.go_fast == self.game.cur_tour-1:
            self.game.plateau[self.x+i][self.y] = None
            if self.test_good_mouv(self.x+i, self.y+av):
              mouvs.append(mouvement(self.x+i, self.y+av, pseudo_pion))
            self.game.plateau[self.x+i][self.y] = pseudo_pion
    return mouvs
  def bouger(self, mouv, save=True):
    if abs(mouv["y"]-self.y) == 2:
      self.go_fast = self.game.cur_tour
    if mouv["y"] == 7 or mouv["y"] == 0:
      xx, yy = self.x, self.y
      if save:
        self.game.partie += str(self.x)+str(self.y)+":"+str(mouv["x"])+str(mouv["y"])
      self.game.verif_bouf(mouv, save)
      self.x, self.y = mouv["x"], mouv["y"]
      self.selected = True
      self.draw()
      new_case = Case(self.game, xx, yy)
      self.game.plateau[xx][yy] = new_case
      new_case.selected = True
      new_case.draw()
      try:
        new_piece = self.game.get_new_piece(self)
      except (Exception,KeyboardInterrupt) as e:
        self.x, self.y = xx, yy
        self.game.plateau[xx][yy] = self
        self.selected = False
        self.draw()
        lm = self.game.partie.split()[-1]
        if lm.split(":")[2]:
          if self.couleur:
            nc = self.game.pc_bouffes[0].pop()
            nc.draw(col=COLOR_CASE_BLANC, just_bkg=True)
          else:
            nc = self.game.pc_bouffes[1].pop()
            nc.draw(col=COLOR_CASE_NOIR, just_bkg=True)
        else:
          nc = Case(self.game)
        nc.x, nc.y = mouv["x"], mouv["y"]
        self.game.plateau[nc.x][nc.y] = nc
        nc.draw()
        self.game.partie = " ".join(self.game.partie.split()[:-1])
        raise e
      self.game.score += (new_piece.point-1)*(1 if self.couleur else -1)
      new_piece.go_fast = self.go_fast
      self.game.plateau[self.x][self.y] = new_piece
      new_piece.x, new_piece.y = self.x, self.y
      if save:
        self.game.partie += ":"+new_piece.notation
      return new_case, new_piece
    else:
      return super().bouger(mouv, save)

class Cavalier(Piece):
  notation = "c"
  point = 3
  dessin = [
    0b000000000000000000000,
    0b000000000000000000000,
    0b000000000000000000000,
    0b000000000000000000000,
    0b000000011111000000000,
    0b000000011111110000000,
    0b000000011111111000000,
    0b000000011111111110000,
    0b000000011111111110000,
    0b000000011111111110000,
    0b000000011111111110000,
    0b000000011111100000000,
    0b000000011111100000000,
    0b000000011111100000000,
    0b000000011111100000000,
    0b000000011111100000000,
    0b000000011111100000000,
    0b000000111111111000000,
    0b000001111111111100000,
    0b000111111111111111000,
    0b000111111111111111000
  ]
  def get_mouvs(self):
    mouvs = []
    for i in 1,-1,2,-2:
      ii = i
      i += self.x
      for j in 1,-1,2,-2:
        jj = j
        j += self.y
        if abs(ii) != abs(jj) and is_in(i) and is_in(j):
          pc_test = self.game.plateau[i][j]
          if (not pc_test or col_is_diff(self,pc_test)) and self.test_good_mouv(i, j):
              mouvs.append(mouvement(i,j,pc_test))
    return mouvs

class Fou(Piece):
  notation = "f"
  point = 3
  dessin = [
    0b000000000000000000000,
    0b000000000010000000000,
    0b000000000111000000000,
    0b000000001111100000000,
    0b000000011111110000000,
    0b000000011111110000000,
    0b000000111111100000000,
    0b000000111111001000000,
    0b000000111110011000000,
    0b000000111110111000000,
    0b000000111111111000000,
    0b000000111111111000000,
    0b000000011111110000000,
    0b000000001111100000000,
    0b000000001111100000000,
    0b000000001111100000000,
    0b000000011111110000000,
    0b000000011111110000000,
    0b000001111111111100000,
    0b000111111111111111000,
    0b000111111111111111000
  ]
  mouvs = (-1,-1), (-1,1), (1,-1), (1,1)

class Tour(Piece):
  notation = "t"
  point = 5
  dessin = [
    0b000000000000000000000,
    0b000000000000000000000,
    0b000000000000000000000,
    0b000011100111001110000,
    0b000011100111001110000,
    0b000011111111111110000,
    0b000011111111111110000,
    0b000011111111111110000,
    0b000000111111111000000,
    0b000000011111110000000,
    0b000000011111110000000,
    0b000000011111110000000,
    0b000000011111110000000,
    0b000000011111110000000,
    0b000000011111110000000,
    0b000000011111110000000,
    0b000000011111110000000,
    0b000000111111111000000,
    0b000001111111111100000,
    0b000111111111111111000,
    0b000111111111111111000
  ]
  mouvs = (0,-1),(0,1),(-1,0),(1,0)
  def __init__(self, *args, **kwargs):
    self.boug = 0
    super().__init__(*args, **kwargs)
  def set_config(self, config):
    if len(config) == 2:
      super().set_config(config)
      self.boug = int(config[1])
    else:
      self.boug = int(config[0])
  def bouger(self, *args, **kwargs):
    if not self.boug:
      self.boug = self.game.cur_tour
    return super().bouger(*args, **kwargs)

class Dame(Piece):
  notation = "d"
  point = 9
  dessin = [
    0b000000000000000000000,
    0b000000000000000000000,
    0b000000000000000000000,
    0b000000000000000000000,
    0b000000000000000000000,
    0b000000000000000000000,
    0b000000000000000000000,
    0b001100000010000001100,
    0b011110000111000011110,
    0b111011111111111110111,
    0b110001111111111100011,
    0b110000000111000000011,
    0b111000000111000000111,
    0b011100000111000001110,
    0b001110000111000011100,
    0b000111000111000111000,
    0b000011000111000110000,
    0b000001100111001100000,
    0b000001100111001100000,
    0b000111111111111111000,
    0b000111111111111111000
  ]
  mouvs = Fou.mouvs + Tour.mouvs

NOT_INV = {"p": Pion, "c": Cavalier, "f": Fou, "t": Tour, "d": Dame}