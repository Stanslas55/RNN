
def duree(individu):            
    indices_chemin = []
    for station in individu:  
        indices_chemin.append(I[station])  
    duree = 0    

    for i in range(19):     # 20 - 19 pour éviter le dépassement du i + 1 ! 
      
        a = indices_chemin[i]
        b = indices_chemin[i+1]
        duree += temps_stations[a][b]    
    duree += temps_stations[indices_chemin[i+1]][indices_chemin[0]]
    return duree
         
def futurePopu(pop):   
    nouvelle = [[] for i in range(100)]
   
    for i in range (0, 50 + 1): # 50 = 100 / 2.
        
        indexa = random.randint(0, 50 - 1)
        indexb = random.randint(0, 50 - 1)
        indexc = random.randint(0, 50 - 1)
        indexd = random.randint(0, 50 - 1)
        # On choisi 2 individus parmis 4
        In1 = choix(pop[indexa], pop[indexb])                     
        In2 = choix(pop[indexc], pop[indexd])                

        if(random.randint(0, 1) == 1):
            In1, In2 = croisement(In1, In2)
            
        # Comme dans la capsule, pas de mutation.              
        nouvelle[i] = In1
        # On ajoute à partir de la moitier du tableau pour ne pas chevaucher In1.
        nouvelle[i - 1 + 50] = In2 # 50 = 100 / 2 (100 = taille population)
    return nouvelle  



def choix(a, b):
    if(duree(a) > duree(b)):
        gagnant = a
        perdant = b
    else:
        gagnant = b
        perdant = a
    #choix de l'individu avec pression de selection
    if(random.randint(0, 100) <= 75):
        return perdant
    else:
        return gagnant

def croisement(In1, In2):   # Méthode de croisement indiquée par la capsule.
     
    f1 = []
    f2 = []
    # On parcours la première moitié de l'individu 1.
    for i in range(10):        
        f1.append(In1[i])  

    for i in range(10):  
        f2.append(In2[i])

    for j in range(20):
        if(In2[j] not in f1):
            f1.append(In2[j])

    for j in range(20):
        if(In1[j] not in f2):
            f2.append(In1[j])  
    return f1,f2

def plusCourt(pop, mini):
    plusPetit = mini
   
    for individu in pop:           
        
        if duree(individu) < duree(plusPetit):           
            plusPetit = individu
    return plusPetit

import random

stations =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

I = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19}

# On se situe dans l'espace, on se rend d'une station a une autre. Le chemin pour aller d'une station à une autre n'est pas le même selon pour l'aller ou le retour
# Grace aux trous noirs. La matrice n'est donc pas symétrique.
# Les temps sont exprimés en Heures.
temps_stations =  [
    [0, 6.7, 7.3, 2.5, 2.9, 1.5, 6.8, 8.4, 2.9, 4.0, 9.0, 9.4, 9.7, 1.0, 1.8, 5.9, 2.7, 8.7, 3.9, 7.1], 
    [1.8, 0, 5.1, 4.5, 5.0, 8.0, 9.2, 9.8, 5.9, 4.7, 6.3, 4.4, 9.2, 6.2, 3.6, 3.7, 4.8, 6.7, 3.6, 8.3], 
    [2.2, 7.0, 0, 9.4, 5.7, 9.4, 5.9, 6.4, 2.8, 4.1, 9.0, 8.9, 8.2, 8.4, 6.8, 2.9, 1.0, 7.7, 5.6, 6.6], 
    [8.9, 5.2, 1.9, 0, 8.6, 6.8, 1.2, 2.3, 9.2, 7.2, 8.9, 4.5, 9.2, 8.1, 6.2, 9.4, 7.1, 6.7, 8.0, 2.3], 
    [7.0, 8.6, 9.0, 9.0, 0, 5.5, 9.1, 2.9, 8.4, 7.0, 2.1, 6.6, 9.5, 1.0, 6.8, 9.3, 3.5, 9.3, 3.0, 1.8], 
    [4.2, 2.3, 8.2, 2.0, 2.5, 0, 7.5, 7.8, 3.6, 3.9, 1.5, 2.5, 7.7, 4.7, 9.9, 5.0, 3.8, 4.9, 2.9, 1.7], 
    [3.0, 6.0, 9.5, 6.4, 3.0, 8.9, 0, 3.4, 8.3, 3.6, 7.2, 7.5, 1.3, 6.9, 2.6, 8.8, 9.9, 1.8, 3.0, 4.0], 
    [3.4, 7.3, 2.2, 3.7, 1.5, 5.5, 6.1, 0, 1.5, 8.4, 6.8, 8.6, 9.7, 1.1, 4.8, 9.9, 2.6, 7.3, 6.5, 7.4], 
    [6.0, 2.0, 8.0, 9.0, 7.7, 3.0, 3.5, 3.3, 0, 8.0, 8.8, 9.4, 9.8, 5.2, 2.8, 3.6, 8.3, 1.9, 4.8, 7.0], 
    [3.4, 2.2, 9.3, 9.9, 7.1, 3.3, 5.5, 4.6, 7.0, 0, 6.3, 9.4, 8.2, 1.0, 2.2, 3.3, 2.4, 5.5, 5.7, 9.3], 
    [6.8, 5.5, 5.3, 6.6, 7.9, 7.8, 3.1, 7.4, 9.8, 3.8, 0, 6.5, 9.6, 7.7, 9.3, 7.3, 5.0, 1.5, 1.6, 9.9], 
    [5.2, 6.2, 1.4, 8.3, 4.1, 7.9, 9.1, 4.4, 5.1, 1.3, 9.1, 0, 9.1, 1.9, 3.6, 1.9, 2.8, 6.8, 3.4, 7.0], 
    [7.0, 7.0, 5.8, 8.6, 6.9, 8.8, 6.0, 5.9, 8.6, 6.5, 6.5, 7.5, 0, 6.7, 6.4, 8.3, 1.8, 8.9, 5.3, 8.1], 
    [3.0, 8.0, 1.0, 5.5, 1.8, 9.5, 7.4, 2.8, 3.5, 9.4, 6.7, 3.6, 8.2, 0, 8.5, 6.5, 2.7, 9.2, 3.4, 7.9], 
    [2.7, 5.3, 7.7, 2.5, 4.8, 3.8, 9.2, 5.1, 8.3, 7.6, 6.2, 5.7, 2.3, 9.8, 0, 4.9, 7.3, 7.6, 2.3, 9.3], 
    [5.7, 7.1, 2.3, 9.2, 3.2, 8.5, 6.7, 1.6, 2.2, 1.6, 7.6, 5.2, 5.6, 8.2, 9.9, 0, 4.9, 7.9, 3.9, 4.5], 
    [6.0, 6.0, 5.0, 4.4, 4.7, 6.7, 7.8, 4.5, 2.2, 4.0, 4.0, 6.1, 3.2, 6.5, 7.7, 8.0, 0, 6.4, 4.2, 7.4], 
    [7.3, 7.7, 2.7, 9.7, 6.7, 2.9, 8.8, 8.5, 6.2, 2.3, 6.9, 8.6, 9.5, 2.6, 4.0, 1.2, 9.5, 0, 3.5, 3.3], 
    [8.3, 5.2, 6.8, 6.4, 9.1, 1.1, 5.0, 7.5, 5.4, 3.5, 2.6, 1.8, 7.2, 8.5, 2.7, 3.1, 4.8, 4.7, 0, 8.6], 
    [6.2, 1.0, 1.4, 1.7, 5.2, 1.6, 6.7, 7.0, 2.2, 4.3, 5.6, 6.1, 1.9, 2.6, 9.6, 7.0, 5.2, 6.7, 3.5, 0]]

pop = []
# On a 100 individus.
for i in range(100):
    In = []
    for j in range(20):
        C = random.choice(stations)        
        while(C in In):
            C = random.choice(stations)            
        In.append(C)  
    pop.append(In)          

mini = plusCourt(pop, pop[0])
print("La solution de base aléatoire est: ", duree(mini), "pour ", mini)
# On fait 20 generations.
for i in range(20):
     pop = futurePopu(pop)
     mini = plusCourt(pop, mini)

itineraire = ""
for i in range(20):
    itineraire += mini[i]

itineraire += mini[0]
print("duree:", duree(mini), " Heures pour le chemin ", itineraire)


