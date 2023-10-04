from tkinter import Tk,Label
from PIL import Image,ImageTk

root=Tk()
root.title("Ejemplo de imagen")
imagen = ImageTk.PhotoImage(file="C:\\Users\\Alumno\\Downloads\\wallpaperflare.com_wallpaper(3).jpg")
label=Label(root,image=imagen)
label.pack()
root.mainloop()