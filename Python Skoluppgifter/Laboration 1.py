#Laboration 1

#importerar random och time modulen
import random 
import time 

#Tärningar i tärnings_spel
def kasta_tarningar():
    return random.randint(1, 6) + random.randint(1, 6)

#Tärningsspelet där sparas kast i listor.
def tarnings_spel(rounds):
    userWins = 0
    computerWins = 0
    userThrows = []
    computerThrows = []
    
    for round in range(1, rounds + 1):
    #Användarens kast
            userthrow = kasta_tarningar()
            userThrows.append(userthrow)
    #Datorns kast
            computerthrow = kasta_tarningar()
            computerThrows.append(computerthrow)

        #Printar resultatet för varje runda med hänsyn till vem som vann omgången.
            if userthrow > computerthrow:
                print(f"Omgång {round}: Du vann! (Du: {userthrow}, Datorn: {computerthrow})")
                userWins += 1
                time.sleep(1)
            elif userthrow < computerthrow:
                print(f"Omgång {round}: Datorn vann! (Du: {userthrow}, Datorn: {computerthrow})")
                computerWins += 1
                time.sleep(1) 
            else:
                print(f"Omgång {round}: Oavgjort! (Du: {userthrow}, Datorn: {computerthrow})")
                time.sleep(1)
                


#Slutresultat
    print("\nSpelet är över!")
    print(f"Totalt: Du vann {userWins} omgångar och datorn vann {computerWins} omgångar.")

#Avgör vem som vann spelet
    if userWins > computerWins:
        print("Grattis, du vann spelet")
        print("") 
    
    elif userWins < computerWins:
        print("Datorn vann spelet")
        print("")

    else:
        print("Spelet blev oavgjort")
        print("") 
    
#Beräkna statistiken
    user_avg = sum(userThrows) / len(userThrows)
    computer_avg = sum(computerThrows) / len(computerThrows)
    user_min = min(userThrows)
    user_max = max(userThrows)
    computer_min = min(computerThrows)
    computer_max = max(computerThrows)

#Skriver ut statistiken
    print("Statistik")  
    print(f"Ditt medelvärde: {user_avg:.1f}")
    print(f"Datorns medelvärde: {computer_avg:.1f}")
    print(f"Ditt lägsta kast: {user_min}, ditt högsta kast: {user_max}")
    print(f"Datorns lägsta kast: {computer_min}, datorns högsta kast: {computer_max}")
    

    # Fråga om de vill spela igen
    spela_igen = input("Vill du spela igen? (ja/nej): ")
    if spela_igen == "ja":
        rounds = int(input("Hur många rundor vill du spela? "))
        tarnings_spel(rounds)
    else:
        print("Återvänder till huvudmenyn.")

#Funktion för menyval 2 som kallar på tärningsspelet
def menyval_2():
    rounds = int(input("Hur många gånger vill du spela? "))
    if rounds > 0:
        tarnings_spel(rounds)

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
        gissa_tal()
    else:
        print("Återvänder till huvudmenyn.")

#Huvudmenyn eller den sk mainloopen
def huvudmeny():
    while True:
        #Menyval
        print("Välkommen till huvudmenyn! ")
        print("1. Information om vilka som skapat programmet!")
        print("2. Tärningsspel! ")
        print("3. Gissa tal mellan 1-100! ")
        print("4. Avsluta programmet")

        menyval = int(input("Välj i menyn mellan 1-4! "))

        if menyval == 1:
            print("Skaparen av programmet är...")

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