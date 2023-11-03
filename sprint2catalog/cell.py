from tkinter import Tk,Label
from PIL import Image,ImageTk
class Cell:
    def __init__(self,title,path,description):
        #definir los atributos de cada imagen
        self.title=title
        self.image_tk=path
        self.description=description
    