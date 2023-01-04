# Pokemon Battle System

## Présentation du Projet

Projet de Baptiste GOSSELET.

L'idée de ce projet est de réaliser une reproduction simplifiée du système de combat des jeux Pokémon. Ce programme s'inspire donc du simulateur **Pokémon Showdown**.

![GB](https://i.ytimg.com/vi/p9B5IyC0yfI/hqdefault.jpg)
![SD](https://lh3.googleusercontent.com/nNVM-eEpuxenHf5OlCeuOINr-f7Gpg0jebk1He6liYO73bZ4thAYE8HfmDuhcCI7jWsQd3h80XZKBLb4heMYQxQynA=w640-h400-e365-rj-sc0x00ffffff)

## Adaptation du système 

Ce système de combat étant très complet, il est nécessaire de simplifier plusieurs mécaniques pour rendre le développement de ce projet possible dans le cadre de cette UE.
Ainsi ce système de combat conserve les qualités suivantes :

### Les Dresseurs
Dans l'univers du jeu, les joueurs sont appelés des "dresseurs de Pokémon". Lors d'un combat, deux dresseurs font s'affronter leur équipe de Pokémon. Ils peuvent chacun posséder une équipe composée de 6 Pokémon maximum.

### Les Pokémon

Les Pokémon possèdent des caractéristiques uniques comme les statistiques qui représentent leur force (PV, Atk, Déf, Atk.Spé, Def.Spé, Vitesse). 

Ils possèdent également un "type qui affecte la résistance et la faiblesse aux différentes attaques. 

Enfin, les Pokémon auront chacun un "Moveset" de 2 capacités prédéfinies, une sélection parmi celles que le Pokémon peut utiliser.

La redéfinition du système pour ce projet édulcore donc : le choix du niveau, les points EV et IV, le Talent, la notion de double type, movepool, objets, et mécaniques de génération (Méga-évolution, Dynamax, et Teracristal) ...

### Capacités

Les capacités sont les attaques que le Pokémon peut lancer ("Tonnerre" de Pikachu par exemple). Celles-ci possèdent une puissance de base, une précision, une catégorie, un type, et un éventuel effet.

Il y a 3 catégories de capacités : 
- Physique : dont les dégats sont calculés à partir des statistiques d'attaque et de défense
- Spécial : calculé à partir des stats d'Atk.spé et Def.Spé
- Secondaire : n'infligeant pas de dégat direct mais possède un effet secondaire

### Types 

Les types sont des éléments attitrés aux Pokémon et aux capacités. Les premières versions du jeu en comportent 15.
Feu, Eau, Plante, Electrique, Roche, ...

Les types sont liés par une table des faiblesses et des résistances qui multiplie ou divise les dégâts des capacités.
Par exemple nous avons : 
- Eau > Feu 
- Feu > Plante
- Plante > Eau

Une attaque "Super efficace" multiplie les dégats par deux, une attaque "Pas très efficace" divise par deux.

Aussi, lorsqu'un pokémon utilise une capacité du même type que le sien celle-ci reçoit un bonus de "Stab" qui multiplie les dégats par 1,5. Ces bonus et malus sont cumulables.

Enfin, les types peuvent immuniser à certains statuts : un Pokémon poison ne peut pas être empoisonné, un Pokémon Electrique ne peut pas être paralysé.

### Statuts

En plus des dégâts bruts, Pokémon possèdent diverses mécaniques de malus passifs. Cette adaptation gardera celles-ci : 
- Poison : Inflige 1/16PV à la fin du tour, puis 2/16, puis 3/16, ... Le compteur est réinitialisé si le Pokémon est retiré.
- Sommeil : Le Pokémon dort et n'attaque plus, il se réveille après deux tours
- Paralysie : Le Pokémon a 1/4 de chance d'être paralysé et ne pas attaquer, ce statut divise aussi la vitesse du Pokémon par 2 

Les Pokémon ne peuvent recevoir qu'un seul statut et il ne peut généralement pas être remplacé par un autre. 

### Les actions 
Comme pour **Pokémon Showdown**, les joueurs ont la possibilité d'attaquer ou bien de changer de Pokémon. 

### Bilan des mécaniques retenues
- Pokémon : base stat + un seul type + 2 capacités prédéfinies 
- Capacité : puissance + précision + type + effet secondaire
- 15 types 
- Statuts : Poison, Sommeil, Paralysie
- Action : Attaquer ou Changer
