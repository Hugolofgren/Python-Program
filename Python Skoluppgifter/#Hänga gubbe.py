#Hänga gubbe 

import random
import os 

#Ordlista och betydelser för spelet
ordlista = ["Vispgrädde", "Ukulele", "Innebandyspelare", "Flaggstång", "Yxa", "Havsfiske", "Prisma", "Landsbygd", "Generositet", "Lyckosam", "Perrong", "Samarbeta", "Välartad"] 

betydelse = ["Uppvispad grädde",
"Ett fyrsträngat instrument med ursprung i Portugal",
"En person som spelar sporten innebandy",
"En mast man hissar upp en flagga på",
"Verktyg för att hugga ved",
"Fiske till havs",
"Ett transparent optiskt element som bryter ljuset vid plana ytor",
"Geografiskt område med lantlig bebyggelse",
"En personlig egenskap där man vill dela med sig av det man har",
"Att man ofta, eller för stunden har tur",
"Den upphöjda yta som passagerare väntar på eller stiger på/av ett spårfordon",
"Att arbeta tillsamans mot ett gemensamt mål",
"Att någon är väluppfostrad, skötsam, eller lovande"]

#Funktion för att slumpa ord ur ordlistan som också hämtar ordets betydelse
def slumpaOrd():
    slumpIndex = random.randint(0, len(ordlista)-1)
    return ordlista[slumpIndex], betydelse[slumpIndex]

#Funktion för hänga gubbe spelet
def hanga_gubbe():
    print("Hänga gubbe!")
    ordet, ord_betydelse = slumpaOrd()  
    gissade_bokstaver = ["_"] * len(ordet)
    felaktiga_gissningar = []
    antal_fel = 5
    x = True

#Loop för spelets gång, printar först ut status för omgången. Därefter frågas spelaren om en bokstav. 
    while x:
        print("\nOrdet: ", " ".join(gissade_bokstaver))
        print("Felaktiga gissningar: ", felaktiga_gissningar)
        print(f"{antal_fel}x gissningar kvar")

        gissning = input("Gissa en bokstav: ").lower()

#Inmatningsfelkontroll, om en siffra, fler än en bokstav eller en redan gissat bokstav skrivs printas ett felmeddelande. 
        if not gissning.isalpha():
            print("Vänligen ange en bokstav!")
            continue
        elif len(gissning) != 1:
            print("Vänligen gissa på en bokstav i taget!")
            continue

        if gissning in gissade_bokstaver or gissning in felaktiga_gissningar:
            print(f"Du har redan gissat på {gissning}. Försök igen")
            continue

#Kollar om bokstaven finns och uppdaterar den på rätt plats. 
        if gissning in ordet.lower(): 
            for slumpIndex, bokstav in enumerate(ordet.lower()):
                if bokstav == gissning:
                    gissade_bokstaver[slumpIndex] = gissning
            
            if "_" not in gissade_bokstaver:
                print("Ordet: ", " ".join(gissade_bokstaver))
                print("Grattis, du har vunnit!")
                print(f"Betydelse: {ord_betydelse}")
                x = False
                break
            
#Räknar antalet felaktiga gissningar, om antal fel = 0 avslutas loopen då spelaren förlorat. 
        else:
            antal_fel -= 1
            felaktiga_gissningar.append(gissning)
            print(f"Felaktig gissning {gissning}")

        if antal_fel == 0:
            print("")
            print("Tyvärr, du har förlorat")
            print(f"Det rätta order var: {ordet}")
            x = False  

#Kollar om man vill spela igen
    spela_igen = input("Vill du spela igen? (ja/nej): ")
    if spela_igen == "ja":
        os.system('cls')
        hanga_gubbe()
    elif spela_igen == "nej":
        print("Tack för att du har spelat!")
        

#Startar spelet
hanga_gubbe()
  