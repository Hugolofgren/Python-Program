#Hänga gubbe

import random

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

def slumpaOrd():
    slumpIndex = random.randint(0, len(ordlista)-1)
    return ordlista[slumpIndex], betydelse[slumpIndex]

def hangagubbe():
    ordet, ord_betydelse = slumpaOrd()  
    gissade_bokstaver = ["_"] * len(ordet)
    felaktiga_gissningar = []
    antal_fel = 5
    x = True

    while x:
        print("Hänga gubbe!")
        print("\nOrdet: ", " ".join(gissade_bokstaver))
        print("Felaktiga gissningar: ", felaktiga_gissningar)
        print(f"{antal_fel}x gissningar kvar")

        gissning = input("Gissa en bokstav: ").lower()

        if gissning in gissade_bokstaver or gissning in felaktiga_gissningar:
            print(f"Du har redan gissat på {gissning}. Försök igen")
            continue

        if gissning in ordet.lower(): #Kollar om bokstaven finns och sparar den gissade bokstaven
            for slumpIndex, bokstav in enumerate(ordet.lower()):
                if bokstav == gissning:
                    gissade_bokstaver[slumpIndex] = gissning
            
            if "_" not in gissade_bokstaver:
                print("Ordet: ", " ".join(gissade_bokstaver))
                print("Grattis, du har vunnit!")
                print(f"Betydelse: {ord_betydelse}")
                x = False
                break

        #LÄGG IN INMATNINGSFELKONTROLL

        else:
            antal_fel -= 1
            felaktiga_gissningar.append(gissning)
            print(f"Felaktig gissning {gissning}")

        if antal_fel == 0:
            print("Tyvärr, du har förlorat")
            print(f"Det rätta order var: {ordet}")
            x = False  

    spela_igen = input("Vill du spela igen? (ja/nej): ")
    if spela_igen == "ja":
        hangagubbe()
    elif spela_igen == "nej":
        print("Tack för att du har spelat!")


hangagubbe()
  