import threading
from window import MainWindow
import tkinter as tk
import requests
class LoadingWindow:
    def __init__(self,root):
        self.finished=False
        self.json=[]
        #definicion de la ventana
        self.root=root
        #centrar la ventana
        self.root.geometry("200x200")
        x=(self.root.winfo_screenwidth()/2-self.root.winfo_reqwidth()/2)
        y=(self.root.winfo_screenheight()/2-self.root.winfo_reqheight()/2)
        self.root.geometry(f"+{int(x)}+{int(y)}") 
        self.root.title("Cargando...")
        self.root.resizable(False,False)
        #añadir una label
        self.label =tk.Label(self.root, text="Cargando datos...",font=("Arial",14))
        self.label.pack(side=tk.TOP,pady=10)

        label_bg_color=self.label.cget("bg")
        #añadir un cuadro para dibjar
        self.canvas=tk.Canvas(self.root,width=60,height=60,bg=label_bg_color)
        self.canvas.pack()
        
        self.progress=0
        self.draw_progress_circle(self.progress)
        self.update_progress_circle()
        
        #empezar el thread
        self.thread=threading.Thread(target=self.get_json)
        self.thread.start()
        self.thread_progress()
    
    def draw_progress_circle(self,progress):#dibuja el circulo
        self.canvas.delete("progress")
        angle=int(360 *(progress / 100))#calcular lo que equivale del progreso a circulo
        self.canvas.create_arc(10,10,35,35,
                               start=0,extent=angle,tag="progress", outline="blue",width=4,style=tk.ARC)
    
    def update_progress_circle(self):#actualiza el progreso
        if self.progress < 100:
            self.progress +=3
        else:
            self.progress = 0
        
        self.draw_progress_circle(self.progress)
        self.root.after(5,self.update_progress_circle)
    
    def get_json(self):#conseguir los datos del JSON de github
        response=requests.get("https://raw.githubusercontent.com/aseoanef/DEWS/main/recursos/catalog.json")
        if response.status_code==200:
            self.json=response.json()
            self.finished=True
    
    def launch_main_window(json):
        root=tk.Tk()
        app = MainWindow(root,json)
        root.mainloop()

    def thread_progress(self):
        if(self.finished): 
            self.root.destroy()
            self.initialize_mainwindow(self.json)
           
        else :
            self.root.after(100,self.thread_progress)

    def initialize_mainwindow(self,json):
        root=tk.Tk()
        app = MainWindow(root,self.json)
        root.mainloop()