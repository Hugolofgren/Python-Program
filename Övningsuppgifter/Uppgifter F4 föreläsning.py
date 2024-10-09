#Uppgift 1
#Fråga användaren vilken multiplikationstabell som ska skrivas ut (tex 3:ans)
#Fråga användaren hur många tal i tabellen som ska skrivas ut (tex 10st)
#Gör en loop som skriver ut tabellen
#Utskrift blir tex:
#3
#6
#9
#..
#30

    #Svar:
    # user_input = int(input('Input number: '))

    # for number in range(11):
    #    print(number*user_input)


#Uppgift 2
#Fråga användaren hur mycket pengar den har (tex 40:-)
#Fråga användaren hur gammal den är (tex 22 år)
#Kolla om användaren har råd med en bussbiljett
#- En biljett kostar 25:- om man är yngre än 20 år, annars 50:-
#Skriv ut resultatet för användaren

    #Svar:

ticketunder20 = 25 
ticketover20 = 50

user_money = int(input('Hur mycket pengar har du?: '))
user_age = int(input('Hur gammal är du?: '))

if user_age < 20 and user_money >= 25:
    print('Du har råd att åka buss och det kostar 25kr')

elif user_age > 20 and user_money >= 50:
    print('Du har råd att åka buss och det kostar 50kr')

else:
    print('Du har inte råd att åka buss')


