import random
import sys
import time


import pygame as pg


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
    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
        self.vy = 2
        self.jump_num = 0
        self.j_lock = True

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
         #ジャンプを多重入力回避フラグ
        key_dct = pg.key.get_pressed() # 辞書型
        #スペース入力でキャラクターに上昇力を与える
        if key_dct[pg.K_SPACE]: 
            if self.j_lock:
                self.jump_num -= 10
                self.j_lock = False
        #位置更新
        self.rct.centery += self.vy + self.jump_num
        #画面外に出ないようにする
        if check_bound(self.rct, scr.rct) != (+1, +1): 
            self.rct.centery -= self.vy + self.jump_num
        #上昇力を減らす
        if self.jump_num < 0:
            self.jump_num += 1
            if self.vy + self.jump_num <= 0:
                self.j_lock = True

        self.blit(scr)                    


class Pipe:
    def __init__(self,scr):
        self.sfc = scr
        self.top = random.randint(0,450)
        self.bottom = random.randint(0,450)
        self.w = 50
        self.x = 1600
        self.speed = 2
        self.passed = False
        self.color = (0,0,0)

    def show(self):
        pg.draw.rect(self.sfc, self.color, (self.x, 0, self.w, self.top))
        pg.draw.rect(self.sfc, self.color, (self.x, self.top+200, self.w, self.top+1000))

    def update(self):
        self.x -= self.speed

    def hits(self,bird):
        if bird.rct.centery < self.top or bird.rct.centery > self.top+200:
            if bird.rct.centerx >= self.x and bird.rct.centerx <= self.x + self.w:
                return True
        return False


def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1

    return yoko, tate


def main():
    time1 = time.time()
    fonto = pg.font.Font(None, 80)
    clock =pg.time.Clock()

    #スクリーン　鳥
    scr = Screen("ふわふわ時間", (1600,900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 1.0, (800,450))
    kkt.update(scr)
    pipes = [Pipe(scr.sfc)]
    run = True  

    
    while True:        
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.update(scr)
        add_pipe = False    #パイプの作成を許可するフラグ
        rem = []            #画面外のパイプリスト
        for pipe in pipes:
            #画面から出たパイプをremに加える
            if pipe.x + pipe.w < 0: 
                    rem.append(pipe)
            #pipeが自キャラより左に行ったときに追加のパイプを作成する
            if not pipe.passed and pipe.x < kkt.rct.centerx:  
                pipe.passed = True #多重作成を回避するフラグ
                add_pipe = True   
            if pipe.hits(kkt):
                pipe.color = (255,0,0)

            pipe.update()

        if add_pipe:
            pipes.append(Pipe(scr.sfc))

        for r in rem:
            pipes.remove(r)

        for pipe in pipes:
            pipe.show()

        #時間表示
        time2 = time.time()
        time_str = fonto.render(str(round(time2-time1, 1)), True, (0, 0, 0))
        scr.sfc.blit(time_str, (1450, 0))
                    
        pg.display.update()
        clock.tick(1000)
        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

#https://qiita.com/igor-bond16/items/7c93477997953ed03b7c 参照