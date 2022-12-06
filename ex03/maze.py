import tkinter as tk
import maze_maker as mm
#キー押下アクション
def key_down(event):
    global key
    key=event.keysym
#キーリリースアクション
def key_up(event):
    global key
    key=""

def main_proc():
    global cx,cy,mx,my
    if key == "Up":my-=1
    if key == "Down":my+=1
    if key == "Right":mx+=1
    if key == "Left":mx-=1
    if maze_lst[mx][my]==1: #壁判定
        if key == "Up":my+=1
        if key == "Down":my-=1
        if key == "Right":mx-=1
        if key == "Left":mx+=1

    cx,cy=mx*100+50,my*100+50
    canv.coords("hato",cx,cy)
    root.after(100,main_proc)

if __name__=="__main__":
    #ウィンドウ生成
    root=tk.Tk()
    root.title("迷えるこうかとん")
    canv=tk.Canvas(root,width=1500,height=900,bg="black")
    #迷路生成
    maze_lst=mm.make_maze(15,9)
    mm.show_maze(canv,maze_lst)
    #画像読み込み～表示
    tori=tk.PhotoImage(file="fig/8.png")
    mx,my=1,1
    cx,cy=mx*100+50,my*100+50
    canv.create_image(cx,cy,image=tori,tag="hato")
    canv.pack()

    key=""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()
