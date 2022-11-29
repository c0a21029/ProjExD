import tkinter as tk
import tkinter.messagebox as tkm

root=tk.Tk()
root.geometry("300x500")

def Button_click(event):
    txt=event.widget["text"]
    if txt=="=":
        num=entry.get()
        res=eval(num)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    else:
        entry.insert(tk.END,txt)

#背景色を変更
def Change_cl(event):
    event.widget["bg"]="lightblue"

def Re_cl(event):
    event.widget["bg"]="white"

#練習ボタン
c=1;k=0
for i in range(8,-1,-1):
    button=tk.Button(root,text=3*(3-c)+k+1,width=4,height=2,font=("",30))
    button.bind("<1>",Button_click)
    button.bind("<Enter>",Change_cl)
    button.bind("<Leave>",Re_cl)
    button.grid(row=c,column=k)
    k+=1
    if k%3==0:
        c+=1
        k=0

button=tk.Button(root,text="a",width=4,height=2,font=("",30))
button.grid(row=1,column=4)
#記号
ope=["+",0,"="]
for i in ope:
        button=tk.Button(root,text=i,width=4,height=2,font=("",30))
        button.bind("<1>",Button_click)
        button.bind("<Enter>",Change_cl)
        button.bind("<Leave>",Re_cl)
        button.grid(row=c,column=k)
        k+=1

#練習入力欄
entry=tk.Entry(root,justify="right",width=10,font=("",40))
entry.grid(row=0,column=0,columnspan=3)

root.mainloop()