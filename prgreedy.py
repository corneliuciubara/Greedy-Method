# Imaginează-ți că ești un automat de jocuri video. 
# Cineva îți oferă 100 de dolari și cumpără un joc video de 60 de dolari. 
# Nu există nicio bancnotă de 40 de dolari.
# Cum calculezi câtă schimbare trebuie returnată?

bancnote = [1, 2, 5, 10, 20, 50, 100]


def returnSchimb(schimb, bancnote):
    adainapoi = [0] * len(bancnote)
    for pos, ban in enumerate(reversed(bancnote)):
        while ban <= schimb:
            schimb = schimb - ban
            adainapoi[pos] += 1
    return(adainapoi)
            
suma = int(input("Suma introdusa in masina = "))
print("100,50,20,10,5,2,1")
print(returnSchimb(suma, bancnote))
