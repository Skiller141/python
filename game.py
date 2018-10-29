import tkinter
from tkinter.messagebox import showerror

tk = tkinter.Tk()
tk.title('Canvas')
tk.iconbitmap('Graphicloads-100-Flat-New.ico')

class Game:
    def __init__(self, master=None):
        self.master = master
        self.x = 1
        self.y = -1
        self.start = False
        
        self.i = 0

        self.widgets_init()

    def start_game(self):
        self.i += 1
        if self.i % 2 == 0:
            self.start = False
            self.start_button['text'] = 'Start'
        else:
            self.start = True
            self.start_button['text'] = 'Pause'
            self.events_init()
            self.ball_move()

    def start_game_keypress(self, event):
        if event.keysym == 'Return' or event.keysym == 'space':
            self.start_game()

    def game_over(self):
        print('END')
        showerror('Game Over!', 'Game Over!')
        self.canvas.pack_forget()
        self.dashboard.pack_forget()
        self.widgets_init()
        self.start = False
        self.i = 0

    def widgets_init(self):
        self.canvas = tkinter.Canvas(self.master, width=500, height=500, bg='#333')
        self.canvas.pack(side='left')
        self.dashboard = tkinter.Frame(self.master, width=300, height=500, bg='#eee', padx=10, pady=10)
        self.dashboard.pack(side='right', fill='both')
        
        self.start_button = tkinter.Button(self.dashboard, width=20, text='Start', command=self.start_game)
        self.start_button.pack()

        self.rectangle = self.canvas.create_rectangle(200, 480, 300, 490, fill='#eee')
        self.ball = self.canvas.create_oval(240, 460, 260, 480, fill='red')

        self.ball_pos = self.canvas.coords(self.ball)
        self.dash_pos = self.canvas.coords(self.rectangle)

        x1 = 0
        y1 = 25
        x2 = 20
        y2 = 5
        for h in range(0, 100):
            if h == 25 or h == 50 or h == 75:
                y1 += 22
                y2 += 22
                x1 = 0
                x2 = 20
            self.canvas.create_rectangle(x1, y1, x2, y2, fill='#ccc')
            x1 += 20
            x2 += 20

    def key(self, event):
        print(event.keysym)

    def events_init(self):
        self.canvas.bind_all('<KeyPress-Left>', self.dash_move)
        self.canvas.bind_all('<KeyPress-Right>', self.dash_move)
        self.canvas.bind_all('<KeyPress-a>', self.dash_move)
        self.canvas.bind_all('<KeyPress-d>', self.dash_move)
        self.canvas.bind_all('<KeyPress-Return>', self.start_game_keypress)
        self.canvas.bind_all('<KeyPress-space>', self.start_game_keypress)
        self.canvas.bind_all('<KeyPress>', self.key)

    def dash_move(self, event):
        if self.start == True:
            self.dash_pos = self.canvas.coords(self.rectangle)
            if event.keysym == 'Left' or event.keysym == 'a':
                if self.dash_pos[0] <= 0:
                    self.canvas.move(self.rectangle, 0, 0)
                else:
                    self.canvas.move(self.rectangle, -5, 0)
            elif event.keysym == 'Right' or event.keysym == 'd':
                if self.dash_pos[2] >= int(self.canvas['width']):
                    self.canvas.move(self.rectangle, 0, 0)
                else:
                    self.canvas.move(self.rectangle, 5, 0)
    
    def ball_move(self):
        if self.start == True:
            self.ball_pos = self.canvas.coords(self.ball)
            if self.ball_pos[1] <= 0:
                self.y = 1
            if self.ball_pos[3] >= int(self.canvas['height']):
                self.game_over()
                return False
            if self.ball_pos[0] <= 0:
                self.x = 1
            if self.ball_pos[2] >= int(self.canvas['width']):
                self.x = -1

            if self.ball_pos[3] >= self.dash_pos[1] and self.ball_pos[0] <= self.dash_pos[2]:
                if self.ball_pos[2] >= self.dash_pos[0] and self.ball_pos[3] <= self.dash_pos[3]:
                    self.y = -1
            
            self.canvas.move(self.ball, self.x, self.y)
            self.canvas.after(10, self.ball_move)   
   
game = Game(master=tk)
# game.widgets_init()
# game.events_init()
# game.ball_move()

tk.mainloop()
