from tkinter import Tk,Button
root=Tk()
root.title="ejemplo uso pack"
button1= Button(root, text="boton 1")
button2= Button(root, text="boton 2")
button3= Button(root, text="boton 3")
button1.pack(side="top",fill="both",expand=True,padx=16,pady=5,anchor="nw")
button2.pack(side="left",fill="x",expand=True)
button2.pack(side="rigth",fill="y")
root.mainloop()
