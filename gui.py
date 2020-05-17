from tkinter import *
import tkinter.ttk
from tkinter import font
import card
import shutdown

class Gui:
	
	def __init__(self, master):
		self.power_button = PhotoImage(file ="img/power_button.png").subsample(6,6)

		self.master = master

		master.title("Stonks")
		#master.attributes("-fullscreen",True) # Fullscreen
		master.geometry(
			"{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))


		# Tech
		self.tech_label = Label(master, text="Technology")  # Header
		self.tech_cellular_label = Label(master, text="Cellular")
		self.tech_biomedical_label = Label(master, text="Biomedical")
		self.tech_ai_label = Label(master, text="AI")
		self.tech_computers_label = Label(master, text="Computers")
		# Cosmetics
		self.cosmetics_label = Label(master, text="Cosmetics")  # Header
		self.cosmetics_essential_oils_label = Label(master, text="Essential Oils")
		self.cosmetics_synth_colors_label = Label(master, text="Synthetic Colors")
		self.cosmetics_makeup_label = Label(master, text="Makeup")
		# Metals
		self.metals_label = Label(master, text="Precious Metals")  # Header
		self.metals_gold_label = Label(master, text="Gold")
		self.metals_silver_label = Label(master, text="Silver")
		self.metals_titanium_label = Label(master, text="Titanium")
		self.metals_platinum_label = Label(master, text="Platinum")
		self.metals_copper_label = Label(master, text="Copper")
		self.metals_bronze_label = Label(master, text="Bronze")
		# Transportation
		self.trans_label = Label(master, text="Transportation")  # Header
		self.trans_auto_label = Label(master, text="Autombile")
		self.trans_aerospace_label = Label(master, text="Aerospace")
		self.trans_railroad_label = Label(master, text="Railroad")
		# Utilities and Energy
		self.utilities_label = Label(master, text="Utilities")  # Header
		self.utilities_waste_recycling_label = Label(
			master, text="Waste and Recycling")
		self.utilities_solar_label = Label(master, text="Solar ")
		self.utilities_wind_label = Label(master, text="Wind")
		self.utilities_coal_label = Label(master, text="Coal")
		self.utilities_nuke_label = Label(master, text="Nuclear")

		# Real Estate
		self.estate_label = Label(master, text="Real Estate")
		self.estate_residential_label = Label(master, text="Residential")
		self.estate_commercial_label = Label(master, text="Commerical")
		# Bonds
		self.bonds_label = Label(master, text="Bonds")
		self.bonds_gov_label = Label(master, text="Government")
		self.bonds_state_label = Label(master, text="State")

		

		
		#!PRICE LABELS
		self.tech_label_price = Label(master, text="—")  # Header These are placeholders and will not ever change
		self.tech_cellular_label_price = Label(master)
		self.tech_biomedical_label_price = Label(master )
		self.tech_ai_label_price = Label(master)
		self.tech_computers_label_price = Label(master)
		# Cosmetics
		self.cosmetics_label_price = Label(master, text="—")  # Header
		self.cosmetics_essential_oils_label_price = Label(master)
		self.cosmetics_synth_colors_label_price = Label(master)
		self.cosmetics_makeup_label_price = Label(master)
		# Metals
		self.metals_label_price = Label(master, text="—")  # Header
		self.metals_gold_label_price = Label(master)
		self.metals_silver_label_price = Label(master )
		self.metals_titanium_label_price = Label(master)
		self.metals_platinum_label_price = Label(master)
		self.metals_copper_label_price = Label(master)
		self.metals_bronze_label_price = Label(master)
		# Transportation
		self.trans_label_price = Label(master, text="—")  # Header
		self.trans_auto_label_price = Label(master)
		self.trans_aerospace_label_price = Label(master)
		self.trans_railroad_label_price = Label(master)
		# Utilities
		self.utilities_label_price = Label(master, text="—")  # Header
		self.utilities_waste_recycling_label_price = Label(
			master)
		self.utilities_solar_label_price = Label(master)
		self.utilities_wind_label_price = Label(master)
		self.utilities_coal_label_price = Label(master)
		self.utilities_nuke_label_price = Label(master)

		# Real Estate
		self.estate_label_price = Label(master,text ='—') # Header
		self.estate_residential_label_price = Label(
			master)
		self.estate_commercial_label_price = Label(
			master)
		# Bonds
		self.bonds_label_price = Label(master, text="—") # Header
		self.bonds_gov_label_price = Label(master)
		self.bonds_state_label_price = Label(master)
		#gridding

		self.list_labels = [self.tech_label, self.tech_cellular_label, self.tech_biomedical_label,self.tech_ai_label, self.tech_computers_label, self.cosmetics_label, self.cosmetics_essential_oils_label, self.cosmetics_synth_colors_label, self.cosmetics_makeup_label, self.metals_label, self.metals_gold_label, self.metals_silver_label, self.metals_titanium_label, self.metals_platinum_label, self.metals_copper_label, self.metals_bronze_label,
					   self.trans_label, self.trans_auto_label, self.trans_aerospace_label, self.trans_railroad_label]
			
		for i in range(len(self.list_labels)):
			self.list_labels[i].grid(row=i, column=0)

		self.list_label_prices1 = [self.tech_label_price, self.tech_cellular_label_price, self.tech_biomedical_label_price,self.tech_ai_label_price ,self.tech_computers_label_price, self.cosmetics_label_price, self.cosmetics_essential_oils_label_price, self.cosmetics_synth_colors_label_price, self.cosmetics_makeup_label_price, self.metals_label_price, self.metals_gold_label_price, self.metals_silver_label_price, self.metals_titanium_label_price, self.metals_platinum_label_price, self.metals_copper_label_price, self.metals_bronze_label_price,
							 self.trans_label_price, self.trans_auto_label_price, self.trans_aerospace_label_price, self.trans_railroad_label_price]
		for i in range(len(self.list_label_prices1)):
			self.list_label_prices1[i].grid(row=i, column=1)
		## Seperator ##
		self.sep = tkinter.ttk.Separator(master,orient=VERTICAL)
		self.sep.grid(column=2,row =0,rowspan=20,sticky='ns',padx=100)
		## --------- ##

		self.list_labels2 = [self.utilities_label, self.utilities_waste_recycling_label, self.utilities_solar_label, self.utilities_wind_label, self.utilities_coal_label, self.utilities_nuke_label, self.estate_label, self.estate_residential_label, self.estate_commercial_label, self.bonds_label, self.bonds_gov_label, self.bonds_state_label]
		for i in range(len(self.list_labels2)):
			self.list_labels2[i].grid(row=i, column=3)	

		self.list_label_prices2 = [self.utilities_label_price, self.utilities_waste_recycling_label_price, self.utilities_solar_label_price, self.utilities_wind_label_price, self.utilities_coal_label_price, self.utilities_nuke_label_price, self.estate_label_price, self.estate_residential_label_price, self.estate_commercial_label_price, self.bonds_label_price, self.bonds_gov_label_price, self.bonds_state_label_price]
		for i in range(len(self.list_label_prices2)):
			self.list_label_prices2[i].grid(row=i, column=4)
		#Entry 
		def entry_click():
			card.num(self.card_entry.get(),self)
			self.card_entry.delete(0,'end')

		self.shutdown_button = Button(master,image=self.power_button,command=shutdown.main) 
		self.shutdown_button.grid(row=0,column=999)

		self.card_entry = Entry(master)
		self.card_entry.grid(row=999,column=998)
		self.next_turn_button = Button(master,text="Next Turn",command=entry_click)
		self.next_turn_button.grid(row=999,column=999)


		
