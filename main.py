from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Stonks")
#window.attributes('-zoomed', True) 
window.attributes("-fullscreen",True)
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.mainloop()