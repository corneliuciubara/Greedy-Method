def rucsac(value, weight, capacity):

    index = list(range(len(value)))
    
    ratio = [v/w for v, w in zip(value, weight)]
    
    index.sort(key=lambda i: ratio[i], reverse=True)
 
    valoarea_maxima = 0
    fractions = [0]*len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            valoarea_maxima += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            valoarea_maxima += value[i]*capacity/weight[i]
            break
 
    return valoarea_maxima, fractions
 
 
n = int(input('Numarul de obiecte din rucsac: '))
value = input('Introduceți volumele celor {} obiecte în ordine: '
              .format(n)).split()
value = [int(v) for v in value]
weight = input('Introduceți ponderile pozitive ale celor {} obiecte în ordine: '
               .format(n)).split()
weight = [int(w) for w in weight]
capacitatea = int(input('Volumul maxim al rucsacului: '))
 
valoarea_maxima, fractions = rucsac(value, weight, capacitatea)
print(':', valoarea_maxima)
print('Fracțiile în care ar trebui luate obiecrele: ', fractions)
