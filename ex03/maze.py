import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
import time
#キー押下アクション
def key_down(event):
    global key
    key=event.keysym
#キーリリースアクション
def key_up(event):
    global key
    key=""

def main_proc():
    #時間の表示
    time_c()
    #移動
    global cx,cy,mx,my
    if key == "Up":my-=1
    if key == "Down":my+=1
    if key == "Right":mx+=1
    if key == "Left":mx-=1
    if key == "g":mx=13;my=7   #ゴールまで瞬間移動できます
    if maze_lst[mx][my]==1: #壁判定
        if key == "Up":my+=1
        if key == "Down":my-=1
        if key == "Right":mx-=1
        if key == "Left":mx+=1
    cx,cy=mx*100+50,my*100+50
    canv.coords("hato", cx,cy)
    #ゴール判定
    if mx==13 and my==7:
        time_end=time.time()
        total_time=str(round(time_end-time_start, 2))      #タイム取得
        tkm.showinfo("クリア", f"！！！！！ゴーーーーーーール！！！！！\nクリアタイム：{total_time}秒")
        root.after_cancel(jid)

    jid=root.after(100, main_proc)
        
#現在のタイムを表示        
def time_c():
    canv.create_rectangle(1100, 0, 1500, 100, fill="pink")
    time2=time.time()
    time_now=str(round(time2-time_start, 1))
    canv.create_text(1300, 50, text=time_now+" 秒", font=("", 60))

if __name__=="__main__":
    #ウィンドウ生成
    root=tk.Tk()
    root.title("迷えるこうかとん")
    canv=tk.Canvas(root, width=1500, height=900, bg="black")
    #迷路生成
    maze_lst=mm.make_maze(15, 9)
    mm.show_maze(canv,maze_lst)
    canv.create_rectangle(100, 100, 200, 200, fill="blue")    #スタート地点の色
    canv.create_rectangle(1300, 700, 1400, 800, fill="red")    #ゴールの色
    #画像読み込み～表示
    tori=tk.PhotoImage(file="fig/8.png")
    mx,my=1,1
    cx,cy=mx*100+50,my*100+50
    canv.create_image(cx, cy, image=tori, tag="hato")
    canv.pack()
    #時間計測開始
    time_start=time.time()

    key=""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()
