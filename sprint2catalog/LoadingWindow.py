import threading
from window import MainWindow
import tkinter as tk
import requests
class LoadingWindow:
    def __init__(self,root):
        #definicion de la ventana
        self.json_data=[]
        self.root=root
        self.root.title("Cargando...")
        self.root.geometry("200x200")
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
        self.thread=threading.Thread(target=self.fetch_json_data)
        self.thread.start()
    
    def draw_progress_circle(self,progress):#dibuja el circulo
        self.canvas.delete("progress")
        angle=int(360 *(progress / 100))
        self.canvas.create_arc(10,10,35,35,
                               start=0,extent=angle,tag="progress", outline="blue",width=4,style=tk.ARC)
    
    def update_progress_circle(self):#actualiza el progreso
        if self.progress < 50:
            self.progress +=5
        elif self.progress < 95:
            self.progress += 3
        elif self.progress < 99 :
            self.progress += 1
        else:
            self.progress = 0
        
        self.draw_progress_circle(self.progress)
        self.root.after(100,self.update_progress_circle)
    
    def fetch_json_data(self):
        response=requests.get("https://raw.githubusercontent.com/aseoanef/DEWS/main/recursos/catalog.json")
        if response.status_code==200:
            self.json_data=response.json()
            self.finished=True
    
    def launch_main_window(json_data):
        root=tk.Tk()
        app = MainWindow(root,json_data)
        root.mainloop()