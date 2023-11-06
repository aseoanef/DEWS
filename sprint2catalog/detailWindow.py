import tkinter as tk

class detail_window():
    def __init__(self,path,title,description):
        #definiendo atributos
        root = tk.Toplevel()
        #self.root=root
        
        #centrar la ventana
        label1 = tk.Label(root ,image=path)
        label1.pack()
        label2 = tk.Label(root, text=title)
        label2.pack()
        label3 = tk.Label(root, text=description)
        label3.pack()
        #tamaño y localizacion de la ventana
        root.geometry("400x200")

        x=(root.winfo_screenwidth()/2-root.winfo_reqwidth())
        y=(root.winfo_screenheight()/2-root.winfo_reqheight())
        root.geometry(f"+{int(x)}+{int(y)}") 

        root.mainloop

        