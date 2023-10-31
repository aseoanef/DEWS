from tkinter import Tk,Label
from PIL import Image,ImageTk
class Cell:
    def __init__(self,title,path,description):
        #definir los atributos de cada imagen
        self.title=title
        self.path=path
        self.description=description
        imageBefore=Image.open(self.path)
        #resize la imagen
        self.image_tk=ImageTk.PhotoImage(imageBefore.resize((100,100),Image.Resampling.LANCZOS))