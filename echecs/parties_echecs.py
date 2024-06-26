from pieces_echecs import *
from ion import keydown


COLOR_WARNING = (255, 125, 123)
COLOR_TXT = (99, 60, 0)
COLOR_BACKGROUND = (239, 154, 66)
COLOR_RED = (255, 0, 0)
COLOR_UNSELECT = (140, 134, 140)


def back():
    try:
        while keydown(5):
            pass
    except KeyboardInterrupt:
        back()

class Back(Exception):
    pass

class Forw(Exception):
    pass

class OnOff(Exception):
    pass

class Fin(Exception):
    pass

class Home(Exception):
    pass

keys = [[-1, 1] for i in range(6)]
last_verif = -1

def get_key(stop=False, ingame=False) -> int:
    global last_verif
    tt = monotonic()
    if stop and tt-last_verif < .05:
        return
    last_verif = tt
    while 1:
        if keydown(6):
            sleep(.3)
            raise Home()
        if keydown(8):
            sleep(.3)
            raise OnOff()
        if keydown(5):
            if keys[5][0] == -1:
                keys[5][0] = 0
                raise KeyboardInterrupt
        else:
            if not keys[5][0]:
                keys[5][0] = -1
        if keydown(48):
            raise Fin
        if stop:
            return
        for i in range(5):
            if keydown(i):
                if keys[i][0] == -1:
                    keys[i][0] = monotonic()
                    return i
                elif keys[i][1] and monotonic()-keys[i][0] > .3:
                    keys[i][0] = monotonic()
                    keys[i][1] = 0
                    return i
                elif not keys[i][1] and monotonic()-keys[i][0] > 0.07:
                    keys[i][0] = monotonic()
                    return i
            else:
                if keys[i][0] != -1:
                    keys[i] = [-1, 1]
        if ingame and keydown(12):
            while keydown(12):
                pass
            raise Back()
        if ingame and keydown(17):
            while keydown(17):
                pass
            raise Forw()

def mouv_select(plt: list[list], x: int, y: int, k: int) -> tuple[int, int]:
    plt_inv = [[plt[j][i] for j in range(len(plt[0]))] for i in range(len(plt))]
    def mvm(x, y, p, pi, r, pri=True):
        if pri:
            if r[0] < 0 and any(p[x][max(y-len(plt[0])+1,0):y]) or r[0] > 0 and any(p[x][y+1:min(y+len(plt[0])-1,len(plt[0]))]):
                for i in range(y+r[0], *r[1:]):
                    if p[x][i]:
                        return x, i
        for i in range(y+r[0], *r[1:]):
            if any(pi[i]):
                for j in range(max(x, len(plt[0])-1-x)+1):
                    for s in 1,-1:
                        if is_in(x+j*s) and pi[i][x+j*s]:
                            return x+j*s,i
        return x,y
    if sens["inv"] == -1:
        if not k:
            k = 1
        elif k == 1:
            k = 0
        elif k == 2:
            k = 3
        elif k == 3:
            k = 2
    if not k:
        if sens["y"]:
            k = 3
    elif k == 3:
        if sens["y"]:
            k = 0
    elif k == 1:
        if sens["x"]:
            k = 2
    elif k == 2:
        if sens["x"]:
            k = 1
    if not k:
        if sens["inv"] == -1:
            pri = True
        else:
            pri = False
        return mvm(x, y, plt, plt_inv, (-1,-1,-1), pri)
    elif k == 3:
        if sens["inv"] == -1:
            pri = True
        else:
            pri = False
        return mvm(x, y, plt, plt_inv, (1,len(plt[0])), pri)
    elif k == 2:
        if sens["inv"] == 1:
            pri = True
        else:
            pri = False
        return list(mvm(y, x, plt_inv, plt, (1,len(plt[0])), pri))[::-1]
    elif k == 1:
        if sens["inv"] == 1:
            pri = True
        else:
            pri = False
        return list(mvm(y, x, plt_inv, plt, (-1, -1, -1), pri))[::-1]
    else:
        return x,y

def fin():
    raise Fin()

class Settings:
    def __init__(self, game, warnings=True, score=True, chang=True):
        self.game, self.warnings, self.score, self.chang = game, warnings, score, chang
        self.senss = [
            {0: (1,-1), 1: (1,-1), "x": 1, "y": 0, "inv": -1},
            {0: (1,-1), 1: (1,-1), "x": 0, "y": 1, "inv": -1}
        ]
        self.base = {i: getattr(sens[i], "copy", lambda:sens[i])() for i in sens}
    
    def home(self):
        reps = (" Nouvelle partie", "Continuer partie", " Charger partie ", "   Parametres   ", "     Quitter    ")
        actions = (self.game.start, self.game.mainloop, self.game.start_with_config, self.params, fin)
        selection = 0
        draw(65, 25, 190, 190, COLOR_BACKGROUND)
        for i,val in enumerate(reps):
            draw_txt(val, 80, 40+i*35, COLOR_TXT, COLOR_BACKGROUND)
        k = -1
        while k != 4:
            draw_txt(">"+reps[selection]+"<", 70, 40+selection*35, COLOR_RED, COLOR_BACKGROUND)
            try:
                k = get_key()
            except OnOff:
                self.off()
                draw(65, 25, 190, 190, COLOR_BACKGROUND)
                for i,val in enumerate(reps):
                    draw_txt(val, 80, 40+i*35, COLOR_TXT, COLOR_BACKGROUND)
                continue
            except (KeyboardInterrupt,Home):
                back()
                if getattr(self.game, "rois", False) and all(self.game.rois):
                    selection = 1
                    break
                else:
                    raise Fin()
            draw_txt(" "+reps[selection]+" ", 70, 40+selection*35, COLOR_TXT, COLOR_BACKGROUND)
            selection += (k==2) - (k==1) + (k==3) - (k==0)
            selection %= len(reps)
        try:
            actions[selection]()
        except (Fin, Home, KeyboardInterrupt) as e:
            raise e
        except Exception as e:
            self.erreur(e)
    
    def params(self):
        draw(65, 25, 190, 190, COLOR_BACKGROUND)
        selection = 0
        sousselect = 0
        plt = Pion(self.game, 3, 3, 1), Pion(self.game, 3, 4, 0), Pion(self.game, 4, 3, 1), Pion(self.game, 4, 4, 0)
        pct = [1,-1], [1,1], [-1,-1], [-1,1]
        pltt = {"x": 0, "y": 0, "inv": 1}, {"x": 0, "y": 1, "inv": -1}, {"x": 1, "y": 1, "inv": 1}, {"x": 1, "y": 0, "inv": -1}
        avs = [0]*3
        if sousselect == 1:
            achang = self.senss[1]
        elif sousselect == 2:
            achang = self.senss[0]
        else:
            achang = self.base
        for i in range(4):
            plt_test = pltt[i]
            if achang["x"] == plt_test["x"] and achang["y"] == plt_test["y"] and achang["inv"] == plt_test["inv"]:
                avs[0] = i
            if achang[1] == pct[i]:
                avs[1] = i
            if achang[0] == pct[i]:
                avs[2] = i
        options = ((" Ne pas changer ", " Changer plateau"), (" Tout les tours ", "   Tour blanc   ", "    Tour noir   "), "Tourner plateau", " Tourner blancs", " Tourner noirs ")
        cur_aff = (options[0][self.chang], options[1][sousselect]) + options[2:]
        dists = (35, 58, 135, 160, 185)
        draw_txt("<"+cur_aff[0]+">", 70, 35, COLOR_RED, COLOR_BACKGROUND)
        draw_txt(cur_aff[1], 80, 58, COLOR_TXT if self.chang else COLOR_UNSELECT, COLOR_BACKGROUND)
        for i in plt:
            i.draw(decy=-15)
        for i,val in enumerate(options[2:]):
            draw_txt(val, 80, 135+25*i, COLOR_TXT, COLOR_BACKGROUND)
        while 1:
            try:
                k = get_key()
            except OnOff:
                self.off()
                continue
            draw_txt(" "+cur_aff[selection]+" ", 70, dists[selection], COLOR_TXT, COLOR_BACKGROUND)
            selection += (k==2) - (k==1)
            selection %= 5
            if selection == 1 and not self.chang:
                selection += (k==2) - (k==1)
            if k in (0,3,4):
                if selection == 0:
                    self.chang = not self.chang
                    if not self.chang:
                        sousselect = 0
                        draw_txt(options[1][0], 80, dists[1], COLOR_UNSELECT, COLOR_BACKGROUND)
                    else:
                        draw_txt(options[1][sousselect], 80, dists[1], COLOR_TXT, COLOR_BACKGROUND)
                elif selection == 1:
                    sousselect += (k==4) + (k==3) - (k==0)
                    sousselect %= 3
                    if sousselect == 1:
                        achang = self.senss[1]
                    elif sousselect == 2:
                        achang = self.senss[0]
                    else:
                        achang = self.base
                    for i in range(4):
                        plt_test = pltt[i]
                        if achang["x"] == plt_test["x"] and achang["y"] == plt_test["y"] and achang["inv"] == plt_test["inv"]:
                            avs[0] = i
                        if achang[1] == pct[i]:
                            avs[1] = i
                        if achang[0] == pct[i]:
                            avs[2] = i
                else:
                    avs[selection-2] += (k==4) + (k==3) - (k==0)
                    avs[selection-2] %= 4
                if sousselect == 1:
                    achang = self.senss[1]
                elif sousselect == 2:
                    achang = self.senss[0]
                else:
                    achang = self.base
                achang.update({1: pct[avs[1]], 0: pct[avs[2]]})
                achang.update(pltt[avs[0]])
                sens.update(achang)
            cur_aff = (options[0][self.chang], options[1][sousselect]) + options[2:]
            for i in plt:
                i.draw(decy=-15)
            draw_txt("<"+cur_aff[selection]+">", 70, dists[selection], COLOR_RED, COLOR_BACKGROUND)
    
    def off(self):
        draw(0, 0, 320, 222, (0,)*3)
        while 1:
            try:
                k = get_key()
            except (Exception,KeyboardInterrupt) as e:
                back()
                if type(e) is OnOff:
                    self.game.draw_all_plt()
                    return
    
    def erreur(self, *messages):
        print("------ Error ------")
        if messages:
            for message in messages:
                print(message)
        else:
            print("Unknow Error")
        print("-------------------")
        draw(10, 70, 300, 60, COLOR_RED)
        if messages:
            for i,message in enumerate(messages):
                draw_txt(str(message), 30, 75+20*i, COLOR_WARNING, COLOR_RED)
        else:
            draw_txt("Unknow Error", 60, 90, COLOR_WARNING, COLOR_RED)
        try:
            get_key()
        except OnOff:
            self.off()
        except KeyboardInterrupt:
            back()
        except:
            pass


LIMIT_PARTIE = 250

partie = [
# Coller ici les lignes
# de la partie que vous
# voulez sauvegarder






]