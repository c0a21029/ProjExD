import tkinter as tk
import tkinter.messagebox as tkm
root=tk.Tk()
root.title ("おためしか")
root.geometry("500x200")

def button_click():
    tkm.showwarning("警告","aaa")

label=tk.Label(root,
                text="ラベルラベルラベル",
                font=("",20))
label.pack()

button=tk.Button(root,text="お砂",command=button_click)
button.pack()

entry=tk.Entry(width=30)
entry.insert(tk.END,"fugyapiyo")
entry.pack()

root.mainloop()