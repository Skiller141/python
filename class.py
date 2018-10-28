import tkinter as tk
from tkinter.messagebox import showinfo

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #frame
        self.frame = tk.Frame(self)
        self.frame['width'] = 700
        self.frame['height'] = 500
        self.frame['bg'] = '#333'
        self.frame.pack_propagate(0)
        self.frame.pack(fill='both', expand=1)

        #image
        self.image = tk.PhotoImage(file='opengraph-icon-200x200.png')
        self.image = self.image.zoom(10)
        self.image = self.image.subsample(26)
        self.label = tk.Label(self.frame, image=self.image)
        self.label.pack(side='top')
        
        #btn click
        self.btn = tk.Button(self.frame)
        self.btn['text'] = 'Hello World\n(click me)'
        self.btn['command'] = self.alert
        self.btn.pack(side='right')

        #quit button
        self.quit = tk.Button(self.frame, text='QUIT', fg='red', command=root.destroy)
        self.quit.pack(side='bottom')

    #functions
    def alert(self):
        showinfo('Alert Title', 'Alert Text')

root = tk.Tk()
root.title("Simple Prog")
root.iconbitmap("Graphicloads-100-Flat-New.ico")
root.geometry("700x500")
root.resizable(0, 0)

app = Application(master=root)
app.mainloop()
