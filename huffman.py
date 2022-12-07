"""
Codurile Huffman reprezintă o tehnică foarte eficientă de compactare a datelor,
spaţiul economisit fiind cuprins adesea între 20% şi 90%.
Algoritmul greedy pentru realizarea acestei codificări înregistrează 
frecvenţele de apariţie ale fiecărui simbol dintr-un fişier,
după care utilizează o modalitate optimă pentru reprezentarea fiecărui simbol sub forma unui şir binar.

Astfel, se dă o mulţime A = {a1,a2,...,an} formată din n simboluri (un text din fișierul huffman.in).
Fie B un şir de lungime n de coduri binare cu proprietatea că niciun cod bi nu este prefixul unui alt cod bj (i ≠ j).
Să se scrie în fișierul huffman.out textul inițial, codurile corespunzătoare fiecărui simbol,
iar mai jos șirul de caractere codificat, utilizând aceste coduri.
"""
import heapq
fin,fout,rez,tree,blocuri=list(open("huffman.in","r").read()),open("huffman.out","w"),[],[],[]
fout.write("Textul initial:\n\n")
fout.write(open("huffman.in","r").read())
fout.write("\n\nCodurile Huffman:\n\n")
txt=[(i,fin.count(i)) for i in set(fin)]
class bloc:
    def __init__(self, frecv, simbol, stang=None, drept=None):
        self.frecv = frecv
        self.simbol = simbol
        self.stang = stang
        self.drept = drept
        self.huffman = ''
    def __lt__(self, urmator):return self.frecv < urmator.frecv
def afisare(bloc, val=''):
    val_noua = val + str(bloc.huffman)
    tree.append([bloc.simbol, bloc.frecv])
    if(bloc.stang):
        afisare(bloc.stang, val_noua)
    if(bloc.drept):
        afisare(bloc.drept, val_noua)
    if(not bloc.stang and not bloc.drept):
        rez.append([bloc.simbol,val_noua])
        fout.write(str(repr(bloc.simbol).strip("'")+"->"+val_noua+"\n"))
for x in range(len(txt)):heapq.heappush(blocuri, bloc(txt[x][1], txt[x][0]))
while len(blocuri) > 1:
    stang = heapq.heappop(blocuri)
    drept = heapq.heappop(blocuri)
    stang.huffman = 0
    drept.huffman = 1
    bloc_nou = bloc(stang.frecv+drept.frecv, stang.simbol+drept.simbol, stang, drept)
    heapq.heappush(blocuri, bloc_nou)
afisare(blocuri[0])
fout.write("\nTextul codificat:\n\n")
for i in fin:
    for j in rez:
        if j[0]==i:
            if j[0]=="\n":fout.write(j[1]+"\n")
            elif j[0]=="\t":fout.write("\t"+j[1]+" ")
            else:fout.write(j[1]+" ")