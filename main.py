import tkinter as tk
import gui
import price_init

root = tk.Tk()
my_gui = gui.Gui(root)
price_init.start(my_gui)
root.mainloop()
