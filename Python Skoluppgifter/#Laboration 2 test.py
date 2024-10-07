#Laboration 2

import random
#Variabler för ordlistor 

def spela_hangagubbe():
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
    ordet = random.choice(ordlista)
    gissade_bokstaver = ["_"] * len(ordet)
    felaktiga_gissningar = []
    antal_fel = 5

    while True:
        print("\nOrdet: ", " ".join(gissade_bokstaver))
        print("Felaktiga gissningar: ", felaktiga_gissningar)
        print("Antal kvarvarande felaktiga försök: ", antal_fel)

        gissning = input("Gissa en bokstav: ").lower()

                
        if len(gissning) != 1 or not gissning.isalpha():
            print("Ogiltig gissning. Skriv bara en bokstav.")
            continue

        if gissning in gissade_bokstaver or gissning in felaktiga_gissningar:
            print(f"Du har redan gissat på {gissning}. Försök igen!")
            continue

        if gissning in ordet:
            for index, bokstav in enumerate(ordet):
                if bokstav == gissning:
                    gissade_bokstaver[index] = gissning
                
                    if "_" not in gissade_bokstaver:
                        print("Ordet: ", " ".join(gissade_bokstaver))
                        print("Grattis, du har vunnit!")
                        print(f"Betydelse: {betydelse[index]}")
                        break
                    
                    else: 
                        antal_fel -= 1
                        felaktiga_gissningar.append(gissning)
                        print(f"Felaktig gissning: {gissning}")

                        if antal_fel == 0:
                            print(f"Du förlorade! Ordet var: {ordet}")
                            print(f"Betydelse: {betydelse}")
                            break

        spela_igen = input("Vill du spela igen? (ja/nej): ").lower()
        if spela_igen == 'ja':
            spela_hangagubbe()


spela_hangagubbe()



    








# def slumpaOrd():
#     
#     return ordlista[slumpindex], betydelse[slumpindex]

# #kod för att testa funktionen

# testOrd, testBetydelse = slumpaOrd()
# print(testOrd)
# print(testBetydelse)




