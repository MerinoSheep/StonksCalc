from random import randint
def start(gui): #Sets initial price of all stocks
	#metals
	gui.metals_gold_label_price['text']=rand99()
	gui.metals_bronze_label_price['text'] = rand20()
	gui.metals_platinum_label_price['text']=rand80()
	gui.metals_copper_label_price['text'] = rand40()
	gui.metals_titanium_label_price['text']= rand60()
	gui.metals_silver_label_price['text']= rand60()
	#Cosmetics
	gui.cosmetics_essential_oils_label_price['text'] = rand40()
	gui.cosmetics_makeup_label_price['text'] = rand40()
	gui.cosmetics_synth_colors_label_price['text']= rand60()
	#Transportation
	gui.trans_aerospace_label_price['text']=rand80()
	gui.trans_railroad_label_price['text']= rand60()
	gui.trans_auto_label_price['text']=rand99()
	#Real Estate 
	gui.estate_commercial_label_price['text']=rand80()
	gui.estate_residential_label_price['text']= rand60()
	#Tech
	gui.tech_biomedical_label_price['text']= rand60()
	gui.tech_cellular_label_price['text']=rand99()
	gui.tech_computers_label_price['text']=rand99()
	gui.tech_ai_label_price['text'] = rand40()
	#Bonds
	gui.bonds_gov_label_price['text'] = rand20()
	gui.bonds_state_label_price['text'] = rand20()
	#Utilities
	gui.utilities_waste_recycling_label_price['text'] = rand20()
	gui.utilities_solar_label_price['text'] = rand20()
	gui.utilities_wind_label_price['text'] = rand20()
	gui.utilities_coal_label_price['text']= rand60()
	gui.utilities_nuke_label_price['text'] = rand40()

def rand20():#random for 1-20
	return str(randint(1,20))
def rand40():#random 20-40
	return str(randint(20,40))
def rand60():#random 40-60
	return str(randint(40,60))
def rand80():#random 60-80
	return str(randint(60,80))
def rand99():#random99
	return str(randint(80,99))
