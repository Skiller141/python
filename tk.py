from tkinter import *
from tkinter.messagebox import showinfo
import tkinter.font as fonts

root = Tk()
root.title("Simple Prog")
root.geometry("500x500")
root.resizable(0, 0)

fontButton = fonts.Font(family='Helvetica', weight='bold')
fontLabel = fonts.Font(weight='bold')

frame = Frame(master=root, background="#333")
frame.pack_propagate(0)
frame.pack(fill=BOTH, expand=1)

def showAlert():
    showinfo('Title', 'My Text')

l = Label(frame, text="Hello World!", background="#333", fg="#eee")
l.pack()

b = Button(frame, text='Show Alert', command=showAlert, font=fontButton)
b.pack()

root.mainloop()
