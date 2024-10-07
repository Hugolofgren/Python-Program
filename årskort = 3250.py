x = int(input('Skriv din brevs längd: '))
y = int(input('Skriv din brevs bredd: '))
z = int(input('Skriv din brevs tjocklek: '))

if x > 600 or x < 140:
    print('Brevet är får vara mellan 140 mm eller 600mm långt: ')

if y < 90:
    print('Brevet är för smalt: ')

if z > 100:
    print('Brevet är för tjockt: ')

if x + y + z >= 900:
    print('Bredd+längd+tjocklek för ej överskrida 900mm! ') 

else:
    print(x , y , z ,'mm, Detta är ok att skicka!')











