#Sten sax påse

import random

user_wins = 0
computer_wins = 0

options = ["sten", "sax", "påse"]

while True:
    user_input = input("Skriv Sten/Sax/Påse eller q för att avsluta: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #Sten: 0, Sax: 1, Påse: 2
    computer_pick = options[random_number]
    print("Datorn valde", computer_pick + ".")

    if user_input == "sten" and computer_pick == "sax":
        print("Du vann!")
        user_wins += 1

    elif user_input == "sax" and computer_pick == "påse":
        print("Du vann!")
        user_wins += 1

    elif user_input == "påse" and computer_pick == "sten":
        print("Du vann!")
        user_wins += 1
    
    else:
        print("Du förlorade!")
        computer_wins += 1

print("Du vann", user_wins, "gånger")
print("Datorn vann", computer_wins, "gånger")
print("Hejdå!")