import random

# Personen-Werte
Charakter = {"Name": "Julian", "HP": 30, "Rüstung": 15, "Schwertschaden": 4, "Schadenswürfel": 6}
Enemy_1 = {"Name": "Ork_1", "HP": 7, "Rüstung": 5, "Schwertschaden": 4, "Schadenswürfel": 8}
Enemy_2 = {"Name": "Ork_2", "HP": 25, "Rüstung": 5, "Schwertschaden": 4, "Schadenswürfel": 8}




# Angreif-Funktion
def attack(Enemy):
	#Würfel_20 Wert
	if Enemy["HP"] > 0:
		Würfelwert_20 = random.randint(1, 20)
		print(f"Der Würfel_20 zeigt {Würfelwert_20} an")
	
	#Schauen, ob Angriff erfolgreich ist, wenn ja:
		if Würfelwert_20 >= int(Enemy["Rüstung"]):
			Würfelwert_Schaden = random.randint(1, int(Enemy["Schadenswürfel"]))
			print(f"Der Schadenswürfel zeigt {Würfelwert_Schaden} an")
			Enemy["HP"] = Enemy["HP"] - (Würfelwert_Schaden + Enemy["Schwertschaden"])
			print(f"Der Angriff trifft und fügt "  + str(Würfelwert_Schaden + int(Charakter["Schwertschaden"])) +  " Schaden zu")
			
		#Wenn nicht	
		else: 
			print("Der Angriff trifft nicht")
	
		
		
	#	If-Schleife für HP Abfrage nach Angriff
	if Enemy["HP"] <= 0:
		Enemy["HP"] = 0 
		print(Enemy["Name"] + " ist tot\n")
	else:
		print(Enemy["Name"] + " lebt noch und hat " + str(Enemy["HP"]) + " Leben\n")
		
#Simulation Durchlauf
def simulation_durchlauf():
	print("Der Kampf startet\n")
	while Charakter["HP"] > 0 or (Enemy_1["HP"] > 0 and Enemy_2["Hp"]) > 0:
		
		print(f"Angriff auf " + Enemy_2["Name"])
		attack(Enemy_2) 
		
		if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
			print(f"Der Kampf ist vorbei")
			break
			
		print(f"Angriff auf " + Enemy_1["Name"])	
		attack(Enemy_1)
		
		if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
			print(f"Der Kampf ist vorbei")
			break
		if Enemy_1["HP"] != 0:
			print(f"Angriff auf " + Charakter["Name"])	
			attack(Charakter)
		
		if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
			print(f"Der Kampf ist vorbei")
			break
		
		if Enemy_2["HP"] != 0:
			print(f"Angriff auf " + Charakter["Name"])	
			attack(Charakter)
		
		if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
			print(f"Der Kampf ist vorbei")
			break
		
#simulation_jetzt kann ich den Gegner auswählen, den ich angreifen möchte

def simulation_auswahl():
	print("Der Kampf startet")
	while Charakter["HP"] > 0 or (Enemy_1["HP"] > 0 and Enemy_2["Hp"]) > 0:
			
		
		#Ich wähle den Gegner aus. Wenn Name nicht existiert, wiederholte Abfrage
		ziel = input("Wen greift Ihr an?\n")
		#Gegner 1
		if ziel == Enemy_1["Name"]:
			
			#Wenn Gegner ausgewählt der schon tot ist, widerhole Abfrage, damit der lebende Gegner nicht angreift
			if Enemy_1["HP"] == 0:
				print("Dieser Gegner ist schon tot")
				continue
				
		
			print(f"Angriff auf " + Enemy_1["Name"])
			attack(Enemy_1) 
			if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
				print(f"Der Kampf ist vorbei")
				break
				
		#Gegner 2	
		elif ziel == Enemy_2["Name"]:
			
			if Enemy_2["HP"] == 0:
				print("Dieser Gegner ist schon tot")
				continue
				
			print(f"Angriff auf " + Enemy_2["Name"])	
			attack(Enemy_2)
			if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
				print(f"Der Kampf ist vorbei")
				break
				
		else:
			print("Gebt den Namen richtig ein")
			continue
			
			
		#Genger 1 greift nicht an, wenn er tot ist
		while Enemy_1["HP"] > 0:
			if Enemy_1["HP"] == 0:
				break
			else:
				print(Enemy_1["Name"] + " greift " + Charakter["Name"] + " an")	
				attack(Charakter)
				break
			
		if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
			print(f"Der Kampf ist vorbei")
			break
		
		#Gegner 1 greift nicht weiter an, wenn er tot ist
		while Enemy_2["HP"] > 0:
			if Enemy_2["HP"] == 0:
				break
			else:
				print(Enemy_2["Name"] + " greift  " + Charakter["Name"] + " an")	
				attack(Charakter)
				break	
		
		
		
		if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
			print(f"Der Kampf ist vorbei")
			break
			
#simulation_auswahl()
simulation_durchlauf()
	
