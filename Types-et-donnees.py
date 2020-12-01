# Algo Bissextile

def algoBissextile():
    # Demande a l'utilisateur de rentrer une année
    annee = (int(input("Rentrez une année pour savoir si elle est Bissextile : ")))
    # Vérifie la première condition : divisible par 4 mais pas par 100
    if (annee%4 == 0) and  (annee%100 != 0):
        print(annee,"est Bissextile")
    # Sinon vérifie la deuxième condition : divisible par 400
    elif (annee%400 == 0) :
        print(annee,"est Bissextile")
    # Sinon renvoi un résultat négatif
    else :
        print(annee,"n'est pas Bissextile")

def cardLuhn():
    # Affectation variable
    cardverif, pair, i = "", True, -2

    # Demande a l'utilisateur le numéro a trouver // vérifier
    print("Si vous cherchez le dernier numéro remplacer le dernier par un 0")
    card = (input("Enter votre numéro de carte : "))

    # Boucle qui définit le nombre de chiffre vérifié (16 actuellement non modifiable)
    while i > -17 :
        # Affecte cardtemp de la valeur en integer du numéro de la carte selon l'indice a chaque itération
        cardtemp = int(card[i])
        # Vérifie si le rang est pair ou impair
        if pair == True :
            # Si pair multiplie par 2
            cardtemp *= 2
            # Si le résultat supérieur ou égal a 10 le remplace par la sommes de ces chiffres
            if cardtemp >= 10 :
                cardtemp = sum([int(c) for c in str(cardtemp)])
            # Change la valeur de pair pour bien alterner
            pair = False
        # Si impair change la valeur de pair pour bien alterner
        else : pair = True
        # Ajoute le chiffre dans la nouvelle chaine en tant que string
        cardverif = str(cardtemp) + cardverif
        i-=1
    # Ajoute le dernier chiffre
    cardverif += card[-1]
    # Fait la somme
    cardsum = sum([int(c) for c in str(cardverif)])
    # Applique un modulo 10
    cardsum = cardsum%10

    # Dans le cas d'une recherche du dernier chiffre envoi le dernier ainsi qu'une séquence correcte
    if card[-1] == "0" and cardsum != 0 :
        print("Le dernier numéro de la carte est",cardsum)
        print("Donc le numéro de carte correcte est :",card[0:4],"",card[4:8],"",card[8:12],"",card[12:15]+str(cardsum))
    # Dans le cas d'une vérification envoi un résultat positif
    elif cardsum == 0 or cardsum == 10:
        print("Votre numéro de carte est correcte")
    # Idem mais en négatif
    else :
        print("Votre numéro de carte est incorrecte")




