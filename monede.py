valoarea_monedei = [1, 5, 10, 20, 50, 100, 200, 500, 1000]
def returnschimb(schimb, valoarea_monedei):
    returneaza = [0] * len(valoarea_monedei)
    for pos, moneda in enumerate(reversed(valoarea_monedei)):
        while moneda <= schimb:
            schimb = schimb - moneda
            returneaza[pos] += 1
    return(returneaza)

suma=int(input('Dati suma necesara='))
print('Valoarea monedei 1000,500,200,100,50,20,10,5,1')
print('Numarul de monede',returnschimb(suma, valoarea_monedei))
