from PIL import ImageTk
import tkinter as tk

class Cell:
    def __init__(self, title , path ):
        self.title=title
        self.path=path 
        self.image_tk = ImageTk.PhotoImage(file=self.path)