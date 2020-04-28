from tkinter import *
from tkinter import ttk
from tkinter import font
class Gui:
    def __init__(self,master):
        self.master = master
        master.title("Stonks")
        #root.attributes("-fullscreen",True) # Fullscreen
        master.geometry(
        "{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        # Tech
        tech_label = Label(master, text="Technology")  # Header
        tech_cellular_label = Label(master, text="Cellular")
        tech_biomedical_label = Label(master, text="Biomedical")
        tech_ai_label = Label(master, text="AI")
        tech_computers_label = Label(master, text="Computers")
        # Cosmetics
        cosmetics_label = Label(master, text="Cosmetics") # Header
        cosmetics_essential_oils_label = Label(master, text="Essential Oils")
        cosmetics_synth_colors_label = Label(master, text="Synthetic Colors")
        cosmetics_makeup_label = Label(master, text="Makeup")
        # Metals
        metals_label = Label(master, text="Precious Metals") # Header
        metals_gold_label = Label(master, text="Gold")
        metals_silver_label = Label(master, text="Silver")
        metals_titanium_label = Label(master, text="Titanium")
        metals_platinum_label = Label(master, text="Platinum")
        metals_copper_label = Label(master, text="Copper")
        metals_bronze_label = Label(master, text="Bronze")
        # Transportation
        trans_label = Label(master, text="Transportation") # Header
        trans_auto_label = Label(master, text="Autombile")
        trans_aerospace_label = Label(master, text="Aerospace")
        trans_railroad_label = Label(master, text="Railroad")
        # Utilities
        utilities_label = Label(master, text="Utilities") # Header
        utilities_waste_recycling_label = Label(master, text="Waste and Recycling")
        utilities_solar_label = Label(master, text="Solar ")
        utilities_wind_label = Label(master, text="Wind ")
        utilities_coal_label = Label(master,text = "Coal")
        utilities_nuke_label = Label(master,text = "Nuclear")
        utilities_water_label = Label(master,text = "Water")
        #Real Estate
        estate_label = Label(master,text="Real Estate")
        estate_residential_label = Label(master,text="Residential")
        estate_commercial_label = Label(master,text="Commerical")
        #Bonds
        bonds_label = Label(master,text="Bonds")
        bonds_gov_label = Label(master,text = "Government")
        bonds_state_label = Label(master,text = "State")

        list_labels = [tech_label,tech_cellular_label,tech_biomedical_label,tech_computers_label,cosmetics_label,cosmetics_essential_oils_label,cosmetics_synth_colors_label,cosmetics_makeup_label,metals_label,metals_gold_label,metals_silver_label,metals_titanium_label,metals_platinum_label,metals_copper_label,metals_bronze_label,trans_label,trans_auto_label,trans_aerospace_label,trans_railroad_label,utilities_label,utilities_waste_recycling_label,utilities_solar_label,utilities_wind_label,utilities_coal_label,utilities_nuke_label,utilities_water_label,estate_label,estate_residential_label,estate_commercial_label,bonds_label,bonds_gov_label,bonds_state_label]
        for i in range(len(list_labels)):
            list_labels[i].grid(row=i,column=0)

root = Tk()
gui = Gui(root)
root.mainloop()