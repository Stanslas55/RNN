import random

### Génere un individu composé de 'taille' chromosomes.
def generer_individu(taille):
    chemin = []

    for i in range(taille):
        ville = random.choice(villes)        
        while(ville in chemin): # Pour ne pas avoir 2 fois le même chromosome.
            ville = random.choice(villes)            
        chemin.append(ville)    
    return chemin

### Génere une population de 'taille' individu ayant 'nb_chromosomes' chromosomes.
def generer_population(taille, nb_chromosomes):
    pop = []

    for i in range(taille):
        pop.append(generer_individu(nb_chromosomes))        
    return pop

### Renvoie la liste des indices des chromosomes.
def indices_chromosomes(individu):
    indices_chemin = []

    for ville in individu:  
        indices_chemin.append(indice_villes[ville])  
    return indices_chemin

### Calcule la fitness d'un individu.
def fitness(individu):
    fitness = 0 
    indices_chemin = indices_chromosomes(individu)      
    
    for i in range(nb_villes - 1):          
        fitness += d_villes[indices_chemin[i]][indices_chemin[i+1]]    
    fitness += d_villes[indices_chemin[i+1]][indices_chemin[0]]
    return fitness
   
### Renvoie le meilleur individu de toutes les générations.         
def meilleur_individu(popu, best):
    actuel = best
   
    for individu in popu:                      
        if(fitness(individu) < fitness(actuel)):           
            actuel = individu
    return actuel

### Renvoie le croisement entre deux individus.
def croisement(couple):      
    taille_f1 = int(nb_villes / 2)       
    fils1 = []
    fils2 = []

    for i in range(taille_f1):        
        fils1.append(couple[0][i])  
        fils2.append(couple[1][i])

    for j in range(nb_villes):
        if(couple[1][j] not in fils1):
            fils1.append(couple[1][j])
        if(couple[0][j] not in fils2):
            fils2.append(couple[0][j])            
       
    enfants = [fils1, fils2]      
    return enfants

### Renvoie un individu parmis les deux
def compareRandomIndividu(I1, I2):

    if(fitness(I1) > fitness(I2)):
        MAX = I1
        MIN = I2
    else:
        MAX = I2
        MIN = I1      

    return MIN if (random.randint(0, 100) <= pression_evolutive) else MAX

### Selection par tournois.
def getNewPop(pop):    
    newPop = [[] for _ in range(taille_population)]
    
    for i in range (0,int(taille_population / 2)): # Génère les individus 2 par 2 donc on parcours seulement la moitier de la population.        
        A = pop[random.randint(0, taille_population - 1)] # Confronte 2 individus pour en garder 1.
        B = pop[random.randint(0, taille_population - 1)]
        while (A is B):
            B = pop[random.randint(0, taille_population - 1)]
        I1 = compareRandomIndividu(A, B)        
        
        A = pop[random.randint(0, taille_population - 1)] # 2eme fois.
        B = pop[random.randint(0, taille_population - 1)]
        while (A is B):
            B = pop[random.randint(0, taille_population - 1)]
        I2 = compareRandomIndividu(A, B)
        
        couple = [I1,I2]

        if(random.randint(0, 100) <= chances_croisement):
            couple = croisement(couple)
            
        # Je choisi de ne pas faire de mutations.       
        
        newPop[i] = couple[0]
        newPop[taille_population - 1 - i] = couple[1] # Insertion en miroir afin d'augmenter encore plus la diversité.
    return newPop           

villes = ["Limoges", "Lyon", "Marseille", "Monaco", "Nantes", "Nice", "Paris", "Reims", "Rennes", "Rouen", "Strasbourg", "Toulouse"]
indice_villes = {'Limoges': 0, 'Lyon': 1, 'Marseille': 2, 'Monaco': 3, 'Nantes': 4, 'Nice': 5, 'Paris': 6, 'Reims': 7, 'Rennes': 8, 'Rouen': 9, 'Strasbourg': 10, 'Toulouse': 11}
d_villes = [
 [0, 366, 609, 797, 300, 776, 369, 514, 372, 444, 690, 324], 
 [366, 0, 326, 425, 598, 404, 462, 473, 640, 591, 434, 506], 
 [609, 326, 0, 206, 909, 185, 772, 799, 958, 898, 769, 407], 
 [797, 425, 206, 0, 1069, 21, 915, 873, 1065, 1015, 824, 586], 
 [300, 598, 909, 1069, 0, 1048, 379, 549, 106, 357, 795, 540], 
 [776, 404, 185, 21, 1048, 0, 894, 852, 1044, 995, 803, 565], 
 [369, 462, 772, 915, 379, 894, 0, 147, 331, 117, 442, 678], 
 [514, 473, 799, 873, 549, 852, 147, 0, 498, 233, 330, 824], 
 [372, 640, 958, 1065, 106, 1044, 331, 498, 0, 290, 771, 652], 
 [444, 591, 898, 1015, 357, 995, 117, 233, 290, 0, 566, 768], 
 [690, 434, 769, 824, 795, 803, 442, 330, 771, 566, 0, 940], 
 [324, 506, 407, 586, 540, 565, 678, 824, 652, 768, 940, 0]]

taille_population = 100 # Donné dans la capsule
nb_villes = len(villes)

chances_croisement = 65  # Chance de croisement en %.
pression_evolutive = 60 # Pression de selection.
nombre_generations = 10 # Nombre constant de génération, donné dans la capsule.

### Main
population = generer_population(taille_population, nb_villes)

meilleur = population[0]
meilleur = meilleur_individu(population, meilleur)

print("fitness initiale:", fitness(meilleur), ":", meilleur) # Fitness du premier individu.

generation_count = 1
while(generation_count <= nombre_generations):
    population = getNewPop(population)
    meilleur = meilleur_individu(population, meilleur)
    generation_count += 1 

print("fitness finale:", fitness(meilleur), ":",meilleur)

print("Un bon itinéraire pour minimiser la distance parcourue serait : ", end= ' ')
for i in range(nb_villes):
    print(meilleur[i], '->', end=' ')
print(meilleur[0])

