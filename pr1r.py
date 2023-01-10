# Metoda Greedy

def Container(W, wt, val, n):

    if n == 0 or W == 0:
        return 0

    if (wt[n-1] > W):
        return Container(W, wt, val, n-1)

    else:
        return max(
            val[n-1] + Container(
                W-wt[n-1], wt, val, n-1),
            Container(W, wt, val, n-1))

pret  = [150, 60, 80, 120, 180] 
volum = [120, 40, 40, 100, 150] 
Volumulcontainerului = 250
n = len(pret)
print("Solutia prin metoda Greedy: ", Container(Volumulcontainerului, volum, pret, n))

############################################################################

# Metoda Trierii

nr = [1, 2, 3, 4, 5]

def solpos(a,b,c,d,e):
    if (nr[0]*a + nr[1]*b + nr[2]*c + nr[3]*d + nr[4]*e == g) and (a+b+c+d+e==n):
        return True
    else:
        return False

def prelucraresol(a,b,c,d,e):
    summin = -1
    sum = pret[0]*a+pret[1]*b+pret[2]*c+pret[3]*d+pret[4]*e
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