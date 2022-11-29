import tkinter as tk
import tkinter.messagebox as tkm

root=tk.Tk()
root.geometry("380x500")

#クリック時の挙動
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
    if event.widget["text"]!="Wow":
        event.widget["bg"]="white"
    else:
        event.widget["bg"]="red"
   
#追加機能(Wowボタン)
def God_func(event):
    for i in range(100,-1,-1):
        if i >=1:
            tkm.showwarning("警告",f"ﾄﾞｩﾜァ…あと{i}回消してね")

#ボタン(数字)
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

#記号
ope=["/",0,"."]
ope2=["*","-","+","="]
for i in ope:
    button=tk.Button(root,text=i,width=4,height=2,font=("",30))
    button.bind("<1>",Button_click)
    button.bind("<Enter>",Change_cl)
    button.bind("<Leave>",Re_cl)
    button.grid(row=c,column=k)
    k+=1
c=1
for i in ope2:
    button=tk.Button(root,text=i,width=4,height=2,font=("",30))
    button.bind("<1>",Button_click)
    button.bind("<Enter>",Change_cl)
    button.bind("<Leave>",Re_cl)
    button.grid(row=c,column=4)
    c+=1

#追加機能(Wowボタン)
button=tk.Button(root,text="Wow",width=4,font=("",30),bg="red")
button.bind("<1>",God_func)
button.bind("<Enter>",Change_cl)
button.bind("<Leave>",Re_cl)
button.grid(row=0,column=4)

#入力欄
entry=tk.Entry(root,justify="right",width=10,font=("",40))
entry.grid(row=0,column=0,columnspan=4)

#いつもの
root.mainloop()