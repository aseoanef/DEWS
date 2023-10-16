from tkinter import ttk
from tkinter import Tk
class yes_window():
    def __init__(self,root):
        self.root=root
        root.title("YesWindow")
        self.root.frame=ttk.Frame(self.root)
        self.root.frame.pack()
        self.root.label=ttk.Label(self.root.frame,text="YES")
        self.root.label.pack()