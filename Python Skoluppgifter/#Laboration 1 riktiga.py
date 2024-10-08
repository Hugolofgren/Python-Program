#Laboration 1

#importerar random och time modulen
import random 
import time 
import os

#Tärningar i tärnings_spel
def kasta_tarningar():
    return random.randint(1, 6) + random.randint(1, 6)

#Tärningsspelet där kast sparas i listor.
def tarnings_spel(rundor):
    spelare_vinster = 0
    dator_vinster = 0
    spelare_kast = []
    dator_kast = []

#Loop för spelets gång     
    for omgang in range(1, rundor + 1):
    #Användarens kast
            tarningar_spelare = kasta_tarningar()
            spelare_kast.append(tarningar_spelare)
    #Datorns kast
            tarningar_dator = kasta_tarningar()
            dator_kast.append(tarningar_dator)

        #Printar resultatet för varje runda med hänsyn till vem som vann omgången.
            if tarningar_spelare > tarningar_dator:
                print(f"Omgång {omgang}: Du vann! (Du: {tarningar_spelare}, Datorn: {tarningar_dator})")
                spelare_vinster += 1
                time.sleep(1)
            elif tarningar_spelare < tarningar_dator:
                print(f"Omgång {omgang}: Datorn vann! (Du: {tarningar_spelare}, Datorn: {tarningar_dator})")
                dator_vinster += 1
                time.sleep(1) 
            else:
                print(f"Omgång {omgang}: Oavgjort! (Du: {tarningar_spelare}, Datorn: {tarningar_dator})")
                time.sleep(1)
                


#Slutresultat
    print("\nSpelet är över!")
    print(f"Totalt: Du vann {spelare_vinster} omgångar och datorn vann {dator_vinster} omgångar.")

#Avgör vem som vann spelet
    if spelare_vinster > dator_vinster:
        print("Grattis, du vann spelet")
        print("") 
    
    elif spelare_vinster < dator_vinster:
        print("Datorn vann spelet")
        print("")

    else:
        print("Spelet blev oavgjort")
        print("") 
    
#Beräkna statistiken
    spelare_avg = sum(spelare_kast) / len(spelare_kast)
    dator_avg = sum(dator_kast) / len(dator_kast)
    spelare_min = min(spelare_kast)
    spelare_max = max(spelare_kast)
    dator_min = min(dator_kast)
    dator_max = max(dator_kast)

#Skriver ut statistiken
    print("Statistik")  
    print(f"Ditt medelvärde: {spelare_avg:.1f}")
    print(f"Datorns medelvärde: {dator_avg:.1f}")
    print(f"Ditt lägsta kast: {spelare_min}, ditt högsta kast: {spelare_max}")
    print(f"Datorns lägsta kast: {dator_min}, datorns högsta kast: {dator_max}")
    print("")
    

    # Fråga om de vill spela igen
    spela_igen = input("Vill du spela igen? (ja/nej): ")
    if spela_igen == "ja":
        os.system('cls')
        rundor = int(input("Hur många rundor vill du spela? "))
        tarnings_spel(rundor)
    else:
        print("Återvänder till huvudmenyn.")
        os.system('cls')

#Funktion för menyval 2 som kallar på tärningsspelet
def menyval_2():
    rundor = int(input("Hur många gånger vill du spela? "))
    print("")
    if rundor > 0:
        tarnings_spel(rundor)

    else:
        print("Ange ett positivt heltal. ")

#Gissa tal spelet
def gissa_tal():
    hemligt_tal = random.randint(1, 100) 
    gissningar = 0
    rätt_gissningar = 0

    while True:            
        gissning = int(input("Gissa ett tal mellan 1-100: "))
        gissningar += 1

                
        if gissning < hemligt_tal:
            print("För lågt!")
        elif gissning > hemligt_tal:
            print("För högt!")
        else:
            print(f"Rätt gissat! Antal gissningar: {gissningar}")

            if gissningar <= 7:
                print("Bra jobbat! ")
                rätt_gissningar += 1
                break
            else:
                print("Så många försök borde det inte ta, försök igen")
                rätt_gissningar = 0
                break

    if rätt_gissningar == 3:
        print("Du använder bevisligen en bra gissningsstrategi")

#Funktion för att fråga användaren om den vill spela igen eller återgå till huvudloopen
    spela_igen = input("Vill du spela igen? (ja/nej): ")
    if spela_igen == "ja":
        os.system('cls')
        gissa_tal()
    else:
        print("Återvänder till huvudmenyn.")
        os.system('cls')

#Huvudmenyn eller den sk mainloopen
def huvudmeny():
    while True:
        #Menyval
        print("Välkommen till huvudmenyn! ")
        print("")
        print("1. Information om vilka som skapat programmet!")
        print("2. Tärningsspel! ")
        print("3. Gissa tal mellan 1-100! ")
        print("4. Avsluta programmet")
        print("")

        menyval = int(input("Välj i menyn mellan 1-4! "))

        if menyval == 1:
            print("Skaparen av programmet är...")
            print("")

        elif menyval == 2:
            menyval_2()

        elif menyval == 3:
            gissa_tal()
        
        elif menyval == 4:
            print("Programmet avslutas. Tack för att du spelade! ")
            break

        else:
            print("Ogiltigt val, försök igen! ")
            

#Gör så att huvudmenyn startar först.    
huvudmeny()   