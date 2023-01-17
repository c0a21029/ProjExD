
### インポート
import pygame
from pygame.locals import *
 
### モジュール初期化
pygame.init()
 
### 画面設定
surface = pygame.display.set_mode((640,400))
 
### 文字設定
font = pygame.font.Font("/Windows/Fonts/meiryo.ttc", 40)
 
### 文字色初期値
color = 255
 
### 色上下限フラグ
flag = 0
 
### 無限ループ
while True:
 
    ### 文字列設定(リスト)
    text = font.render("Hello World", True, (color,255,color))
 
    ### ベース画面塗りつぶし
    #surface.fill((0,0,0))
 
    ### テキスト画面表示
    surface.blit(text, (208,169))
 
    ### 画面更新
    pygame.display.update()
 
    ### 一定時間停止
    pygame.time.wait(5)
 
    ### 色上下限確認
    if   color <= 0:
        flag = 0
    elif color >= 255:
        flag = 1
 
    ### 文字色変更
    if flag == 0:
        color += 1
    else:
        color -= 1
 
    ### イベント処理
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            break
    else:
        continue
 
    ### whileループ終了
    break
 
### 終了処理
pygame.quit()