import tkinter as tk
from tkinter import ttk  # for some buttons
# from PIL import Image, ImageTk


class Launcher(tk.Tk):
    def __init__(self):
        super().__init__()

    def start(self):
        self.app()

    def stop(self):
        self.App.quit()  # close application

    def app(self):  # init tk.Tk
        self.width = 500  # width and height of the window
        self.height = 394

        self.title("game launcher")  # new title
        self.resizable(False, False)  # make sure that the window isn't resizable
        self.geometry(f"{self.width}x{self.height}")  # set width and height of the window

        self.columnconfigure(0, weight=1)  # configure the columns
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.makeButtons()

        self.mainloop()  # start the application

    def onclick(self, button):
        print(button)

    def makeButtons(self):
        for i in range(9):
            games = ["snake", "pong", "3", "4", "5", "6", "7", "8", "9"]  # names of the games
            button = f'button{i} = ttk.Button(self, text="{games[i]}") \nbutton{i}.grid(column={i % 3}, row={int(i / 3)}, sticky=tk.EW, ipady=53)'  # make every loop a string. if you don't want to type each button by yourself...
            exec(button)  # execute the stings


