from parties_echecs import *

class Game(PreGame):
  def start(self, go=True):
    self.__init__()
    self.plateau = [[Case(self,x,y) for y in range(8)] for x in range(8)]
    self.last_tour = [None]*2
    self.pc_bouffes = [[],[]]
    self.tour = 1
    self.cur_tour = 0
    self.score = 0
    self.depl = 0
    self.partie = ""
    for x in range(8):
      self.plateau[x][1] = Pion(self, x, 1, 1)
      self.plateau[x][6] = Pion(self, x, 6, 0)
    for sgn in -1,1:
      self.plateau[int(3.5+3.5*sgn)][0] = Tour(self, int(3.5+3.5*sgn), 0, 1)
      self.plateau[int(3.5+3.5*sgn)][7] = Tour(self, int(3.5+3.5*sgn), 7, 0)
      self.plateau[int(3.5+2.5*sgn)][0] = Cavalier(self, int(3.5+2.5*sgn), 0, 1)
      self.plateau[int(3.5+2.5*sgn)][7] = Cavalier(self, int(3.5+2.5*sgn), 7, 0)
      self.plateau[int(3.5+1.5*sgn)][0] = Fou(self, int(3.5+1.5*sgn), 0, 1)
      self.plateau[int(3.5+1.5*sgn)][7] = Fou(self, int(3.5+1.5*sgn), 7, 0)
    self.plateau[3][0] = Dame(self, 3, 0, 1)
    self.plateau[3][7] = Dame(self, 3, 7, 0)
    self.plateau[4][0] = Roi(self, 4, 0, 1, self.plateau[0][0], self.plateau[7][0])
    self.plateau[4][7] = Roi(self, 4, 7, 0, self.plateau[0][7], self.plateau[7][7])
    self.rois = [self.plateau[4][7], self.plateau[4][0]]
    if go:
      self.mainloop()
  def start_with_config(self, go=True):
    self.__init__()
    config = sum(partie, "")
    try:
      self.plateau = [[Case(self,x,y) for y in range(8)] for x in range(8)]
      self.last_tour = [None]*2
      self.pc_bouffes = [[],[]]
      self.rois = [None, None]
      self.score = 0
      plateau, pb_bouuffes, vall, self.partie = config.split("|")
      for x,ligne in enumerate(plateau.split("/")):
        for y,obj in enumerate(ligne.split(" ")):
          if obj:
            args = obj.split(",")
            np = NOT_INV[args[0].lower()](self, x, y, args[0] not in NOT_INV, config=args[1:])
            if type(np) is Roi:
              self.rois[args[0] not in NOT_INV] = np
            else:
              self.score += np.point * (1 if np.couleur else -1)
            self.plateau[x][y] = np
      for i,lst in enumerate(pb_bouuffes.split("/")):
        for j,pc in enumerate(lst.split()):
          pc = pc.split(",")
          self.pc_bouffes[i].append(NOT_INV[pc[0].lower()](self, j%8, 8.3+(j//8)if i else -1.3-(j//8), i, config=pc[1:]))
      for obj in self.rois:
        xx, yy = obj.big_tour
        if yy == int(yy):
          xx, yy = int(xx), int(yy)
          obj.big_tour = self.plateau[xx][yy]
        else:
          if obj.couleur:
            obj.big_tour = self.pc_bouffes[1][int(xx+8*(yy==-2.3))]
          else:
            obj.big_tour = self.pc_bouffes[0][int(xx+8*(yy==9.3))]
        xx, yy = obj.small_tour
        if yy == int(yy):
          xx, yy = int(xx), int(yy)
          obj.small_tour = self.plateau[xx][yy]
        else:
          if obj.couleur:
            obj.small_tour = self.pc_bouffes[1][int(xx+8*(yy==-2.3))]
          else:
            obj.small_tour = self.pc_bouffes[0][int(xx+8*(yy==9.3))]
      self.tour, self.cur_tour, self.depl = map(int, vall.split())
    except Exception as e:
      self.settings.erreur("Erreur chargement partie :", "  La partie est corrompue" if config else "  La partie n'existe pas", repr(e))
      return self.start(go)
    if go:
      self.mainloop()
  def start_all(self):
    try:
      self.draw_all_plt()
      while 1:
        try:
          self.settings.home()
        except (Home,KeyboardInterrupt):
          back()
          pass
    except Fin:
      if getattr(self, "rois", False) and all(self.rois):
        print("Pour sauvegarder la partie,\ncopiez les lignes suivantes et\ncollez-les entres les crochets\ndans le script parties_echecs")
        print(game)
  def get_pcs_can_mouvs(self):
    return [j for i in self.plateau for j in i if (j.couleur==self.tour and j.get_mouvs())]
  def verif_bouf(self, mouv, save=True):
    if mouv["pb"]:
      if save:
        self.partie += ":"+mouv["pb"].notation+str(mouv["pb"].x)+str(mouv["pb"].y)
      new_case = Case(self, mouv["pb"].x, mouv["pb"].y)
      self.plateau[mouv["pb"].x][mouv["pb"].y] = new_case
      new_case.draw()
      len_pb = len(self.pc_bouffes[mouv["pb"].couleur])
      mouv["pb"].x = len_pb % 8
      if not mouv["pb"].couleur:
        mouv["pb"].y = -1.3-(len_pb//8)
        mouv["pb"].draw(col=COLOR_CASE_BLANC, psens=sens[1])
      else:
        mouv["pb"].y = 8.3 + (len_pb//8)
        mouv["pb"].draw(col=COLOR_CASE_NOIR, psens=sens[0])
      self.pc_bouffes[mouv["pb"].couleur].append(mouv["pb"])
      self.score += mouv["pb"].point * (-1 if mouv["pb"].couleur else 1)
    else:
      if save:
        self.partie += ":"
  def verif_exception(self):
    try:
      get_key(True)
    except (OnOff):
      self.settings.off()
  def draw_all_plt(self):
    if sens["y"]:
      col1, col2 = COLOR_CASE_NOIR, COLOR_CASE_BLANC
    else:
      col1, col2 = COLOR_CASE_BLANC, COLOR_CASE_NOIR
    draw(0, 0, 59, 222, col1)
    draw(261, 0, 59, 222, col2)
    for i in self.pc_bouffes[0]:
      self.verif_exception()
      i.draw(col=COLOR_CASE_BLANC, psens=sens[1])
    for i in self.pc_bouffes[1]:
      self.verif_exception()
      i.draw(col=COLOR_CASE_NOIR, psens=sens[0])
    draw(59, 0, 202, 19, COLOR_BACKGROUND)
    draw_txt("ECHECS by Caucaucybu", 60, 0, COLOR_TXT, COLOR_BACKGROUND)
    draw(59, 19, 202, 203, COLOR_TXT)
    for i in self.plateau:
      for j in i:
        self.verif_exception()
        j.draw()
    self.verif_exception()
    if self.mouvs:
      for pos in self.mouvs:
        rond(pos["x"], pos["y"])
      select(*self.selected)
    elif self.selected:
      x, y = self.selected
      self.plateau[x][y].draw(is_select=True)
  def get_new_piece(self, pc):
    if self.is_forw:
      return self.pc_prep
    if pc.couleur:
      colback = COLOR_CASE_NOIR
      pcs = [Dame(self,2,4,1), Cavalier(self,3,4,1), Tour(self,4,4,1), Fou(self,5,4,1)]
      pcs_plt = [[Case(self, i, j) for j in range(8)] for i in range(8)] 
      for i in pcs:
        pcs_plt[i.x][i.y] = i
      x, y = get_ver_coords(2, 4)[::sens["inv"]]
    else:
      colback = COLOR_CASE_BLANC
      pcs = [Dame(self,2,3,0), Cavalier(self,3,3,0), Tour(self,4,3,0), Fou(self,5,3,0)]
      pcs_plt = [[Case(self, i, j) for j in range(8)] for i in range(8)] 
      for i in pcs:
        pcs_plt[i.x][i.y] = i
      x, y = get_ver_coords(2, 3)[::sens["inv"]]
    if sens["y"]:
      if sens["x"]:
        draw(*[x+30, y+30][::sens["inv"]]+[-35, -25*4-10][::sens["inv"]]+[colback])
      else:
        draw(*[x+30, y-5][::sens["inv"]]+[-35, 25*4+10][::sens["inv"]]+[colback])
    else:
      if sens["x"]:
        draw(*[x-5, y+30][::sens["inv"]]+[35, -25*4-10][::sens["inv"]]+[colback])
      else:
        draw(*[x-5, y-5][::sens["inv"]]+[35, 25*4+10][::sens["inv"]]+[colback])
    for i in pcs:
      self.verif_exception()
      i.draw(col=colback)
    xx, yy = pcs[0].x, pcs[0].y
    pcs[0].draw(col=colback, is_select=True)
    k = -1
    try:
      while k != 4:
        try:
          k = get_key(ingame=True)
        except OnOff:
          self.settings.off()
          if sens["y"]:
            if sens["x"]:
              draw(*[x+30, y+30][::sens["inv"]]+[-35, -25*4-10][::sens["inv"]]+[colback])
            else:
              draw(*[x+30, y-5][::sens["inv"]]+[-35, 25*4+10][::sens["inv"]]+[colback])
          else:
            if sens["x"]:
              draw(*[x-5, y+30][::sens["inv"]]+[35, -25*4-10][::sens["inv"]]+[colback])
            else:
              draw(*[x-5, y-5][::sens["inv"]]+[35, 25*4+10][::sens["inv"]]+[colback])
          for i in pcs:
            self.verif_exception()
            i.draw(col=colback)
          pcs_plt[xx][yy].draw(col=colback, is_select=True)
          continue
        last_x, last_y = xx, yy
        xx, yy = mouv_select(pcs_plt, xx, yy, k)
        pcs_plt[last_x][last_y].draw(col=colback)
        pcs_plt[xx][yy].draw(col=colback, is_select=True)
    except (Forw, Back, KeyboardInterrupt) as e:
      back()
      for i in range(1,7):
        for j in range(2,6):
          self.verif_exception()
          self.plateau[i][j].draw()
      raise e
    for i in range(1,7):
      for j in range(2,6):
        self.verif_exception()
        self.plateau[i][j].draw()
    return pcs_plt[xx][yy]
  def frame(self):
    draw_txt(" "*5, 265-260*sens["y"], 2, COLOR_WARNING, COLOR_CASE_NOIR)
    draw_txt(" "*5, 5+260*sens["y"], 2, COLOR_WARNING, COLOR_CASE_BLANC)
    if self.settings.score and self.score:
      if self.score > 0:
        draw_txt(" +"+("" if self.score//10 else " ")+str(self.score), 5+260*sens["y"], 2, COLOR_TXT, COLOR_CASE_BLANC)
      else:
        draw_txt(" +"+("" if self.score//10 else " ")+str(abs(self.score)), 265-260*sens["y"], 2, COLOR_TXT, COLOR_CASE_NOIR)
    if self.settings.warnings:
      if self.tour:
        if self.rois[1].est_en_echec():
          draw_txt("ECHEC", 5+260*sens["y"], 2, COLOR_WARNING, COLOR_CASE_BLANC)
      else:
        if self.rois[0].est_en_echec():
          draw_txt("ECHEC", 265-260*sens["y"], 2, COLOR_WARNING, COLOR_CASE_NOIR)
    all_pcs = [], []
    for lign in self.plateau:
      for obj in lign:
        if obj:
          all_pcs[obj.couleur].append(obj.notation)
    result = ""
    if len(all_pcs[0]) == len(all_pcs[1]) == 1:
      result = "NULLE"
    else:
      for i,j in (1,0),(0,1):
        if len(all_pcs[i]) == 1:
          if len(all_pcs[j]) == 3 and all_pcs[j].count("c") == 2:
            result = "NULLE"
          elif len(all_pcs[j]) == 2 and ("c" in all_pcs[j] or "f" in all_pcs[j]):
            result = "NULLE"
    if not self.get_pcs_can_mouvs():
      result = " PAT "
    if self.rois[self.tour].est_en_echec() and result == " PAT ":
      if self.tour:
        draw_txt(" MAT ", 5+260*sens["y"], 2, COLOR_WARNING, COLOR_CASE_BLANC)
      else:
        draw_txt(" MAT ", 265-260*sens["y"], 2, COLOR_WARNING, COLOR_CASE_NOIR)
    else:
      draw_txt(result, 265-260*sens["y"], 2, COLOR_WARNING, COLOR_CASE_NOIR)
      draw_txt(result, 5+260*sens["y"], 2, COLOR_WARNING, COLOR_CASE_BLANC)
    return result + " "
  def forw_pos(self):
    for i in self.last_tour:
      if i != None:
        i.selected = False
        i.draw()
    if len(self.partie.split()) == self.cur_tour-self.depl:
      return
    if self.tour:
      self.tour = 0
    else:
      self.tour = 1
    next_mouv = self.partie.split()[self.cur_tour-self.depl].split(":")
    dep_x, dep_y = map(int, next_mouv[0])
    arr_x, arr_y = map(int, next_mouv[1])
    pc_to_move = self.plateau[dep_x][dep_y]
    if next_mouv[2]:
      xx, yy = map(int, next_mouv[2][1:])
      pc_bouf = self.plateau[xx][yy]
    else:
      pc_bouf = None
    try:
      self.pc_prep = NOT_INV[next_mouv[3]](self, arr_x, arr_y, pc_to_move.couleur)
      self.is_forw = True
    except IndexError:
      pass
    self.last_tour = pc_to_move.bouger(mouvement(arr_x, arr_y, pc_bouf), save=False)
    self.is_forw = False
    self.cur_tour += 1
  def back_pos(self):
    if self.cur_tour-self.depl:
      self.cur_tour -= 1
    else:
      return
    if self.tour:
      self.tour = 0
    else:
      self.tour = 1
    last_mouv = self.partie.split()[self.cur_tour-self.depl].split(":")
    dep_x, dep_y = map(int, last_mouv[0])
    arr_x, arr_y = map(int, last_mouv[1])
    pc = self.plateau[arr_x][arr_y]
    pc.x, pc.y = dep_x, dep_y
    self.plateau[dep_x][dep_y] = pc
    pc.selected = False
    pc.draw()
    nc = Case(self, arr_x, arr_y)
    self.plateau[arr_x][arr_y] = nc
    nc.selected = False
    nc.draw()
    try:
      if last_mouv[3]:
        self.score -= (NOT_INV[last_mouv[3]].point-1)*(1 if self.tour else -1)
        newpc = Pion(self, dep_x, dep_y, pc.couleur)
        newpc.go_fast = pc.go_fast
        self.plateau[dep_x][dep_y] = newpc
        newpc.draw()
    except IndexError:
      pass
    if last_mouv[2]:
      if pc.couleur:
        pc_bouf = self.pc_bouffes[0].pop()
      else:
        pc_bouf = self.pc_bouffes[1].pop()
      pc_bouf.draw(just_bkg=True, col=COLOR_CASE_NOIR if pc_bouf.couleur else COLOR_CASE_BLANC)
      self.score -= pc_bouf.point * (-1 if pc_bouf.couleur else 1)
      pc_bouf.x, pc_bouf.y = map(int, last_mouv[2][1:])
      self.plateau[pc_bouf.x][pc_bouf.y] = pc_bouf
      pc_bouf.draw()
    if type(pc) is Pion:
      if abs(dep_x-arr_x) == 2:
        pc.go_fast = False
    elif type(pc) is Roi:
      if self.cur_tour == pc.boug:
        pc.boug = 0
      if dep_x - arr_x == 2:
        t = pc.big_tour
        t.x = 0
        t.boug = 0
        self.plateau[t.x][t.y] = t
        t.draw()
        self.plateau[arr_x+1][t.y] = Case(self, arr_x+1, arr_y)
        self.plateau[arr_x+1][t.y].draw()
      elif arr_x - dep_x == 2:
        t = pc.small_tour
        t.x = 7
        t.boug = 0
        self.plateau[t.x][t.y] = t
        t.draw()
        self.plateau[arr_x-1][t.y] = Case(self, arr_x-1, arr_y)
        self.plateau[arr_x-1][t.y].draw()
    elif type(pc) is Tour:
      if pc.boug == self.cur_tour:
        pc.boug = 0
    if self.cur_tour-self.depl:
      last_mouv = self.partie.split()[self.cur_tour-self.depl-1].split(":")
      dep_x, dep_y = map(int, last_mouv[0])
      arr_x, arr_y = map(int, last_mouv[1])
      self.last_tour = [self.plateau[dep_x][dep_y], self.plateau[arr_x][arr_y]]
    else:
      self.last_tour = [None] *2
    self.frame()
  def mainloop(self):
    if not getattr(self, "rois", False) or not all(self.rois):
      self.start_with_config(False)
    if not self.settings.chang:
      self.draw_all_plt()
    while 1:
      if self.frame() == " PAT  " and self.settings.chang:
        sens.update(self.settings.base)
        self.draw_all_plt()
      elif self.settings.chang:
        sens.update(self.settings.senss[self.tour])
        self.draw_all_plt()
      while self.frame():
        for i in self.last_tour:
          if i != None:
            i.selected = True
            i.draw()
        pcs = self.get_pcs_can_mouvs()
        if pcs:
          pcs_plt = [[Case(i,j) for j in range(8)] for i in range(8)]
          for i in pcs:
            pcs_plt[i.x][i.y] = i
          x, y = pcs[0].x, pcs[0].y
          pcs[0].draw(is_select=True)
          self.selected = x, y
        k = -1
        try:
          while k != 4:
            try:
              k = get_key(ingame=True)
            except OnOff:
              self.settings.off()
              continue
            if pcs:
              last_x, last_y = x, y
              x, y = mouv_select(pcs_plt, x, y, k)
              self.selected = x, y
              self.plateau[last_x][last_y].draw()
              self.plateau[x][y].draw(is_select=True)
        except (Back, Forw) as e:
          if pcs:
            self.plateau[x][y].draw()
          self.selected = None
          if type(e) is Back:
            self.back_pos()
          else:
            self.forw_pos()
          continue
        pc_selected = self.plateau[x][y]
        pc_selected.selected = True
        pc_selected.draw()
        for i in self.last_tour:
          if i is not None:
            i.selected = False
            i.draw()
        mouvs = pc_selected.get_mouvs()
        self.mouvs = mouvs
        mouvs_plt = [[0]*8 for i in range(8)]
        for i in mouvs:
          mouvs_plt[i["x"]][i["y"]] = i
          rond(i["x"], i["y"])
        k = -1
        x, y = mouvs[0]["x"], mouvs[0]["y"]
        self.selected = x, y
        select(x, y)
        try:
          while k != 4:
            try:
              k = get_key(ingame=True)
            except OnOff:
              self.settings.off()
              continue
            last_x, last_y = x, y
            x, y = mouv_select(mouvs_plt, x, y, k)
            self.selected = x, y
            self.plateau[last_x][last_y].draw()
            rond(last_x, last_y)
            select(x, y)
          self.selected = None
          self.mouvs = []
          for i in mouvs:
            self.verif_exception()
            self.plateau[i["x"]][i["y"]].draw()
          self.partie = " ".join(self.partie.split()[:self.cur_tour-self.depl])
          self.partie += " "
          if self.partie.startswith(" "):
            self.partie = self.partie[1:]
          if len(self.partie) > LIMIT_PARTIE:
            ind_deb = 0
            dec = 0
            while len(self.partie)-ind_deb > LIMIT_PARTIE:
              ind_deb += 1
              if self.partie[ind_deb] == " ":
                dec += 1
            while self.partie[ind_deb] != " ":
              ind_deb += 1
              if self.partie[ind_deb] == " ":
                dec += 1
                break
            self.depl += dec
            self.partie = self.partie[ind_deb+1:]
          self.last_tour = pc_selected.bouger(mouvs_plt[x][y])
        except (KeyboardInterrupt,Back,Forw) as e:
          back()
          self.selected = None
          self.mouvs = []
          for i in mouvs:
            self.verif_exception()
            self.plateau[i["x"]][i["y"]].draw()
          pc_selected.selected = False
          pc_selected.draw()
          if type(e) is Back:
            self.back_pos()
          elif type(e) is Forw:
            self.forw_pos()
          continue
        self.cur_tour += 1
        if self.tour:
          self.tour = 0
        else:
          self.tour = 1
        break
        

game = Game()
game.start_all()