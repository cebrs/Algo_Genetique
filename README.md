# Algo_Genetique
Il s'agit d'un projet école, réalisé en BAC+3, qui permet de réaliser une approximation de fonction dite de Weierstrass par algorithme génétique.
Extrait de l'énoncé : 
<img width="323" alt="Enonce" src="https://user-images.githubusercontent.com/94990700/148781596-16cff39b-f527-47ad-bee3-be05a39987d2.png">

Environnement de travail : Spyder

# Fonctionnement
Les algorithmes génétiques sont des algorithmes s’inspirant de la biologie et s’appuyant sur la théorie de l’évolution de Darwin. On part d’une population d’individu de base, que l’on évalue à l’aide d’une fonction dite fitness. On réalise ensuite une sélection parmi ses individus pour pouvoir réaliser des croisements et des mutations afin de faire varier la population initiale. 
Ici, un individu correspond à une combinaison de variables (a,b,c) avec :
- a compris entre 0 et 1 non inclus
- b compris entre 1 et 20 inclus
- c compris entre 1 et 20 inclus
La population initiale est générée de manière aléatoire en petit nombre.

Critère d'arrêt : si la fonction fitness d'un individu est <0.037 alors il est considéré comme le résultat le plus proche possible de la fonction que l’on cherche à approximer.


