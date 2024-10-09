minuter = int(input('Ange antal minuter du uppskattar ringa: '))

if minuter < 33:
    print('Välj kontant')

if minuter >= 33:
    if minuter <= 66:
        print('Välj normal')

if minuter > 66:
    print('Välj plus')