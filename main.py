import tkinter as tk
import gui
import price_update

root = tk.Tk()
my_gui = gui.Gui(root)
price_update.start(my_gui)
root.mainloop()
