from tkinter import *
from tkinter import ttk


def TestLogic():
    global cont
    stgImg = PhotoImage(file="./storage/imagens/fim%d.png" % cont)
    label = ttk.Label(root, image=stgImg)
    label.image = stgImg
    cont += 1
    root.update_idletasks()
    return


root = Tk()

root.geometry('1010x740+200+200')
cont = 1
stgImg = PhotoImage(file="./storage/imagens/fim0.png")
label = ttk.Label(root, image=stgImg)
label.place(x=400, y=400)

testBtn = ttk.Button(root, text="TEST", command=TestLogic)
testBtn.place(x=400, y=200)
root.mainloop()