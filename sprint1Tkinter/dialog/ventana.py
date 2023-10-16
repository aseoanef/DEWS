from tkinter import Tk,ttk,messagebox
from yes_window import yes_window
from no_window import no_window

class MainWindow():  
    def openYesWindow():
        root=Tk()
        app=yes_window(root)
    def openNoWindow():
        root=Tk()
        app=no_window(root)
    def __init__(self,root):
        self.root=root
        root.title("MainWindow")
        self.frame=ttk.Frame(self.root)
        self.frame.pack()
        self.label=ttk.Label(self.frame,text="blablablabla")
        self.label.pack()
        button1= ttk.Button(root,text="sí",command=MainWindow.openYesWindow)#,command=yes_window()
        button2=ttk.Button(root,text="no",command=MainWindow.openNoWindow)
        button1.pack(side="left",fill="x",expand=True)
        button2.pack(side="right",fill="x",expand=True)
        label=ttk.Label(root)
    
        #label.bind("button1",lambda event,celda=cell: self.on_button_clicked(celda))
        
        


# from tkinter import Tk,ttk,messagebox
# import tkinter as Tk
# from cell import Cell
# class MainWindow():
#     def on_button_clicked(self,cell):
#         message="has hecho click en la celda"+ cell.title
#         messagebox.showinfo("Información " + message )
#     def __init__(self,root):
#         #self.root=root
#         root.title("MainWindow")
#         self.cells= [
#             Cell("imagen1",'C:\\Users\\Alumno\\Downloads\\wallpaperflare.com_wallpaper(2).jpg'),
#             Cell("image2",'C:\\Users\\Alumno\\Downloads\\wallpaperflare.com_wallpaper(1).jpg'),
#             Cell("imagen3",'C:\\Users\\Alumno\\Downloads\\wallpaperflare.com_wallpaper.jpg')
#         ]
#         for i ,cell in enumerate(self.cells):
#             label =ttk.Label(root,image=cell.image_tk,text=cell.title,compound=Tk.BOTTOM)
#             label.grid(row=i,column=0)
#             label.bind("<Button-1>",lambda event, cell=cell:self.on_button_clicked)
#         #self.frame=ttk.Frame(self.root)
#         #self.frame.pack()
#         #self.label=ttk.Label(self.frame,text="mensaje etc")
#         #self.label.pack()
#         #self.button=ttk.Button(self.frame,text="otro mensaje")
#         #self.button.pack()
