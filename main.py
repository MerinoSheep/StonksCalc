from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Stonks")
#window.attributes('-zoomed', True) 
#window.attributes("-fullscreen",True)
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))


tech_Label = Label(window,text = "Technology")

 
cosmetics_Label = Label(window,text = "Cosmetics")
metals_Label = Label(window,text = "Precious Metals")
trans_Label = Label(window,text = "Transportation")
utilities_Label = Label(window,text = "Utilities")
estate_Label = Label(window,text = "Real Estate")
bonds_Label = Label(window,text = "Bonds")

tech_Label.grid(row = 0,column = 0)
cosmetics_Label.grid(row = 1,column = 0)
metals_Label.grid(row = 2,column = 0)
trans_Label.grid(row = 3,column = 0)
utilities_Label.grid(row = 4,column = 0)
estate_Label.grid(row = 5,column = 0)
bonds_Label.grid(row = 6,column = 0)

window.mainloop()