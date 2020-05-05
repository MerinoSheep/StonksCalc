#Reference google doc for documentation 
from math import ceil

def num(num,gui):
	def mult_label(label,num):
		for i in label:
			i['text'] = ceil(int(i['text'])*num)
	try:
		num = int(num)
	except ValueError:
		print("No number or no input")
#TODO SWITCH TO DICTIONARY LATER, SIMPLE ONES 
	if num == 0:
		pass
	elif num == 2:
		mult_label([gui.metals_gold_label_price,gui.metals_bronze_label_price,gui.metals_platinum_label_price,
		gui.metals_copper_label_price,gui.metals_titanium_label_price,gui.metals_silver_label_price],1.1)

	elif num == 3:
		mult_label([gui.trans_aerospace_label_price],.8)
	elif num == 4:
		mult_label(gui.utilities_nuke_label_price,.85)
		mult_label([gui.utilities_solar_label_price,gui.utilities_wind_label_price,gui.utilities_coal_label_price],1.1)
	elif num == 5:
		pass
		#TODOASK
	elif num == 6 : 
		mult_label([gui.bonds_gov_label_price],1.1)
	elif num == 7 :
		mult_label([gui.metals_gold_label_price,gui.metals_bronze_label_price,gui.metals_platinum_label_price,
		gui.metals_copper_label_price,gui.metals_titanium_label_price,gui.metals_silver_label_price],1.1)

		#TODOASK
	elif num == 11 :
		mult_label([gui.tech_ai_label_price],*.88)
	elif num == 12 :
		pass
		#TODO ASK
	elif num == 13 :
		pass
	elif num == 14 :
		pass
	elif num == 15:
		mult_label([gui.bonds_gov_label_price,gui.bonds_state_label_price],1.05)
	elif num == 16:
		pass
		#TODOASK
	elif num == 18:
		pass
		#TODOASK
	elif num == 19:
		mult_label([gui.cosmetics_makeup_label_price],.8)
	elif num == 20:
		mult_label([gui.metals_titanium_label_price],.8)
	elif num == 21:
		mult_label([gui.trans_auto_label_price],1.12)
	elif num == 22:
		mult_label([gui.utilities_coal_label_price],1.05)
	elif num == 23:
		mult_label([gui.estate_commercial_label_price],1.15)