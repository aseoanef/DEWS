from tkinter import Tk,Label
from PIL import Image,ImageTk
class Cell:
    def __init__(self,title,path):
        self.title=title
        self.path=path
        imageBefore=Image.open(self.path)
        self.image_tk=ImageTk.PhotoImage(imageBefore.resize((100,100),Image.Resampling.LANCZOS))
        
        # self.image_tk= ImageTk.PhotoImage(file=self.path)



# root=Tk()
# root.title("Ejemplo de imagen")
# imagen = ImageTk.PhotoImage(file="C:\\Users\\Alumno\\Downloads\\wallpaperflare.com_wallpaper(3).jpg")
# label=Label(root,image=imagen)
# label.pack()
# root.mainloop()