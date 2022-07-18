import random

# Personen-Werte
Charackter = {"Name": "Julian", "HP": 15, "Rüstung": 15, "Schwertschaden": 4, "Schadenswürfel": 8}
Enemy_1 = {"Name": "Ork_1", "HP": 7, "Rüstung": 5, "Schwertschaden": 2, "Schadenswürfel": 6}
Enemy_2 = {"Name": "Ork_2", "HP": 7, "Rüstung": 5, "Schwertschaden": 2, "Schadenswürfel": 6}




# Angreif-Funktion
def attack(Enemy):
	#Würfel_20 Wert
	if Enemy["HP"] > 0:
		Würfelwert_20 = random.randint(1, 20)
		print(f"Der Würfel_20 zeigt {Würfelwert_20} an")
	
	#Schauen, ob Angriff erfolgreich ist, wenn ja:
		if Würfelwert_20 > int(Enemy["Rüstung"]):
			Würfelwert_Schaden = random.randint(1, int(Enemy["Schadenswürfel"]))
			print(f"Der Schadenswürfel zeigt {Würfelwert_Schaden} an")
			Enemy["HP"] = Enemy["HP"] - (Würfelwert_Schaden + Charackter["Schwertschaden"])
			print(f"Der Angriff trifft und fügt "  + str(Würfelwert_Schaden + int(Charackter["Schwertschaden"])) +  " Schaden zu")
			
		#Wenn nicht	
		else: 
			print("Der Angriff trifft nicht")
	#elif Enemy["HP"] <= 0:
		
		
	#	If-Schleife für HP Abfrage nach Angriff
	if Enemy["HP"] <= 0:
		Enemy["HP"] = 0 
		print(Enemy["Name"] + " ist tot\n")
	else:
		print(Enemy["Name"] + " lebt noch und hat " + str(Enemy["HP"]) + " Leben\n")
		
#Simulation
print("Der Kampf startet\n")
while Charackter["HP"] > 0 or (Enemy_1["HP"] > 0 and Enemy_2["Hp"]) > 0:
	
	print(f"Angriff auf " + Enemy_2["Name"])
	attack(Enemy_2) 
	
	if Charackter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
		print(f"Der Kampf ist vorbei")
		break
		
	print(f"Angriff auf " + Enemy_1["Name"])	
	attack(Enemy_1)
	
	if Charackter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
		print(f"Der Kampf ist vorbei")
		break
	print(f"Angriff auf " + Charackter["Name"])	
	attack(Charackter)
	
	if Charackter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
		print(f"Der Kampf ist vorbei")
		break
	print(f"Angriff auf " + Charackter["Name"])	
	attack(Charackter)
	
	if Charackter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
		print(f"Der Kampf ist vorbei")
		break
	
