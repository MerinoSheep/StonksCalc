# Reference google doc for documentation
from math import ceil
from random import randint
complex_dict={}
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

def num(num, gui):
	global complex_dict
	all_metal = [gui.metals_gold_label_price, gui.metals_bronze_label_price, gui.metals_platinum_label_price,
	gui.metals_copper_label_price, gui.metals_titanium_label_price, gui.metals_silver_label_price]
	def mult_label(label, num):
		for i in label:
			i['text'] = ceil(int(i['text'])*num)
	did_input= True
	try:
		num = int(num)
		
	except ValueError:
		print("No number or no input")
		did_input = False
	 # KEY: list and value amount of turns put 9999 if infinite 
	if(did_input):
		if num == 0:
			complex_dict[tuple(all_metal)]=[9999,.92]
		elif num == 2: mult_label(all_metal, 1.1)
		elif num == 3:  mult_label([gui.trans_aerospace_label_price], .8)
		elif num ==4: 
			mult_label([gui.utilities_nuke_label_price], .85)
			mult_label([gui.utilities_solar_label_price, gui.utilities_wind_label_price, gui.utilities_coal_label_price], 1.1)
		elif num ==6:  mult_label([gui.bonds_gov_label_price],1.1)
		elif num ==7:  
			mult_label([gui.metals_gold_label_price, gui.metals_bronze_label_price, gui.metals_platinum_label_price,
		gui.metals_copper_label_price, gui.metals_titanium_label_price, gui.metals_silver_label_price,gui.trans_aerospace_label_price,gui.trans_auto_label_price,
		gui.bonds_gov_label_price,gui.bonds_state_label_price,gui.trans_railroad_label_price],1.1)#TODOASK
			mult_label([gui.estate_commercial_label_price],.92)
			mult_label([gui.estate_residential_label_price],.92)
		elif num == 11: mult_label([gui.tech_ai_label_price,gui.metals_gold_label_price, gui.metals_bronze_label_price, gui.metals_platinum_label_price,
		gui.metals_copper_label_price, gui.metals_titanium_label_price, gui.metals_silver_label_price],*.88)
		elif num == 13: 
			complex_dict[tuple([gui.utilities_coal_label_price,gui.utilities_solar_label_price,gui.utilities_wind_label_price])]=[2,1.1]
			complex_dict[tuple([gui.utilities_nuke_label_price])] = [2,1.05]
		elif num == 15: mult_label([gui.bonds_gov_label_price,gui.bonds_state_label_price],1.05)
		elif num == 16: 
			gui.metals_gold_label_price['text']=rand99()
			gui.metals_bronze_label_price['text'] = rand20()
			gui.metals_platinum_label_price['text']=rand80()
			gui.metals_copper_label_price['text'] = rand40()
			gui.metals_titanium_label_price['text']= rand60()
			gui.metals_silver_label_price['text']= rand60()
			gui.trans_aerospace_label_price['text']=rand80()
			gui.trans_railroad_label_price['text']= rand60()
			gui.trans_auto_label_price['text']=rand99()
			gui.bonds_gov_label_price['text'] = rand20()
			gui.bonds_state_label_price['text'] = rand20()
		elif num == 18: complex_dict[tuple([gui.tech_ai_label_price])]=[4,1.1]
		elif num == 19: mult_label([gui.cosmetics_makeup_label_price],.8)
		elif num == 20: mult_label([gui.metals_titanium_label_price],.8)
		elif num == 21: mult_label([gui.trans_auto_label_price],1.12)
		elif num == 23:
			mult_label([gui.estate_commercial_label_price],1.15)
			mult_label([gui.estate_residential_label_price],1.1)
		elif num == 24:  mult_label([gui.bonds_gov_label_price,gui.bonds_state_label_price],.9)
		elif num == 27: complex_dict[tuple([gui.tech_biomedical_label_price])] = [9999,1.08]
		elif num == 28:  mult_label([gui.cosmetics_synth_colors_label_price],1.08)
		elif num == 29:  mult_label([gui.metals_platinum_label_price],.95)   
		elif num == 30:  mult_label([gui.trans_auto_label_price],.95)
		#31: print("hello"), #TODOASK
		elif num == 32:   
			mult_label([gui.estate_commercial_label_price],.9)
			mult_label([gui.estate_residential_label_price],.92)
		elif num == 33:  mult_label([gui.bonds_gov_label_price,gui.bonds_state_label_price],1.08)
		elif num == 34: 
			mult_label([gui.metals_gold_label_price, gui.metals_bronze_label_price, gui.metals_platinum_label_price,
			gui.metals_copper_label_price, gui.metals_titanium_label_price, gui.metals_silver_label_price,
			gui.bonds_gov_label_price,gui.bonds_state_label_price,gui.estate_commercial_label_price,gui.estate_residential_label_price,
			gui.tech_ai_label_price,gui.tech_biomedical_label_price,gui.tech_cellular_label_price,gui.tech_computers_label_price,
			gui.cosmetics_makeup_label_price,gui.cosmetics_synth_colors_label_price,gui.cosmetics_essential_oils_label_price,
			gui.trans_aerospace_label_price,gui.trans_auto_label_price,gui.trans_railroad_label_price,
			gui.utilities_solar_label_price, gui.utilities_wind_label_price,gui.utilities_nuke_label_price,gui.utilities_coal_label_price,gui.utilities_waste_recycling_label_price],.85)
		elif num == 38: mult_label([gui.metals_platinum_label_price],1.2)
		elif num == 39: mult_label([gui.trans_aerospace_label_price],1.15)
		elif num == 41: mult_label([gui.estate_commercial_label_price,gui.estate_residential_label_price],1.08),
		elif num == 43: #need to add 5 percent
			mult_label([gui.metals_gold_label_price, gui.metals_bronze_label_price, gui.metals_platinum_label_price,
			gui.metals_copper_label_price, gui.metals_titanium_label_price, gui.metals_silver_label_price,
			gui.bonds_gov_label_price,gui.bonds_state_label_price,gui.estate_commercial_label_price,gui.estate_residential_label_price,
			gui.tech_ai_label_price,gui.tech_biomedical_label_price,gui.tech_cellular_label_price,gui.tech_computers_label_price,
			gui.cosmetics_makeup_label_price,gui.cosmetics_synth_colors_label_price,gui.cosmetics_essential_oils_label_price,
			gui.trans_aerospace_label_price,gui.trans_auto_label_price,gui.trans_railroad_label_price,
			gui.utilities_solar_label_price, gui.utilities_wind_label_price,gui.utilities_nuke_label_price,gui.utilities_coal_label_price,gui.utilities_waste_recycling_label_price],.85)
		elif num == 45: mult_label([gui.tech_biomedical_label_price],.80),
		elif num == 47: mult_label(all_metal, 1.12)
		elif num == 48: mult_label([gui.trans_auto_label_price],1.08)
		elif num == 50: mult_label([gui.estate_residential_label_price],1.1)
		elif num == 52: complex_dict.clear() #Stop
		elif num == 54: mult_label([gui.tech_cellular_label_price],1.18)
		elif num == 59: mult_label([gui.estate_residential_label_price],.9)
		elif num == 63: complex_dict[tuple([gui.tech_cellular_label_price])]=[99999,.9]
		elif num == 68: mult_label([gui.estate_residential_label_price],.92)
		elif num == 72: complex_dict.pop(tuple([gui.tech_cellular_label_price]))#delete
		elif num == 77: mult_label([gui.estate_residential_label_price],.88)
		elif num == 81: complex_dict[tuple([gui.tech_computers_label_price])]=[2,1.15]
		elif num == 86: mult_label([gui.estate_residential_label_price],.82)
		elif num == 90: complex_dict[tuple([gui.tech_computers_label_price])]=[9999,.9]
		elif num == 99: 
			complex_dict.pop(tuple([gui.tech_cellular_label_price]))
		elif num == 108:
			complex_dict[tuple([gui.tech_ai_label_price,gui.tech_biomedical_label_price,gui.tech_cellular_label_price,gui.tech_computers_label_price])]=[5,1.1]
		elif num == 117:  mult_label([gui.tech_ai_label_price,gui.tech_biomedical_label_price,gui.tech_cellular_label_price,gui.tech_computers_label_price],.88)
		elif num == 126:  mult_label([gui.tech_ai_label_price,gui.tech_biomedical_label_price,gui.tech_cellular_label_price,gui.tech_computers_label_price],1.1)

	for key, value in complex_dict.items():#TODO Apply Dict Comprehension later
		mult_label(key,value[1])
		value[0] -= 1
		print(value[0])


	complex_dict = {key:val for key, val in complex_dict.items() if val[0] != 0}
	print(complex_dict)

