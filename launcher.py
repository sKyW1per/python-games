import tkinter as tk
from tkinter import ttk  # for some buttons?


def center_screen(window, w_width, w_height):
    """center a tkinter-window"""
    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width / 2 - w_width / 2)
    center_y = int(screen_height / 2 - w_height / 2)

    # set the position of the window to the center of the screen
    window.geometry(f'{w_width}x{w_height}+{center_x}+{center_y}')


class Launcher:
    def __init__(self):
        self.width = 500  # width and height of the window
        self.height = 400
        self.window = tk.Tk()  # setting up the window
        self.window.title("game launcher")  # new title
        self.window.resizable(False, False)  # make sure that the window isn't resizable
        center_screen(self.window, self.width, self.height)

    def start(self):
        self.window.mainloop()  # start the window

    def stop(self):
        self.window.quit()  # doesn't work: https://stackoverflow.com/questions/35792365/how-to-destroy-this-tkinter-window?adlt=strict&toWww=1&redig=D4EDD692FE0749C5BCB2029985553E02


#test script
if __name__ == "__main__":
    lc = Launcher()
    lc.start()
    lc.stop()
