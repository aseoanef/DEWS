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
        

