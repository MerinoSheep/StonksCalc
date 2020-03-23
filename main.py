from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Stonks")
#window.attributes('-zoomed', True) 
#window.attributes("-fullscreen",True)
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))


tech_label = Label(window,text = "Technology")
cosmetics_label = Label(window,text = "Cosmetics")
metals_label = Label(window,text = "Precious Metals")
trans_label = Label(window,text = "Transportation")
utilities_label = Label(window,text = "Utilities")
estate_label = Label(window,text = "Real Estate")
bonds_label = Label(window,text = "Bonds")

tech_label.grid(row = 0,column = 0)
cosmetics_label.grid(row = 1,column = 0)
metals_label.grid(row = 2,column = 0)
trans_label.grid(row = 3,column = 0)
utilities_label.grid(row = 4,column = 0)
estate_label.grid(row = 5,column = 0)
bonds_label.grid(row = 6,column = 0)

window.mainloop()