def fusion(l1,l2):
    # Initialisation des variables
    il1, il2, l3 = 0, 0, []
    # Tant que les indices sont inférieur a la taille des listes
    while il1 < len(l1) and il2 < len(l2):      
        # Si la valeur de la première liste est inférieurs alors on l'ajoute a la 3 eme liste (l3 -> résultat)
        if l1[il1] <= l2[il2]:
            l3.append(l1[il1])
            il1 += 1
        # Idem mais dans le cas inverse
        else:
            l3.append(l2[il2])
            il2 += 1
    # Ajoute le reste X2
    if l1: l3.extend(l1[il1:])
    if l2: l3.extend(l2[il2:])
    return l3
    
def tri_fusion(l):
    # Vérifie que la liste est supérieur a 1
    if len(l) < 2:
        return l
    # Découpe la liste
    cut = len(l) // 2
    # Retourne les deux liste découper de multiple fois dans fusion
    return list(fusion(tri_fusion(l[:cut]),tri_fusion(l[cut:])))



def additionMatrice(m1,m2):
    for i in range(len(m1)):
        for o in range(len(m1[0])):
            m1[i][o] = m1[i][o] + m2[i][o]
    return m1

l1 ,l2 = [[1,2],[5,7]],[[5,3],[9,1]]
l3=[1,54,2,11,85,744,15,56,4,6,8,1,444,5412,24,9]
print(tri_fusion(l3))


