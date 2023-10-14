##AZOUAGH Safiya RACHID.K Assmâe
##############
# SAE S01.01 #
##############

def liste_amis(amis, prenom):
    """
        Retourne la liste des amis de prenom en fonction du tableau amis.
    """
    prenoms_amis = []
    i = 0
    while i < len(amis)//2:
        if amis[2 * i] == prenom:
            prenoms_amis.append(amis[2*i+1])
        elif amis[2*i+1] == prenom:
            prenoms_amis.append(amis[2*i])
        i += 1
    return prenoms_amis

def nb_amis(amis, prenom):
    """ Retourne le nombre d'amis de prenom en fonction du tableau amis. """
    return len(liste_amis(amis, prenom))


def personnes_reseau(amis):
    """ Retourne un tableau contenant la liste des personnes du réseau."""
    people = []
    i = 0
    while i < len(amis):
        if amis[i] not in people:
            people.append(amis[i])
        i += 1
    return people

def taille_reseau(amis):
    """ Retourne le nombre de personnes du réseau."""
    return len(personnes_reseau(amis))

def lecture_reseau(path):
    """ Retourne le tableau d'amis en fonction des informations contenues dans le fichier path."""
    f = open(path, "r")
    l = f.readlines()
    f.close()
    amis = []
    i = 0
    while i < len(l):
        fr = l[i].split(";")
        amis.append(fr[0].strip())
        amis.append(fr[1].strip())
        i += 1
    return amis

def dico_reseau(amis):
    """ Retourne le dictionnaire correspondant au réseau."""
    dico = {}
    people = personnes_reseau(amis)
    i = 0
    while i < len(people):
        dico[people[i]] = liste_amis(amis, people[i])
        i += 1
    return dico

def nb_amis_plus_pop (dico_reseau):
    """ Retourne le nombre d'amis des personnes ayant le plus d'amis."""
    personnes = list(dico_reseau)
    maxi = len(dico_reseau[personnes[0]])
    i = 1
    while i < len(personnes):
        if maxi < len(dico_reseau[personnes[i]]):
            maxi = len(dico_reseau[personnes[i]])
        i += 1
    return maxi


def les_plus_pop (dico_reseau):
    """ Retourne les personnes les plus populaires, c'est-à-dire ayant le plus d'amis."""
    max_amis = nb_amis_plus_pop(dico_reseau)
    most_pop = []
    personnes = list(dico_reseau)
    i = 1
    while i < len(personnes):
        if len(dico_reseau[personnes[i]]) == max_amis:
            most_pop.append(personnes[i])
        i += 1
    return most_pop

##AZOUAGH Safiya RACHID.K Assmâe
##############
# SAE S01.02 #
##############
"""retourne le dictionnaire correspondant au réseau"""
def create_network(list_of_friends):
    dico={}
    i=0
    while i<len(list_of_friends)-1:
        if list_of_friends[i] not in dico:                     # si la personne n'est pas dans le nouveau dico 
            dico[list_of_friends[i]]=[]                        # alors on l'ajoute en tant que clé dans le dico  
        if list_of_friends[i+1] not in dico:                   # si la personne juste apres n'est pas dans le dico
            dico[list_of_friends[i+1]]=[]                      # alors ont l'ajoute en tant que clé du dico 
        dico[list_of_friends[i]].append(list_of_friends[i+1])  # nous ajoutons les amies  de la clé
        dico[list_of_friends[i+1]].append(list_of_friends[i])  # nous ajoutons les amis de la clé 
        i+=2
    return dico

"""retourne un tableau contenant la liste des personne participant au réseau"""
def get_people(network):
     return list(network) #on prend seulement les clés du dico 

"""retourne True ou False si les deux personnes sont amis"""
def are_friends(network, person1, person2):
    if person2 in network[person1]:                           #nous verifions si person1 est dans le groupe d'amis de person2
        return True                                           # si c'est le cas on retrourne True 
    else:
        return False                                          # sinon on retorune False  
    
   
"""retorune True si la personne est ami avec tout le groupe"""
def all_his_friends(network, person, group):
    i=0
    while i<len(group):
        if person==group[i]:
            i+=1
        if are_friends(network,person,group[i])==False:      # si la personne n'est pas ami avec une personne du groupe  
            return False                                     # alors on retourne False 
        i+=1

    return True                                              # si nous arrivons a sortir de la boucle, on retourne True 

"""sert a savoir si le groupe de personnes est une comunauté"""
def is_a_community(network, group):
    i=0                                  
    while i<len(group):                                      # sert a selectioner une seule personne du groupe 
        k=0
        while k<len(group):                                  # nous alons selectionner chaque personne du groupe une part une  
            if group[i] != group[k] and (are_friends(network,group[i],group[k])) ==False : #sert a verifier si les deux personne ne sont 
                return False                                                               # pas amie,dans ce cas la nous retournon False                               
            k+=1
        i+=1
    return True         # si nous sortons de la boucle alors on sait que les tout le monde est amis alors on retourne True 


"""sert a savoir si un groupe est une communauté"""
def find_community(network, group):    
    community = []                                              # on créer un tableau vide communauté
    i=0
    while i < len(group):
        community.append (group[i])                            # on ajoute une par une les personnes du groupe dans le tableau communauté
        if(is_a_community(network, community))==False:         # si les personne dans le groupe ne sont pas une communauté 
            community.pop()                                    # on supprime la derniere personne ajouté au tableau communauté
        i+=1
    return community

"""retourne un groupe en le triant du plus populaire au moins populaire"""
def order_by_decreasing_popularity(network, group):
    friend=[]
    community=[]
    i=0
    while i<len(group):
        tab=[len(network[group[i]]), group[i]] # sert a faire un tableau dans lequel se trouve le nombre d'amis de la personne et son prenom 
        friend.append(tab)                     # nous alons ajouter le tableau que nous venon de créer dans un tableau (friend),afin d'avoir
        i+=1                                   # un tableau avec toutes les personnes et leurs nombre d'amis 
    friend.sort()                              # on trie le tableau dans l'ordre croissant 
    friend.reverse()                           # on se sert de reverse pour le trier dans l'orde decroissant
    i=0
    
    while i<len(friend):
        community.append(friend[i][1])       # on créer un tableau dans lequel il n'y a que le prenoms.
        i+=1
    return community


"""retourne la communauté avce les personnes les plus populaire"""
def find_community_by_decreasing_popularity(network):
    friend=order_by_decreasing_popularity(network, get_people(network)) #nous trions les personne du réseau du plus au moins populaire 
    return find_community(network,friend) #on retourne la communauté du plus populaire


"""sert a trouver un communauté a partir d'une personne,"""
def find_community_from_person(network, person):
    community=[person]
    friend=order_by_decreasing_popularity(network, network[person]) #nous trions les personne du réseau du plus au moins populaire
    i=0
    while i<len(network[person])-1:
        if friend[i] in network[friend[i+1]]:  #nous verifions si la personne est dans le groupe d'amis de la personne juste apres elle 
            community.append(friend[i])        #ceci nous sert a savoir si les deux sont amis mutuellement
            community.append(friend[i+1])      # dans ce cas-là nous les ajoutons au tableau community
        i+=1
    if len(network[person])==1:                #si il n'y a une seule personne dans le groupe d'ami alors on l'ajoute directement à 
        community.append(friend[0])            # communauté
    return community

"""sert a trouver la communauté avec plus de personne"""
def find_max_community(network):
    max_community=''
    net=get_people(network)
    i=0
    while i<len(network):
        community=find_community_from_person(network,net[i]) # nous cherchons la communauté de chaque personne du réseau
        if len(community)>len(max_community): # nous comparons la taille de chaque communaté                                   
            max_community=community           # et nous gardons la plus grande communauté 
        i+=1
    return max_community 

##AZOUAGH Safiya RACHID.K Assmâe