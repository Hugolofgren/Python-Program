ålder = int(input('Ange din ålder: '))

standard_pris = 200 

if ålder < 0:
    print('Ålder kan inte vara mindre än 0')

if ålder < 18: 
    pris = standard_pris * 0.8
    print(pris)

if ålder >= 65:
    pris = standard_pris * 0.7 
    print(pris)

else:
    print(standard_pris)


    
