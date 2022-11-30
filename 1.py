#Conditia:...Dat un număr întreg pozitiv n astfel încât n > 2. Împărțiți numerele de la 1 la n în două grupuri astfel încât diferența absolută a sumei fiecărui grup să fie minimă. Tipăriți oricare două grupuri cu dimensiunea 
#lor pe prima linie și pe linia următoare tipăriți elementele grupului respectiv.
#Diferenta dintre sume trebuie sa fie minim


#Input : 5
#Output : 2
#         5 2
#        3
#         4 3 1
#Aici suma grupului 1 este 7 și suma grupului 2 este 8.
#Diferența lor absolută este 1, ceea ce este minim.
#Putem avea mai multe răspunsuri corecte. (1, 2, 5) și (3, 4) este un alt astfel de grup.




#Informatia adaugatoare:...Putem împărți întotdeauna suma de n numere întregi în două grupuri, astfel încât diferența lor absolută a sumei lor să fie 0 sau 1. 
# Deci suma grupului diferă cel mult cu 1. Definim suma grupului1 ca jumătate din suma n elemente.
#Acum rulați o buclă de la n la 1 și introduceți i în grupul 1 dacă inserarea unui element nu depășește suma grupului 1, altfel inserați acel i în grupul 2.
import math
 
def printVector( v):
 
    
    print('Dimisiunea vectorului:',len(v))
 
    
    for i in range( 0, len(v)):
        print(v[i] , end =  "   ") #'Imprima Elimentele vectorului',
 
    print()
 
 
#Divizam in 2 grupe, astfel diferenta lor sa fie minim
def Gasim2grupe(n):
 
    
    sum = n * (n + 1) / 2
 
    
    group1Sum = sum / 2
 
    group1=[]
    group2=[]
    for i in range(n, 0, -1):
 
        # Dacă suma este mai mare sau egală
        # la 0 includ i în grupa 1
        # în caz contrar includeți în grupa 2
        if (group1Sum - i >= 0) :
            group1.append(i)
 
             # Scaderea din grupul 1
            group1Sum -= i
         
        else :
            group2.append(i)
 
    # Print Ambele grupe
    printVector(group1)
    printVector(group2)
 

n = int(input("Introduceti n="))
if n>2:
    Gasim2grupe(n)
else:
    print('Gresit')
 