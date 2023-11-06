import tkinter as ttk
from cell import Cell
from PIL import Image,ImageTk
from detailWindow import detail_window
import requests
from io import BytesIO
from tkinter import messagebox

class MainWindow():


    def on_button_click(self, cell):
        #abrimos otra pestaña con los datos de cada cell
        zoom_image_window = detail_window(cell.image_tk, cell.title, cell.description)
        #zoom_image_window.mainloop()
   
   
    def load_image(self,image_url):
        response = requests.get(image_url)
        image_data = Image.open(BytesIO(response.content))
        image = ImageTk.PhotoImage(image_data)
        return image
    def about(self):
        messagebox.showinfo("Acerca del desarrollador","Programa desarrollado en Python 3.11.5 por Anxo Seoane")

     
    def __init__(self,root,json):
        self.root=root
        root.title("MainWindow")
        #tamaño de las columnas y filas
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        #crear barra de menus
        barra_menus= ttk.Menu()
        menu_ayuda = ttk.Menu(barra_menus, tearoff=False)
        menu_ayuda.add_command(
        label="Acerca de",
        command=self.about
        )
        barra_menus.add_cascade(menu=menu_ayuda, label="Ayuda")
        # Insertarla en la ventana principal.
        root.config(menu=barra_menus)
        #localizacion de la ventana
        x=(self.root.winfo_screenwidth()/2-self.root.winfo_reqwidth())
        y=(self.root.winfo_screenheight()/2-self.root.winfo_reqheight())
        self.root.geometry(f"+{int(x)}+{int(y)}")  
        
        canvas = ttk.Canvas(root)
        canvas.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        canvas.config(yscrollcommand=scrollbar.set)

        # Crear un marco para contener las celdas
        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.grid_rowconfigure(0, weight=1)
        canvas.grid_columnconfigure(0, weight=1)
        #lista de imagenes
        self.cells= []
        for i in range(len(json)):
            print(i)
            name=json[i].get("name")
            description=json[i].get("description")
            image_url=json[i].get("URL")
            image = self.load_image(image_url)
            self.cells.append(Cell(name,image,description))


        for i ,cell in enumerate(self.cells):
            #enseñar cada imagen
            label =ttk.Label(frame,image=cell.image_tk,text=cell.title,compound=ttk.BOTTOM)
            label.grid(row=i,column=0, sticky="w")
            #bindear el click
            label.bind("<Button-1>", lambda event, cell = cell: self.on_button_click(cell))
        #bindear el scroll al frame
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        frame.bind("<Configure>", on_configure)  

if __name__ == "__main__":
    root = ttk.Tk()
    app = MainWindow(root)
    
    root.mainloop()