import tkinter as tk
import pygame
from tkinter import *


class Morpion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        size = 550
        self.Canevas = tk.Canvas(self, width=size, height=size, bg='lightgray')
        self.Canevas.pack(padx=10, pady=10)
        self.deleteButton = None
        self.clearButton = None
        self.flag = 1  # The flag is used to determine which player is actually playing. 0 / 1
        self.moves = []
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
            self.moves.clear()
            self.grille()

        self.deleteButton = tk.Button(self, text='Quit', width=6, command=self.destroy)
        self.deleteButton.pack(side=LEFT, pady=2, padx=2)

        self.clearButton = tk.Button(self, text='Clear', width=6, command=erase)
        self.clearButton.pack(side=LEFT, pady=2, padx=2)

    def move(self, px, py):  # Depending on the player, draw cross or circle
        if (px, py) not in self.moves:
            if self.flag:
                self.Canevas.create_line(px, py, px + 120, py + 120)
                self.Canevas.create_line(px + 120, py, px, py + 120)
                self.flag = 0

                pygame.mixer.init()
                pygame.mixer.music.load("son_1.mp3")
                pygame.mixer.music.play(loops=0)
            else:
                self.Canevas.create_oval(px, py, px + 120, py + 120)
                self.flag = 1
                pygame.mixer.music.load("son_2.mp3")
                pygame.mixer.music.play(loops=0)
        else:
            print("Are you an idiot ? You can't play here my friend")

    def events(self):  # events clic, uses function to record the position of the moves and the function to draw

        def clic(event):
            pos_x = event.x
            pos_y = event.y
            valid = 0
            if pos_x < 50:
                print("Incorrect position. Try again.")
            elif pos_x < 200:
                pos_x = 65
            elif pos_x < 350:
                pos_x = 215
            elif pos_x < 500:
                pos_x = 365

            if pos_y < 200:
                pos_y = 65
            elif pos_y < 350:
                pos_y = 215
            elif pos_y < 500:
                pos_y = 365

            self.move(pos_x, pos_y)
            self.moves.append((pos_x, pos_y))

        self.Canevas.bind('<Button-1>', clic)

    def vue_loop(self):
        self.mainloop()


if __name__ == '__main__':
    pygame.mixer.init()
    f1 = Morpion()
