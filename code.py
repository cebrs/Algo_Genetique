# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 11:51:40 2021

@author: celia
"""
import random
import math

class individu:
    def __init__(self,val=None): #constrcuteur
        if(val == None): # si on ne donne pas les valeurs de a,b,c => aléatoire
            a = random.random()
            while(a == 0):
                a = random.random()
            b = random.randint(1,20)
            c = random.randint(1,20)
            self.val = [a,b,c]
        else:
            self.val = val #si les valeurs sont fournies
        self.difftemp = self.fitness()
    
    def __str__(self): 
        """ permis d'écrire print(indiv) avec indiv un invidu"""
        characters = "(a b c) = ( "
        for value in self.val:
            characters += str(value)
            characters += " "
        characters+=")"
        return characters #retourner les valeurs de a,b,c
    
    def calcul(self, i): #à vérifier / calcule la température d'un individu à l'instant i
        t = 0
        a = self.val[0]
        b = self.val[1]
        c = self.val[2]
        for n in range(c):
            t+=((a**n)* math.cos((b**n)*math.pi*i))
        return t
    
    def temperature_list(self):
        time_temp = temperature_sample()
        calcultemp = dict()
        for i in time_temp.keys():
            calcultemp[i] = self.calcul(i)
        return calcultemp
    
    def fitness(self): #à tester
        """évaluer l'individu c'est connaitre sa différence par rapport 
        à la température mesurée de l'étoile"""
        #problème = plusieurs tests selon plusieurs températures
        #faire une liste de différences de température ?
        #autre ?
        time_temp = temperature_sample()
        self.difftemp = 0
        listdiff = []
        calcultemp = self.temperature_list()
        for j in time_temp.keys():
            listdiff.append(time_temp[j]-calcultemp[j])
        for x in listdiff:
            self.difftemp += abs(x)
        self.difftemp = self.difftemp/len(time_temp)
        return self.difftemp

def create_rand_pop(count):
    compteur = 0
    pop =[]
    while(compteur < count):
        indiv = individu()
        pop.append(indiv)
        compteur+=1
    return pop

def temperature_sample():
    time_temperature = dict() #à un temps on associe une temperature
    file = open('temperature_sample.csv','r')#possibilité de passer le fichier en paramètres
    x= file.readlines()
    del x[0]
    for i in x:
       y=i.split(';')
       time_temperature[float(y[0])] = float(y[1])
    file.closed
    return time_temperature

#def calibrate():
#Prendre le triplet de valeur donné
#val=[a,b,c]
#indiv = individu(val))
#print(indiv.difftemp())


def evaluate(pop):
    return sorted(pop,key=lambda individu : individu.difftemp) 

def selection(pop, hcount, lcount):
    selec = pop[:hcount]
    for i in range(len(pop)-lcount, len(pop)):
        selec.append(pop[i])
    return selec

def croisement(ind1, ind2): #à tester #vérifier si on peut croiser 3 individus 
    list_croisement = []
    mem1 = ind1.val[0:2]
    mem1.append(ind2.val[2])
    mem2 = ind2.val[0:2]
    mem2.append(ind1.val[2])
    ind1.val = mem1
    ind2.val = mem2
    list_croisement = [ind1,ind2]
    return list_croisement

def mutation(i):
    x = random.randint(0,2)
    if(x == 0):
        i.val[0] = random.random()
        while(i.val[0] == 0):
            i.val[0] = random.random()
    else:
        i.val[x] = random.randint(1,20)
    return i

def algoloopSimple():
    pop=create_rand_pop(30) #je commence par créer une population aléatoire de 30 individus
    solutiontrouvee = False
    nbriteration = 0
    while not solutiontrouvee: #j'entre dans une boucle jusqu'à ce que je trouve une solution 
        print("iteration numéro :", nbriteration)
        nbriteration+=1
        evaluation=evaluate(pop) #j'évalue la population, le retour est une liste triée selon la fitness des individus
        #penser à modifier la condition d'arrêt
        if evaluation[0].fitness() < 0.037: #c'est-à-dire si j'ai une solution proche de la fonction
            solutiontrouvee = True
        else: #pas de solution
            select = selection(evaluation, 11,3) #je sélectionne les 11 meilleurs et les 3 pires
            croises=[]
            for i in range(0,len(select),2): #croisement deux par deux avec les sélectionnées
                croises +=croisement(select[i], select[i+1])
            mutes=[]
            for i in select: #j'opère la mutation sur chacun des sélectionnés
                mutes.append(mutation(i))
            newalea=create_rand_pop(5)#j'ajoute 5 nouveaux individus aléatoires
            pop=select[:]+croises[:]+mutes[:]+newalea[:] #nouvelle population
    print("solution :", evaluation[0])
# %% zone du main
if __name__ == '__main__':
    algoloopSimple()
