
def aff_res(system):           
    print("(" , system[0], ",", system[1],",", system[2],",", system[3],")")

# Activation synchrone
def synchrone(debut):
   
    aff_res(debut)
    suivant = []
    nouvelle_valeur = 0
    for prochaine in range(4):
        nouvelle_valeur = 0
       
        for actuelle in range(len(debut)):             
            if prochaine != actuelle:  
               
                nouvelle_valeur += debut[actuelle] * poids[prochaine][actuelle]
        suivant.append(nouvelle_valeur)   
    indice = 0
    for i in suivant:
        if(i > 0):
            suivant[indice] = 1
        else:
            suivant[indice] = 0
        indice += 1
    suivant = (suivant)
    return suivant

# Dectecte un état stable (cycle de taille 1) ou un cycle de taille 2, pour une configuration donnée en synchrone
def test_synchrone(system):
    system_actuel = system
    system_suivant = synchrone(system_actuel)

    save = [system_suivant, system_actuel, (0)]

    while system_actuel != system_suivant:   

        save[2] = system_actuel
        system_actuel = system_suivant

        save[1] = system_actuel
        system_suivant = synchrone(system_actuel)  
        save[0] = system_suivant

        #print(save)
        if(save[0] == save[2]): 
            print("cycle de 2 : ", save[0], "->", save[1])
            break

# Activation synchrone
def asynchrone(debut):   
    aff_res(debut) 
    debut = list(debut)
    nouvelle_valeur = 0
    for prochaine in range(4):
        nouvelle_valeur = 0
        
        for actuelle in range(len(debut)): 
            
            if prochaine != actuelle:  
               
                nouvelle_valeur += debut[actuelle] * poids[prochaine][actuelle]
        debut[prochaine] = 1 if nouvelle_valeur > 0 else 0
        
   
    return tuple(debut)

# Dectecte un état stable (cycle de taille 1) ou un cycle de taille 2, pour une configuration donnée en asynchrone
def test_asynchrone(system):
    system_actuel = system
    system_suivant = asynchrone(system_actuel)

    save = [system_suivant, system_actuel, (0)]


    while system_actuel != system_suivant:   

        save[2] = system_actuel
        system_actuel = system_suivant

        save[1] = system_actuel
        system_suivant = asynchrone(system_actuel)  
        save[0] = system_suivant

        #print(save)
        if(save[0] == save[2]): 
            print("cycle de 2 : ", save[0], "->", save[1])
            break

def utilisateur():
    # Ici on récupère les entrées du réseau
    a = int(input("a = ? "))
    b = int(input("b = ? "))
    c = int(input("c = ? "))
    d = int(input("d = ? "))

    system = (a,b,c,d)
    aff_res(system)
    
    print("synch")
    test_synchrone(system)
    
    print("asynch")
    test_asynchrone(system)

def combi_synch():
    
    print("Les combinaisons en synchrone")
    for combi in combinaisons:
        test_synchrone(combi)
        print("\n")

def combi_asynch():   
    print("Les combinaisons en asynchrone")
    for combi in combinaisons:
        test_asynchrone(combi)
        print("\n")


# Ici on va créer la matrice de poids

poids = [[0,-1,1,1], [-1,0,1,-1], [1,1,0,1], [1,-1,1,0]]

'''poids = [[0, 1,1,1],
         [-1,0,1,-1],
         [-1,1,0,1],
         [-1,1,1,0]]'''
combinaisons = [(0,0,0,0), (0,0,0,1), (0,0,1,0), (0,0,1,1), (0,1,0,0), (0,1,0,1), (0,1,1,0), (0,1,1,1), (1,0,0,0), (1,0,0,1), (1,0,1,0), (1,0,1,1), (1,1,0,0), (1,1,0,1), (1,1,1,0), (1,1,1,1),]


utilisateur()

combi_synch()

combi_asynch()
