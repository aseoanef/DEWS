import tkinter as tk

class detail_window():
    def __init__(self,path,title,description):
        #definiendo atributos
        root = tk.Toplevel()
        label1 = tk.Label(root ,image=path)
        label1.pack()
        label2 = tk.Label(root, text=title)
        label2.pack()
        label3 = tk.Label(root, text=description)
        label3.pack()

        root.mainloop()

        