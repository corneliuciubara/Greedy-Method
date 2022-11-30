
#Dat un număr întreg pozitiv n astfel încât n > 2. Împărțiți numerele de la 1 la n în două grupuri astfel încât diferența absolută a sumei fiecărui grup să fie minimă. Tipăriți oricare două grupuri cu dimensiunea 
#lor pe prima linie și pe linia următoare tipăriți elementele grupului respectiv.
#Diferenta dintre sume trebuie sa fie minim
import math
 
def printVector( v):
 
    print('Dimisiunea vectorului:', len(v))
 
    for i in range( 0, len(v)):
        print ('Imprima Elimentele vectorului', v[i] , end =  " ") 
 
    print()
 
 
#Divizam in 2 grupe, astfel diferenta lor sa fie minim
def findTwoGroup(n):
 

    sum = n * (n + 1) / 2
 

    grop1Sum = sum / 2
 
    grop1=[]
    grop2=[]
    for i in range(n, 0, -1):
 
        # Dacă suma este mai mare sau egală
        # la 0 includ i în grupa 1
        # în caz contrar includeți în grupa 2
        if (grop1Sum - i >= 0) :
            grop1.append(i)
 
            # Scaderea din grupul 1
            grop1Sum -= i
         
        else :
            grop2.append(i)
 

    printVector('1 grup:', grop1)
    printVector('2 grup:',grop2)
 

n = int(input("Introduceti n="))
findTwoGroup(n)
 
