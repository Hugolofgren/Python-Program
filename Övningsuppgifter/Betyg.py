# Ta input från användaren och konvertera till ett heltal (int)
# number = int(input("Ange ett tal: "))
# While-loopen
# i = 0
# while i <= number:
   # if i % 2 == 0: # Om jämnt tal
      #  print(i)
    # i = i + 1
      
# number = int(input('Ange ett tal: '))

# for i in range(number + 1):
  #  if i % 2 == 1:
   #     print(i)


def beräkna_antal_studsar(start_höjd, tröskel=0.01):
    antal_studsar = 0
    nuvarande_höjd = start_höjd
    
    while nuvarande_höjd >= tröskel:
        nuvarande_höjd *= 0.7  # Minska höjden med 30% per studs
        antal_studsar += 1
   
    return antal_studsar

# Exempel på användning
start_höjd = float(input("Ange höjden där bollen släpps (i meter): "))
antal_studsar = beräkna_antal_studsar(start_höjd)
print(f"Bollen studsar {antal_studsar} gånger innan den når tröskelhöjden.")

