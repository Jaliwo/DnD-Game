import random

# Personen-Werte
Charakter = {"Name": "Julian", "HP": 20, "Rüstung": 9, "Schwertschaden": 5, "Schadenswürfel": 8}
Enemy_1 = {"Name": "Ork_1", "HP": 10, "Rüstung": 10, "Schwertschaden": 4, "Schadenswürfel": 8}
Enemy_2 = {"Name": "Ork_2", "HP": 10, "Rüstung": 10, "Schwertschaden": 4, "Schadenswürfel": 8}

#____________________________________________________________________________________________________________

# Angreif-Funktion Nahkampf
def attack(Enemy):
	#Würfel_20 Wert
	if Enemy["HP"] > 0:
		Würfelwert_20 = random.randint(1, 20)
		print(f"Der Würfel_20 zeigt {Würfelwert_20} an")
		
	# Schauen, ob Angriff erfolgreich ist, wenn ja:
		if Würfelwert_20 >= int(Enemy["Rüstung"]):
			Würfelwert_Schaden = random.randint(1, int(Enemy["Schadenswürfel"]))
			print(f"Der Schadenswürfel zeigt {Würfelwert_Schaden} an")
			Enemy["HP"] = Enemy["HP"] - (Würfelwert_Schaden + Enemy["Schwertschaden"])
			print(f"Der Angriff trifft und fügt "  + str(Würfelwert_Schaden + int(Enemy["Schwertschaden"])) +  " Schaden zu")
			
		#Wenn nicht
		else:
			print("Der Angriff trifft nicht")	
			
	# Lebensstatus nach Angriff
	if Enemy["HP"] <= 0:
		Enemy["HP"] = 0
		print(Enemy["Name"] + " ist tot\n")
	else:
		print(Enemy["Name"] + " lebt noch und hat " + str(Enemy["HP"]) + " Leben\n")
		
#______________________________________________________________________________________________________________
				
#Simulation Durchlauf
def simulation_durchlauf():
	print("Der Kampf startet\n")
	while Charakter["HP"] > 0 or (Enemy_1["HP"] > 0 and Enemy_2["HP"]) > 0:
	
		print(f"Angriff auf " + Enemy_2["Name"])
		attack(Enemy_2)
		
		if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
			print(f"Der Kampf ist vorbei")
			break
			
		print("Angriff auf " + Enemy_1["Name"])
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
			
#_________________________________________________________________________________________________________
			
#Simulation: Jetzt kann ich den Gegner auswählen, den ich angreifen möchte

def simulation_auswahl():
	print("Der Kampf startet\n")
	
	#Start der Schleife
	while True:
		
		#Anzeige Leben
		print("Charakter HP: " + str(Charakter["HP"]))
		print("Ork_1 HP: " + str(Enemy_1["HP"]))
		print("Ork_2 HP: " + str(Enemy_2["HP"]) + "\n")
		
		
		#Ich wähle den Gegner aus. 
		ziel = input("Wen greift Ihr an?\n")
		
		#Auswahl: Gegner 1
		if ziel == Enemy_1["Name"]:
		
			#Wenn Gegner ausgewählt wird, der schon tot ist, 
			#widerhole Abfrage, damit der lebende Gegner nicht angreift
			if Enemy_1["HP"] == 0:
				print("\nDieser Gegner ist schon tot\n")
				continue
				
			#führe Attacke aus	
			print("\nAngriff auf " + Enemy_1["Name"])
			attack(Enemy_1)
			if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
				print(f"Der Kampf ist vorbei")
				break
				
		#Auswahl: Gegner 2
		elif ziel == Enemy_2["Name"]:
		
			#Wenn Gegner ausgewählt der schon tot ist, 
			#widerhole Abfrage, damit der lebende Gegner nicht angreift
			if Enemy_2["HP"] == 0:
				print("\nDieser Gegner ist schon tot\n")
				continue
				
			#führe Attacke aus
			print("\nAngriff auf " + Enemy_2["Name"])
			attack(Enemy_2)
			if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
				print(f"Der Kampf ist vorbei")
				break
		
		# Widerhole Eingabe, wenn es Gegner nicht gibt		
		else:
			print("Gebt den Namen richtig ein\n")
			continue
			
			
		#Gegner 1 greift nicht weiter an, wenn er tot ist
		while Enemy_1["HP"] > 0:
			if Enemy_1["HP"] == 0:
				break
				
			#Charakter wird von Gegner 1 angegriffen
			else:
				print(Enemy_1["Name"] + " greift " + Charakter["Name"] + " an")
				attack(Charakter)
				break
				
		#	Abfrage, ob eine Partei tot ist	
		if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
			print(f"Der Kampf ist vorbei")
			break
			
		#Gegner 2 greift nicht weiter an, wenn er tot ist
		while Enemy_2["HP"] > 0:
			if Enemy_2["HP"] == 0:
				break
				
			#Charakter wird von Gegner 2 angegriffen
			else:
				print(Enemy_2["Name"] + " greift  " + Charakter["Name"] + " an")
				attack(Charakter)
				break	
		
		#Abfrage, ob eine Partei tot ist				
		if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
			print(f"Der Kampf ist vorbei")
			break
			
#simulation_auswahl()
#simulation_durchlauf()


def simulation_durchlauf_anzahl():

	anzahl_chrakter_gewinnt = 0
	anzahl_gegner_gewinnt = 0	
	for i in range(0, 1000):
		print("Der Kampf startet")
		while True:
			
		
		
			print(f"Angriff auf " + Enemy_2["Name"])
			attack(Enemy_2)
			
			if Charakter["HP"] == 0:
				anzahl_gegner_gewinnt += 1
				
			if (Enemy_1["HP"] == 0 and Enemy_2["HP"] == 0):
				anzahl_chrakter_gewinnt += 1
			
			if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
				print(f"Der Kampf ist vorbei")
				
				Charakter["HP"] = 20
				Enemy_1["HP"] = 10
				Enemy_2["HP"] = 10
				break
				
				
			print("Angriff auf " + Enemy_1["Name"])
			attack(Enemy_1)
			
			if Charakter["HP"] == 0:
				anzahl_gegner_gewinnt += 1
				
			if (Enemy_1["HP"] == 0 and Enemy_2["HP"] == 0):
				anzahl_chrakter_gewinnt += 1
				
			if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
				print(f"Der Kampf ist vorbei")
				
				Charakter["HP"] = 20
				Enemy_1["HP"] = 10
				Enemy_2["HP"] = 10
				break
				
			if Enemy_1["HP"] != 0:
				print(f"Angriff auf " + Charakter["Name"])
				attack(Charakter)
				
			if Charakter["HP"] == 0:
				anzahl_gegner_gewinnt += 1
				
			if (Enemy_1["HP"] == 0 and Enemy_2["HP"] == 0):
				anzahl_chrakter_gewinnt += 1	
				
			if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
				print(f"Der Kampf ist vorbei")
				
				Charakter["HP"] = 20
				Enemy_1["HP"] = 10
				Enemy_2["HP"] = 10
				break
				
			if Enemy_2["HP"] != 0:
				print(f"Angriff auf " + Charakter["Name"])
				attack(Charakter)
				
			
			
			if Charakter["HP"] == 0:
				anzahl_gegner_gewinnt += 1
				
			if (Enemy_1["HP"] == 0 and Enemy_2["HP"] == 0):
				anzahl_chrakter_gewinnt += 1
				
			if Charakter["HP"] == 0 or (Enemy_1["HP"] == 0 and  Enemy_2["HP"] == 0):
				print(f"Der Kampf ist vorbei")
				Charakter["HP"] = 20
				Enemy_1["HP"] = 10
				Enemy_2["HP"] = 10
				break
				
			
				
		print("Anzahl Charackter gewonnen: " + str(anzahl_chrakter_gewinnt))
		print("Anzahl Gegner gewonnen: " + str(anzahl_gegner_gewinnt))
		
simulation_durchlauf_anzahl()
