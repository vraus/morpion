import tkinter as tk
from tkinter import *
import time


class Morpion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        size = 550
        self.Canevas = tk.Canvas(self, width=size, height=size, bg='lightgray')
        self.Canevas.pack(padx=10, pady=10)
        self.deleteButton = None
        self.clearButton = None
        self.grilleButton = None
        self.flag = 1  # The flag is used to determine which player is actually playing. 0 / 1
        self.mooves = []  # An array of tuple, (absolute_pos, player_number). Used to check if someone won
        self.buttons()
        self.grille()
        self.events()
        self.vue_loop()

    def grille(self):  # Draw the board
        for i in range(4):
            self.Canevas.create_line(50 + i * 150, 50, 50 + i * 150, 500)
        for i in range(4):
            self.Canevas.create_line(50, 50 + i * 150, 500, 50 + i * 150)

    def buttons(self):  # Simple buttons at the bottom of the board
        def erase():
            self.Canevas.delete(ALL)

        self.deleteButton = tk.Button(self, text='Quit', width=6, command=self.destroy)
        self.deleteButton.pack(side=LEFT, pady=2, padx=2)

        self.clearButton = tk.Button(self, text='Clear', width=6, command=erase)
        self.clearButton.pack(side=LEFT, pady=2, padx=2)

        self.grilleButton = tk.Button(self, text='Grille', width=6, command=self.grille)
        self.grilleButton.pack(side=LEFT, pady=2, padx=2)

    def record_moove(self, pX, pY):  # To put the absolute position of the mooves
        pass

    def is_won(self):  # Function to check after each moove if there is a winner or not
        print(self.mooves)

    def moove(self, pX, pY):  # Depending on the player, draw cross or circle
        if self.flag:
            self.Canevas.create_line(pX, pY, pX + 120, pY + 120)
            self.Canevas.create_line(pX + 120, pY, pX, pY + 120)
            self.is_won()
            self.flag = 0
        else:
            self.Canevas.create_oval(pX, pY, pX + 120, pY + 120)
            self.is_won()
            self.flag = 1

    def events(self):  # events clic, uses function to record the position of the mooves and the function to draw

        def clic(event):
            posX = event.x
            posY = event.y
            if posX < 200:
                posX = 65
            elif posX < 350:
                posX = 215
            elif posX < 500:
                posX = 365

            if posY < 200:
                posY = 65
            elif posY < 350:
                posY = 215
            elif posY < 500:
                posY = 365
            self.moove(posX, posY)
            self.record_moove(posX, posY)

        self.Canevas.bind('<Button-1>', clic)

    def vue_loop(self):
        self.mainloop()


if __name__ == '__main__':
    f1 = Morpion()
