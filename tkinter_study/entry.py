from tkinter import *

root = Tk()


e = Entry(root)
e.pack()
e.insert(0, "Digite seu nome")

def clicked():
    texto = f'Olá, {e.get()}'
    myLabel = Label(root, text=texto).pack()

myButton = Button(root, text="Click Me!", command=clicked, fg="white", bg="blue").pack()

root.mainloop()