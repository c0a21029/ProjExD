import pygame as pg
import sys
import random
#画面領域から出ないようにする関数
def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko=-1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate=-1
    return yoko, tate
#ライフが0になった時に動作を一時停止する関数
def retry():
    while True:
        for event in pg.event.get(): 
            if event.type == pg.QUIT: return    #これがないと閉じれない
            if event.type == pg.KEYDOWN and event.key == pg.K_r:    #rでmain()を再起動する
                main()
                return
                
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
    #メッセージ
    fonto = pg.font.Font(None, 80)
    message = fonto.render("Press[r] to try again", True, (0, 0, 0))
    scrn_sfc.blit(message, (350,0))
    #爆弾
    bomb_sfc = pg.Surface((20, 20)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)

    vx, vy, life = 1, 1, 2 #跳ね返りの変数と体力
    #ループ開始地点
    while True:
        scrn_sfc.blit(back_sfc, back_rct)
        scrn_sfc.blit(message, (350,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        #鳥移動
        dex = 1 #移動速度の変数
        key_dct = pg.key.get_pressed() # 辞書型
        if key_dct[pg.K_LSHIFT]: #移動速度UP
            dex *= 2
        if key_dct[pg.K_r]:      #リトライ
            main()
            return
        if key_dct[pg.K_UP]:
            tori_rct.centery -= dex
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += dex
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= dex
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += dex
        if check_bound(tori_rct, scrn_rct) != (1, 1):
            if key_dct[pg.K_UP]:
                tori_rct.centery += dex
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= dex
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += dex
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= dex
            
        scrn_sfc.blit(tori_sfc, tori_rct) 
        #爆弾移動
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        if check_bound(bomb_rct, scrn_rct) != (1, 1):
            vx*=1.2
            vy*=1.2
        vx*=yoko ; vy*=tate
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)  
        #接触判定
        if tori_rct.colliderect(bomb_rct):
            if life <= 2: #一度目の接触判定
                tori_rct.center = 900, 400
                tori_sfc = pg.image.load("fig/8.png")
                tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 1.8)
                life -=1
            if life <= 0: #二度目の接触判定
                retry()
                return
        #残機の表示  
        txt = fonto.render("Life:"+str(life), True, (0, 0, 0))
        scrn_sfc.blit(txt, (0, 0))
        #表示のためのあれこれ
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()