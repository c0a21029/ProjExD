import tkinter as tk
import tkinter.messagebox as tkm

root=tk.Tk()
root.geometry("300x500")

def Button_click(event):
    txt=event.widget["text"]
    entry.insert(tk.END,txt)

#練習ボタン
c=1;k=0
for i in range(9,-1,-1):
    button=tk.Button(root,text=i,width=4,height=2,font=("",30))
    button.bind("<1>",Button_click)
    button.grid(row=c,column=k)
    k+=1
    if k%3==0:
        c+=1
        k=0
#記号
ope=["+","="]
for i in ope:
        button=tk.Button(root,text=i,width=4,height=2,font=("",30))
        button.grid(row=c,column=k)
        k+=1

#練習入力欄
entry=tk.Entry(root,justify="right",width=10,font=("",40))
entry.grid(row=0,column=0,columnspan=3)

root.mainloop()