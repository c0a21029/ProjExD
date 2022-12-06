import tkinter as tk


if __name__=="__main__":
    #ウィンドウ生成
    root=tk.Tk()
    root.title("迷えるこうかとん")
    canv=tk.Canvas(root,width=1500,height=900,bg="black")
    #画像読み込み～表示
    tori=tk.PhotoImage(file="fig/8.png")
    cx,cy=300,400
    canv.create_image(cx,cy,image=tori,tag="hato")
    canv.pack()

    key=""
    root.mainloop()
