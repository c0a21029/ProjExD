import pygame as pg
import sys

def main():
    #時間
    clock = pg.time.Clock()
    clock.tick(1)
    #画面
    pg.display.set_caption("初めてのPyGame")
    scrn_sfc = pg.display.set_mode((800, 600))
    #画像
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 400, 300
    scrn_sfc.blit(tori_sfc, tori_rct)
    #文字
    fonto = pg.font.Font(None, 80)
    txt = fonto.render("aaa", True, "WHITE")
    scrn_sfc.blit(txt, (300, 200))

    pg.display.update()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            if event.type == pg.KEYDOWN and event.key == pg.K_F1:
                scrn_sfc = pg.display.set_mode((800, 600), pg.FULLSCREEN)
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                scrn_sfc = pg.display.set_mode((800,600))
if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()