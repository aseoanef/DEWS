from tkinter import Tk
from window import MainWindow
from LoadingWindow import  LoadingWindow
if __name__=="__main__":
    root=Tk()
    app=LoadingWindow(root)
    root.mainloop()
    root.destroy

