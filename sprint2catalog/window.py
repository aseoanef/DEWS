import tkinter as ttk
from cell import Cell
from PIL import Image,ImageTk
from detailWindow import detail_window
import requests
from io import BytesIO

class MainWindow():


    def on_button_click(self, cell):
        #abrimos otra pestaña con los datos de cada cell
        zoom_image_window = detail_window(cell.image_tk, cell.title, cell.description)
        zoom_image_window.mainloop()
   
   
    def load_image(self,image_url):
        response = requests.get(image_url)
        image_data = Image.open(BytesIO(response.content))
        image = ImageTk.PhotoImage(image_data)
        return image
        
        
    def __init__(self,root,json):
        self.root=root
        root.title("MainWindow")
        #lista de imagenes
        self.cells= []
        for i in range(len(json)):
            name=json[i].get("name")
            description=json[i].get("description")
            image_url=json[i].get("URL")
            image = self.load_image(image_url)
            self.cells.append(Cell(name,image,description))


        for i ,cell in enumerate(self.cells):
            #enseñar cada imagen
            label =ttk.Label(root,image=cell.image_tk,text=cell.title,compound=ttk.BOTTOM)
            label.grid(row=i,column=0)
            #bindear el click
            label.bind("<Button-1>", lambda event, cell = cell: self.on_button_click(cell))


if __name__ == "__main__":
    root = ttk.Tk()
    app = MainWindow(root)
    root.mainloop()