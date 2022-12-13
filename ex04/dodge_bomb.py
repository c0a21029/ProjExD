import pygame as pg
import sys
import random

def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko=-1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate=-1
    return yoko, tate
def main():
    #時間
    clock = pg.time.Clock()
    #ウィンドウ生成
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    #画像読み込み
    back_sfc = pg.image.load("fig/pg_bg.jpg")   #背景
    back_rct = back_sfc.get_rect()
    back_rct.center = 800, 450
    #鳥
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct) 
    #文字
    fonto = pg.font.Font(None, 80)
    txt = fonto.render("tinko", True, "WHITE")
    scrn_sfc.blit(txt, (300, 200))
    #爆弾
    bomb_sfc = pg.Surface((20, 20)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    
    
    #ループ
    vx, vy = +1, +1 #跳ね返りの変数
    while True:
        scrn_sfc.blit(back_sfc, back_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        #鳥移動
        key_dct = pg.key.get_pressed() # 辞書型
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if check_bound(tori_rct, scrn_rct) != (1, 1):
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        scrn_sfc.blit(tori_sfc, tori_rct) 
        #爆弾移動
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx*=yoko ; vy*=tate
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        #接触判定
        if tori_rct.colliderect(bomb_rct):
            return


        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()