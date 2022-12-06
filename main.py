from src.gui import Gui
import tkinter as tk 


if __name__ == "__main__":
   root = tk.Tk()
   app = Gui(root)
   app.pack()
   root.title('L/r 7')
   root.geometry('1000x600')
   root.mainloop()
