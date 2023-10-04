from tkinter import Tk,ttk,messagebox
import tkinter as Tk
from cell import Cell
class MainWindow():
    def on_button_clicked(self,cell):
        message="has hecho click en la celda"+ cell.title
        messagebox.showinfo("Información " + message )
    def __init__(self,root):
        #self.root=root
        root.title("MainWindow")
        self.cells= [
            Cell("imagen1",'C:\\Users\\Alumno\\Downloads\\wallpaperflare.com_wallpaper(2).jpg'),
            Cell("image2",'C:\\Users\\Alumno\\Downloads\\wallpaperflare.com_wallpaper(1).jpg'),
            Cell("imagen3",'C:\\Users\\Alumno\\Downloads\\wallpaperflare.com_wallpaper.jpg')
        ]
        for i ,cell in enumerate(self.cells):
            label =ttk.Label(root,image=cell.image_tk,text=cell.title,compound=Tk.BOTTOM)
            label.grid(row=i,column=0)
            label.bind("<Button-1>",lambda event, cell=cell:self.on_button_clicked)
        #self.frame=ttk.Frame(self.root)
        #self.frame.pack()
        #self.label=ttk.Label(self.frame,text="mensaje etc")
        #self.label.pack()
        #self.button=ttk.Button(self.frame,text="otro mensaje")
        #self.button.pack()
