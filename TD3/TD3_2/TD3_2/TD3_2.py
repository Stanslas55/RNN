def liste_vers_matrice(liste):
    matrice_a_renvoyer = []        
    for i in range(5):
        part = []
        for j in range(5):
            part.append(liste[5*i+j])
        matrice_a_renvoyer.append(part)    
    return matrice_a_renvoyer
        
def matrice_vers_liste(matrice):
    liste_a_renvoyer = []
    for i in range(5):
        for j in range(5):
            liste_a_renvoyer.append(matrice[i][j])
            
    return liste_a_renvoyer




alphabet = \
[ [ [False, True,  True,  True,  False],  # { A }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  True],
     [True,  False, False, False, True],
     [True,  False, False, False, True] ],
   [ [True,  True,  True,  True,  False],  # { B }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False],
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False] ],
   [ [False, True,  True,  True,  True],   # { C }
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [False, True,  True,  True,  True] ],
   [ [True,  True,  True,  True,  False],  # { D }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False] ],
   [ [True,  True,  True,  True,  True],   # { E }
     [True,  False, False, False, False],
     [True,  True,  True,  False, False],
     [True,  False, False, False, False],
     [True,  True,  True,  True,  True] ],
   [ [True,  True,  True,  True,  True],   # { F }
     [True,  False, False, False, False],
     [True,  True,  True,  False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, False] ],
   [ [True,  True,  True,  True,  True],   # { G }
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, True],
     [True,  True,  True,  True,  True] ],
   [ [True,  False, False, False, True],   # { H }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  True],
     [True,  False, False, False, True],
     [True,  False, False, False, True] ],
   [ [False, False, True,  False, False],  # { I }
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False] ],
   [ [False, False, True,  True,  True],   # { J }
     [False, False, False, True,  False],
     [False, False, False, True,  False],
     [False, False, False, True,  False],
     [True,  True,  True,  True,  False] ],
   [ [True,  False, False, False, True],   # { K }
     [True,  False, False, True,  False],
     [True,  True,  True,  False, False],
     [True,  False, False, True,  False],
     [True,  False, False, False, True] ],
   [ [True,  False, False, False, False],  # { L }
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  False, False, False, False],
     [True,  True,  True,  True,  True] ],
   [ [True,  True,  False, True,  True],   # { N }
     [True,  False, True,  False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True] ],
   [ [True,  False, False, False, True],   # { M }
     [True,  True,  False, False, True],
     [True,  False, True,  False, True],
     [True,  False, False, True,  True],
     [True,  False, False, False, True] ],
   [ [False, True,  True,  True,  False],  # { O }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [False, True,  True,  True,  False] ],
   [ [True,  True,  True,  True,  False],  # { P }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False],
     [True,  False, False, False, False],
     [True,  False, False, False, False] ],
   [ [True,  True,  True,  True,  True],   # { Q }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, True,  True],
     [True,  True,  True,  True,  True] ],
   [ [True,  True,  True,  True,  False],  # { N_cell }
     [True,  False, False, False, True],
     [True,  True,  True,  True,  False],
     [True,  False, False, True,  False],
     [True,  False, False, False, True] ],
   [ [False, True,  True,  True,  True],   # { S }
     [True,  False, False, False, False],
     [False, True,  True,  True,  False],
     [False, False, False, False, True],
     [True,  True,  True,  True,  False] ],
   [ [True,  True,  True,  True,  True],   # { T }
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False] ],
   [ [True,  False, False, False, True],   # { U }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [False, True,  True,  True,  False] ],
   [ [True,  False, False, False, True],   # { V }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [False, True,  False, True,  False],
     [False, False, True,  False, False] ],
   [ [True,  False, False, False, True],   # { W }
     [True,  False, False, False, True],
     [True,  False, False, False, True],
     [True,  False, True,  False, True],
     [False, True,  False, True,  False] ],
   [ [True,  False, False, False, True],   # { X }
     [False, True,  False, True,  False],
     [False, False, True,  False, False],
     [False, True,  False, True,  False],
     [True,  False, False, False, True] ],
   [ [True,  False, False, False, True],   # { Y }
     [False, True,  False, True,  False],
     [False, False, True,  False, False],
     [False, False, True,  False, False],
     [False, False, True,  False, False] ],
   [ [True,  True,  True,  True,  True],   # { Z }
     [False, False, False, True,  False],
     [False, False, True,  False, False],
     [False, True,  False, False, False],
     [True,  True,  True,  True,  True] ]]

exemple_a_reconnaitre = [ [True,  False, True,  False, True],
                          [True,  True,  False, False, True],
                          [False, False, True,  False, True],
                          [True,  False, False, True,  True],
                          [True, False, False, False, True] ]

def affiche(dessin):
    for ligne in range(5):
        for colonne in range(5):
            if(dessin[ligne][colonne]):
                print('#', end='')
            else:
                print(' ', end='')
        print("\n", end='')

        
def entrainement(etat, dessin, poids, seuils, eps):    
    
    for cell in range(N_cell):  
        somme = 0
        combien = 0
        for cell_voisine in range(N_cell):
            if(cell != cell_voisine):
                if(etat[cell_voisine]):
                    somme = somme + poids[cell][cell_voisine]
                    combien = combien + 1          
               
        suivante = True if (somme - seuils[cell] ) > 0 else False   
        
        if(suivante != dessin[cell]):               
                   
            triangle = (dessin[cell] - suivante + eps) / combien
          
            for cell_voisine in range(N_cell):
                 if(cell != cell_voisine):
                    if(etat[cell_voisine]):                       # Je met à jour les poids !
                        poids[cell][cell_voisine] += triangle
                        poids[cell_voisine][cell] += triangle
            
            seuils[cell] -= triangle                      
    return poids, seuils


def forward(etat, poids, seuils):
    
    for cell in range(N_cell):  
        somme = 0       
        for cell_voisine in range(N_cell):
            if(cell != cell_voisine):                   
                somme += poids[cell][cell_voisine] * etat[cell_voisine]             
                              
        etat[cell] = True if (somme - seuils[cell]) > 0 else False 
    return etat


N_cell = 5*5

# états des cellules du réseau (booléens)
etats = [ False for _ in range(N_cell) ]

# seuils des cellules du réseau (réels)
seuils = [ 0.0 for _ in range(N_cell) ]

# poids des connexions du réseau (réels)
poids = [ [ 0.5 for _ in range(N_cell)] for _ in range(N_cell) ]
 # La marge de sécurité 
epsilon = 0.3  


for lettre in range(0, 2):  
    for i in range(100): 
        poids, seuils = entrainement(matrice_vers_liste(alphabet[lettre]), matrice_vers_liste(alphabet[lettre]), poids, seuils, epsilon)   
 

for letter in range(0, 2):                                
    dessin = alphabet[letter]   
    print("On donne :\n")
    affiche(dessin)    
    etat_apres = matrice_vers_liste(dessin)                                    

    for i in range(100):
        etat_apres = forward(etat_apres, poids, seuils)
    print("Le programme renvoi :\n")
    affiche(liste_vers_matrice(etat_apres))
    print("\n")


# Dans cette partie on se concentre sur la reconnaissance de la lettre bruitée.
# Je change la valeur des poids, pour voir ce que ça fait

etats = [ False for _ in range(N_cell) ]
seuils = [ 0.1 for _ in range(N_cell) ]
poids = [ [ 0.7 for _ in range(N_cell)] for _ in range(N_cell) ]
epsilon = 0.3


for lettre in range(12, 14):  
    for i in range(100): 
        poids, seuils = entrainement(matrice_vers_liste(alphabet[lettre]), matrice_vers_liste(alphabet[lettre]), poids, seuils, epsilon)  

dessin = exemple_a_reconnaitre
print("On donne :\n")
affiche(dessin)
etats = matrice_vers_liste(dessin)
print("\n")
for i in range(100):
    etats = forward(etats, poids, seuils)
print("Le programme renvoi :\n")
affiche(liste_vers_matrice(etats))


