import pygame as pg
import random
import sys
import time


class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:
    key_delta = {
        pg.K_UP:    [0, -2],
        pg.K_DOWN:  [0, +2],
        pg.K_LEFT:  [-2, 0],
        pg.K_RIGHT: [+2, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0] 
                self.rct.centery += delta[1] 
            if check_bound(self.rct, scr.rct) != (+1, +1, 1):
                self.rct.centerx -= delta[0] 
                self.rct.centery -= delta[1] 
        self.blit(scr)                    


class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate, up_speed = check_bound(self.rct, scr.rct)
        self.vx *= yoko * up_speed
        self.vy *= tate * up_speed
        self.blit(scr)


#挙動の異なる爆弾
class Bomb2:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx = random.randint(1,10)
        self.vy = random.randint(1,3)

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate, up_speed = check_bound(self.rct, scr.rct)
        self.vx *= yoko * up_speed
        self.vy *= tate * up_speed
        self.blit(scr)


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    up_speed =1

    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
        up_speed =1.2
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
        up_speed = 1.2

    return yoko, tate, up_speed


def main():
    time1 = time.time()
    fonto = pg.font.Font(None, 80)
    clock =pg.time.Clock()

    #スクリーン　鳥
    scr = Screen("逃げろ！こうかとん", (1600,900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900,400))
    kkt.update(scr)

    bkd_lis = []
    for i in range(3):
        vx = random.choice([-1, +1])
        vy = random.choice([-1, +1])
        bkd_lis.append(Bomb((255, 0, 0), 10, (vx, vy), scr))

    bkd_lis2 = []
    for i in range(1):
        vx = random.choice([-1, +1])
        vy = random.choice([-1, +1])
        bkd_lis.append(Bomb2((25, 250, 110), 50, (vx, vy), scr))
    
    life=3
    while True:        
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.update(scr)

        #接触時アクション
        for bkd in bkd_lis:
            bkd.update(scr)
            if kkt.rct.colliderect(bkd.rct):
                if life == 3: #1度目の接触判定
                    kkt.rct.center = 900, 400
                    kkt.sfc = pg.image.load("fig/8.png")
                    kkt.sfc = pg.transform.rotozoom(kkt.sfc, 0, 1.8)
                if life == 2: #2度目の接触判定
                    kkt.rct.center = 900, 400
                    kkt.sfc = pg.image.load("fig/2.png")
                    kkt.sfc = pg.transform.rotozoom(kkt.sfc, 0, 1.8)
                if life == 1: #3度目の接触判定
                    return
                bkd_lis.append(Bomb((255, 0, 0), 10, (vx, vy), scr))
                life -= 1

        #残機表示
        txt = fonto.render("Life:"+str(life), True, (0, 0, 0))
        scr.sfc.blit(txt, (0, 0))

        #時間表示
        time2 = time.time()
        time_str = fonto.render(str(round(time2-time1, 1)), True, (0, 0, 0))
        scr.sfc.blit(time_str, (1500, 0))
                    
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()