
import random

# Personen-Werte
Charakter = {"Name": "Julian", "HP": 50, "Rüstung": 10, "Schwertschaden": 2, "Schadenswürfel": 6}
Enemy_1 = {"Name": "Ork_1", "HP": 25, "Rüstung": 10, "Schwertschaden": 4, "Schadenswürfel": 8}
Enemy_2 = {"Name": "Ork_2", "HP": 25, "Rüstung": 10, "Schwertschaden": 4, "Schadenswürfel": 8}

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
                
#Simulation Durchlauf, ich greife beide nach einander an
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

#________________________________________________________________________________________
def simulation_durchlauf_anzahl():
    #Start der Zählung für Ergebnis
    anzahl_chrakter_gewinnt = 0
    anzahl_gegner_gewinnt = 0	
    x = int(input("Gibt die Durchlaufzahl ein: "))
    #For-Schleife: Anzahl der Kämpfe
    for durchlauf in range(0, x):
        print("""Der Kampf startet""")
        #While-Schleife wird durchbrochen sobald die Lebenspunkte des Charakter auf 0 ist,
        #oder die Lebenspunkte aller Gegner auf 0 sind
        while True:
            #Taktik: Greife zuerst einen Gegner an, danach den nächsten.
            #Macht Sinn, wenn 1 VS. 2
            #Solange Lebenspunkte von Gegner 2 nicht 0, greife erst diesen an
            if Enemy_2["HP"] > 0:
            
                print(f"Angriff auf " + Enemy_2["Name"])
                attack(Enemy_2)
                
                #Wenn nach dem Angriff beide Genger tot sind, setze Zähler für Charaktergewinn eins nach oben
                if (Enemy_1["HP"] == 0 and Enemy_2["HP"] == 0):
                    anzahl_chrakter_gewinnt += 1
                #wenn beide Gegner tot, beende Kampf und setze HP zurück
                    print("""Der Kampf ist vorbei\n""")
                    
                    Charakter["HP"] = 50
                    Enemy_1["HP"] = 25
                    Enemy_2["HP"] = 25
                    break
                    
            #Wenn erster Gegner schon tot, greife immer zweiten Gegner 		
            elif Enemy_2["HP"] <= 0:
                
                print("Angriff auf " + Enemy_1["Name"])
                attack(Enemy_1)
                
                #Wenn beide Gegner durch Angriff tot, setze Zähler für Charaktergewinn 1 hoch	
                if (Enemy_1["HP"] == 0 and Enemy_2["HP"] == 0):
                    anzahl_chrakter_gewinnt += 1
                    print(f"Der Kampf ist vorbei\n")
                    Charakter["HP"] = 50
                    Enemy_1["HP"] = 25
                    Enemy_2["HP"] = 25
                    break
            
            #Gegner greifen an		
            if (Enemy_1["HP"] and Enemy_2["HP"]) != 0:
                for i in range(0, 2):
                    print(f"Angriff auf " + Charakter["Name"])
                    attack(Charakter)
                    if Charakter["HP"]==0:
                        break
                        
                
            elif Enemy_1["HP"] != 0 and Enemy_2["HP"] == 0:
                print(f"Angriff auf " + Charakter["Name"])
                attack(Charakter)
                
            
            if Charakter["HP"] == 0:
                anzahl_gegner_gewinnt += 1
                print(f"Der Kampf ist vorbei\n")
                Charakter["HP"] = 50
                Enemy_1["HP"] = 25
                Enemy_2["HP"] = 25
                break
                
            
                
        print("Anzahl Charackter gewonnen: " + str(anzahl_chrakter_gewinnt))
        print("Anzahl Gegner gewonnen: " + str(anzahl_gegner_gewinnt) + "\n")



def spiel_auswahl_endlossschleife():
    game = True

    Charakter["Name"] = input("Gib den Namen deines Helden ein, diesen Kannst du während des Spiels nicht mehr ändern! \n")
    if Charakter["Name"] == "Hurensohn":
        print("Du bist wahrlich ein Hurensohn, auf in die Schlacht Hurensohn")
  
    while True:
        Enemy_1["Name"] = input("Gib den Namen des ersten Gegners ein, diesen Kannst du während des Spiels nicht mehr ändern! \n")
        Enemy_2["Name"] = input("Gib den Namen des zweiten Gegners ein, diesen Kannst du während des Spiels nicht mehr ändern! \n")

        if Enemy_1["Name"] == Enemy_2["Name"]:
            print("Die beiden Gegner können nicht gleich heißen. Vergib die Namen der Gegner noch einmal neu\n")

        elif Charakter["Name"] == Enemy_1["Name"] or Charakter["Name"] == Enemy_2["Name"]:
            print("Die Gegner können nicht wie dein Held heißen")
        else:
            break

    while game == True:

        
        spielstart = input("\nSpiel Starten? Drücke Y für Ja und N für Nein\n")
        
        

        if spielstart == "Y" or spielstart == "y":
            
            print(Charakter)
            print(Enemy_1)
            print(Enemy_2)
            werte_aendern()
            simulation_auswahl()
        
        elif spielstart == "N" or spielstart == "n":
            print("Das Spiel wird beendet")
            game = False
        else:
            print("Gib bitte Y oder N ein")


def werte_aendern():
    loop_werte_aendern = True
    while loop_werte_aendern == True: 
        eig_andern = input("Eigenschaften ändern? Y/N \n")
        if eig_andern == "Y" or eig_andern== "y":
            char_auswahl = input("Werte welches Kämpfers ändern? \n")
            if char_auswahl == Charakter["Name"]:
                eig_a_chr = input("Welche Eigenschft möchtest du ändern? (HP, Rüstung, Schwertschaden, Schadenswürfel) \n")
                if eig_a_chr == "HP": 
                    Charakter["HP"] = int(input("Wie viel Leben soll dein Held haben? \n"))
                elif eig_a_chr == "Rüstung":
                    Charakter["Rüstung"] = int(input("Wie viel Rüstung soll dein Held haben? \n"))
                elif eig_a_chr == "Schwertschaden":
                    Charakter["Schwertschaden"] = int(input("Wie viel Grundschaden sollen deine Gegner auf dich machen? \n"))
                elif eig_a_chr == "Schadenswürfel":
                    Charakter["Schadenswürfel"] = int(input("Welchen Schadenwürfel sollen deine Gegner haben? \n"))
                else:
                    print("Gib HP, Rüstung, Schwertschaden oder Schadenswürfel ein")

            elif char_auswahl == Enemy_1["Name"]:
                eig_a_chr = input("Welche Eigenschft möchtest du ändern? (S. Liste Anfang) \n")
                if eig_a_chr == "HP": 
                    Enemy_1["HP"] = int(input("Wie viel Leben soll dein Gegner haben? \n"))
                elif eig_a_chr == "Rüstung":
                    Enemy_1["Rüstung"] = int(input("Wie viel Rüstung soll dein Gegner haben? \n"))
                elif eig_a_chr == "Schwertschaden":
                    Enemy_1["Schwertschaden"] = int(input("Wie viel Grundschaden sollen dein Held gegen Gegner machen? \n"))
                elif eig_a_chr == "Schadenswürfel":
                    Enemy_1["Schadenswürfel"] = int(input("Welchen Schadenwürfel sollen dein Held gegen Gegner haben ? \n"))
                else:
                    print("Gib HP, Rüstung, Schwertschaden oder Schadenswürfel ein")

            elif char_auswahl == Enemy_2["Name"]:
                eig_a_chr = input("Welche Eigenschft möchtest du ändern? (S. Liste Anfang) \n")
                if eig_a_chr == "HP": 
                    Enemy_2["HP"] = int(input("Wie viel Leben soll dein Gegner haben? \n"))
                elif eig_a_chr == "Rüstung":
                    Enemy_2["Rüstung"] = int(input("Wie viel Rüstung soll dein Gegner haben? \n"))
                elif eig_a_chr == "Schwertschaden":
                    Enemy_2["Schwertschaden"] = int(input("Wie viel Grundschaden sollen dein Held gegen Gegner machen? \n"))
                elif eig_a_chr == "Schadenswürfel":
                    Enemy_2["Schadenswürfel"] = int(input("Welchen Schadenwürfel sollen dein Held gegen Gegner haben ? \n"))
                else: 
                    print("Gib Gib HP, Rüstung, Schwertschaden oder Schadenswürfel ein")
            else:
                print("Diesen nahmen gibt es nicht")
                

        elif eig_andern == "N" or eig_andern == "n":
            print(Charakter)
            print(Enemy_1)
            print(Enemy_2)
            loop_werte_aendern = False
        else:
            print("Gib Y oder N ein")

    









#simulation_durchlauf_anzahl()
#simulation_auswahl()
#simulation_durchlauf()
spiel_auswahl_endlossschleife()
#werte_aendern()