from tkinter import ttk
from tkinter import Tk
class no_window():
    def __init__(self,root):
        self.root=root
        root.title("NoWindow")
        self.root.frame=ttk.Frame(self.root)
        self.root.frame.pack()
        self.root.label=ttk.Label(self.root.frame,text="NO")
        self.root.label.pack()