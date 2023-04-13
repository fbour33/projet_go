Explication de chaque fichier : 
----------------------------------


myPlayer.py
-----------

Ce fichier contient notre player le plus abouti. Il est constitué d'un alphabeta avec une heuristique
qui sera détaillée dans le fichier endGame.py. Aussi, nous avons une bibliothèque d'ouverture qui
est dans le fichier openLibrary.json.

alphaBeta.py
------------

Ce fichier contient une version de alphabeta avec la même bibliothèque d'ouverture et la même 
heurstique. Ce fichier avait un but lors de la phase de développement de l'heuristique car cela
permettait de comparer les performances de notre heurstique au fur et à mesure de son implémentation

endGame.py
----------

Ce fichier contient notre heuristique. Dans ce fichier, il y a les fonctions isEndGame() et 
isEndGameBlack() qui sont notre première version de l'heurstique, elle servait de base pour tester 
l'intégralité du projet.

Par la suite, pour obtenir une heuristiqueplus performante, on créer une fonction neighbors() qui
retounre le nombre de voisins de couleur noire et blanche. Par la suite, la fonction heuristique()
permet de calculer une version plus complexe de l'heuristiqueen prenant en compte les voisins des 
cases sur lesquelles on veut poser notre pion, le nombre de pion que l'on capture de l'aversaire, 
ainsi que la différence de pion que l'on a avec l'adversaire. Aussi, pour ne pas manquer l'occasion 
de gagner des parties facilement, si l'adsersaire fait un PASS, on calcul le score final pour voir 
s'il est préférable de continuer à jouer ou si jouer PASS nous permet de gagner.
Notre améliorationf finale est que lorsqu'il y a plus de 60 pièces sur le plateau, il est rapide de 
calculer précisement le score final sans trop entacher les performances donc on se permet de le 
faire pour améliorer notre heurstique en fin de partie.

Enfin, la fonction coloredHeuristique() permet de généraliser la fonction heuristique() en fonction 
de la couleur du joueur qui fait appel à cette fonction.

buildOpenLibraby.py
---------------

Pour créer la bibliothèque d'ouverture, nous avons utilisé le fichier proGameArchives.json contenant un ensemble
de parties jouées par des pros. 
Dans le fichier buildOpenLibraby.py, on réccupère la totalité des coups joués par le gagnant de la 
partie. Ensuite, on 

