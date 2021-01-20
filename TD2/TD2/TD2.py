
def print_reseau(reseau):  
    if not isinstance(reseau,tuple):
         raise TypeError("Entrez un reseau valide !")            
    print("Votre réseau : (a,b,c,d) = ({},{},{},{})".format(reseau[0], reseau[1], reseau[2], reseau[3]))

# Activation synchrone
def synchrone(initial):
    # Ici on test si il y a des erreurs
    if not isinstance(initial,tuple) or len(initial) != 4:
         raise TypeError("Entrez un reseau valide !")  
    print_reseau(initial)
    suivant = []
    nouvelle = 0
    for cellule_suivante in range(4):
        nouvelle = 0
        #print("On s'occupe de la cellule {}".format(affichage[cellule_suivante]))
        for cellule_actuelle in range(len(initial)):             
            if cellule_suivante != cellule_actuelle:  
                #print("\t{} -> {}, on ajoute {} * {}".format(affichage[cellule_actuelle], affichage[cellule_suivante], initial[cellule_actuelle], poids[cellule_suivante][cellule_actuelle] ))
                nouvelle += initial[cellule_actuelle] * poids[cellule_suivante][cellule_actuelle]
        suivant.append(nouvelle)
    suivant = [1 if i > 0 else 0 for i in suivant]
   
    return tuple(suivant)

# Dectecte un état stable (cycle de taille 1) ou un cycle de taille 2, pour une configuration donnée en synchrone
def test_synchrone(reseau):
    reseau_actuel = reseau
    reseau_suivant = synchrone(reseau_actuel)

    sauvegarde = [reseau_suivant, reseau_actuel, (0)]

    while reseau_actuel != reseau_suivant:   

        sauvegarde[2] = reseau_actuel
        reseau_actuel = reseau_suivant

        sauvegarde[1] = reseau_actuel
        reseau_suivant = synchrone(reseau_actuel)  
        sauvegarde[0] = reseau_suivant

        #print(sauvegarde)
        if(sauvegarde[0] == sauvegarde[2]): 
            print("On a atteint un cycle de 2 : {} -> {}".format(sauvegarde[0], sauvegarde[1]))
            break

# Activation synchrone
def asynchrone(initial):
    if not isinstance(initial,tuple) or len(initial) != 4:
         raise TypeError("Entrez un reseau valide !")  
    print_reseau(initial) 
    initial = list(initial)
    nouvelle = 0
    for cellule_suivante in range(4):
        nouvelle = 0
        #print("On s'occupe de la cellule {}".format(affichage[cellule_suivante]))
        #print("initial vaut {}".format(initial))
        for cellule_actuelle in range(len(initial)): 
            
            if cellule_suivante != cellule_actuelle:  
                #print("\t{} -> {}, on ajoute {} * {}".format(affichage[cellule_actuelle], affichage[cellule_suivante], initial[cellule_actuelle], poids[cellule_suivante][cellule_actuelle] ))
                nouvelle += initial[cellule_actuelle] * poids[cellule_suivante][cellule_actuelle]
        initial[cellule_suivante] = 1 if nouvelle > 0 else 0
        
    #initial = [1 if i > 0 else 0 for i in initial]
    return tuple(initial)

# Dectecte un état stable (cycle de taille 1) ou un cycle de taille 2, pour une configuration donnée en asynchrone
def test_asynchrone(reseau):
    reseau_actuel = reseau
    reseau_suivant = asynchrone(reseau_actuel)

    sauvegarde = [reseau_suivant, reseau_actuel, (0)]


    while reseau_actuel != reseau_suivant:   

        sauvegarde[2] = reseau_actuel
        reseau_actuel = reseau_suivant

        sauvegarde[1] = reseau_actuel
        reseau_suivant = asynchrone(reseau_actuel)  
        sauvegarde[0] = reseau_suivant

        #print(sauvegarde)
        if(sauvegarde[0] == sauvegarde[2]): 
            print("On a atteint un cycle de 2 : {} -> {}".format(sauvegarde[0], sauvegarde[1]))
            break

def a_la_main():
    # Ici on récupère les entrées du réseau
    a = int(input("a = ? "))
    b = int(input("b = ? "))
    c = int(input("c = ? "))
    d = int(input("d = ? "))

    reseau = (a,b,c,d)
    print_reseau(reseau)
    
    print("En synchrone")
    test_synchrone(reseau)
    
    print("En asynchrone")
    test_asynchrone(reseau)

def toutes_les_combinaisons_synchrones():
    
    print("Les combinaisons en synchrone")
    for combi in combinaisons:
        test_synchrone(combi)
        print("\n")
def toutes_les_combinaisons_asynchrones():   
    print("Les combinaisons en asynchrone")
    for combi in combinaisons:
        test_asynchrone(combi)
        print("\n")


# Ici on créer la matrice de poids
affichage = {0:"a", 1:"b", 2:"c", 3:"d"}
poids = [[0,-1,1,1],
         [-1,0,1,-1],
         [1,1,0,1],
         [1,-1,1,0]]

'''poids = [[0, 1,1,1],
         [-1,0,1,-1],
         [-1,1,0,1],
         [-1,1,1,0]]'''
combinaisons = [(0,0,0,0), (0,0,0,1), 
                    (0,0,1,0), (0,0,1,1), 
                    (0,1,0,0), (0,1,0,1), (0,1,1,0), (0,1,1,1),
                   (1,0,0,0), (1,0,0,1), (1,0,1,0), (1,0,1,1), (1,1,0,0), (1,1,0,1), (1,1,1,0), (1,1,1,1),]


a_la_main()

toutes_les_combinaisons_synchrones()

toutes_les_combinaisons_asynchrones()