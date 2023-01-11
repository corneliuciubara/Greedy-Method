# Metoda Greedy:

Costulobiectelor  = [150, 60, 80, 120, 180]
Volumulobiectelor = [120, 40, 40, 100, 150]
Volumulcontainerului = 250

def Container(Costulobiectelor, Volumulobiectelor, Volumulcontainerului):
    index = list(range(len(Costulobiectelor)))
    raport = [v / w for v, w in zip(Costulobiectelor, Volumulobiectelor)]
    index.sort(key = lambda i: raport[i], reverse=True)
    costmax = 0
    frac = [0] * len(Costulobiectelor)

    for i in index:
        if Volumulobiectelor[i] <= Volumulcontainerului:
            frac[i] = 1
            costmax += Costulobiectelor[i]
            Volumulcontainerului -= Volumulobiectelor[i]
    return costmax, frac

valoaremax, frac = Container(Costulobiectelor, Volumulobiectelor, Volumulcontainerului)

print("Soluția prin metoda Greedy:\n")

for i in range(len(frac)):
    print(f"În container încape {round(frac[i], 2)} obiect cu prețul de {Costulobiectelor[i]}\n")

print("Suma tutror obiectelor din container: ", valoaremax)

#################################################################################################################################

# Metoda Trierii

nr = [1, 2, 3, 4, 5]

def solpos(a,b,c,d,e):
    if (nr[0]*a + nr[1]*b + nr[2]*c + nr[3]*d + nr[4]*e == g) and (a+b+c+d+e==n):
        return True
    else:
        return False

def prelucraresol(a,b,c,d,e):
    summin = -1
    sum = Costulobiectelor[0]*a + Costulobiectelor[1]*b + Costulobiectelor[2]*c + Costulobiectelor[3]*d + Costulobiectelor[4]*e
    if sum >summin:
        summin = sum
    if summin==-1:
        summin=sum 
    return print(summin)

n = 5
g = 250
for a in range(0, n):
    for b in range(0, n):
        for c in range(0, n):
            for d in range(0, n):
                for e in range(0, n):
                    if solpos(a,b,c,d,e):
                        print("Solutia prin metoda Trierii", prelucraresol(a,b,c,d,e))
