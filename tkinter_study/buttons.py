from tkinter import *

root = Tk()

def clicked():
    myLabel = Label(root, text="Clicou!").pack()

myButton = Button(root, text="Click Me!", command=clicked, fg="white", bg="blue").pack()

root.mainloop()