# Pokemon Battle System

*Projet de Baptiste GOSSELET*.

## Présentation du Projet

L'idée de ce projet est de réaliser une reproduction simplifiée du système de combat des jeux Pokémon à la façon de [**Pokémon Showdown**](https://pokemonshowdown.com/).

Le jeu propose à deux dresseurs (dont l'un peut être contrôlé par l'ordinateur) de choisir trois Pokémon pour combattre. Le joueur parvenant à mettre K.O. l'équipe de son adversaire gagne la partie. 

### Captures d'écran

![capture_1](./img/screenshots/capture_1.png)
![capture_2](./img/screenshots/capture_2.png)

### Executer le programme

Pour lancer ce jeu, il faut utiliser la commande `python3` avec le fichier `src/main.py` depuis la racine du projet :
```bash
python3 src/main.py
``` 

Pour lancer les tests, il s'agit du fichier `test/mainTest.py`
```bash
python3 test/mainTest.py
```

## Mécaniques implémentées

Au lancement de la partie, les joueurs peuvent choisir les 3 pokemons avec lesquels il va combattre. 
Le logiciel permet une option de randomisation et de joueur ordinateur.

Les attaques des pokémons sont pré-définies et sont au nombre de 4. Si le joueur veut attaquer, il devra choisir entre l'une de ces 4 options. Comme dans le jeu original, chaque capacité possède une puissance, une précision, un type, et un éventuel effet, soit de soin ou de statuts. Le survol de la sourie sur l'attaque permet de lire sa description.

Le switch est une mécanique de jeu fondamentale de Pokemon qui consiste à retirer le Pokémon utilisé et de l'échanger avec l'un de son équipe.
Etant donné que les pokemons sont avantagés face à certains autres, il est parfois justifié de faire cet échange. 

Les Pokemons possèdent des caractéristiques uniques : des statistiques qui déterminent la puissance de leurs attaques ou leur résistance, 
ainsi que d'un ou deux types qui ont des effets multiplicateurs de dégât selon l'attaque utilisée.

Les joueurs choisissent leurs actions à tour de rôle, mais ce qui détermine l'ordre d'attaque sont la comparaison de vitesse des deux pokemons en jeu, 
la priorité des attaques, ou bien le switch qui agit toujours avant l'attaque adverse.

Enfin, le simulateur implémente aussi les effets de statuts qui sont des malus dû à des effets secondaires d'attaques : la brûlure (inflige de petits dégâts chaque tour divise l'attaque par 2), la gelûre (même chose avec l'attaque spéciale), la paralysie empêchant d'attaquer ou encore le poison qui inflige des dégâts croissants, etc.