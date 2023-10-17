from tkinter import Tk,ttk
import tkinter as Tk
from cell import Cell

class MainWindow():
    def __init__(self,root):
        self.root=root
        root.title("MainWindow")
        self.cells= [
            Cell("image1",'C:\\msys64\\home\\Alumno\\DEWS\\sprint1Tkinter\\catalog\\data\\edited\\artic.jpg'),
            Cell("image2",'C:\\msys64\\home\\Alumno\\DEWS\\sprint1Tkinter\\catalog\\data\\edited\\fennec.jpg'),
            Cell("image3",'C:\\msys64\\home\\Alumno\\DEWS\\sprint1Tkinter\\catalog\\data\\edited\\marble.jpg'),
            Cell("image4",'C:\\msys64\\home\\Alumno\\DEWS\\sprint1Tkinter\\catalog\\data\\edited\\red.jpg'),
            Cell("image5",'C:\\msys64\\home\\Alumno\\DEWS\\sprint1Tkinter\\catalog\\data\\edited\\grey.jpg')
        ]
        for i ,cell in enumerate(self.cells):
            label =ttk.Label(root,image=cell.image_tk,text=cell.title,compound=Tk.BOTTOM)
            label.grid(row=i,column=0)
        