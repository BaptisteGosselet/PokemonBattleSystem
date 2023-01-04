# Pokemon Battle System

## Présentation du Projet

Projet de Baptiste GOSSELET.

L'idée de ce projet est de réaliser une reproduction simplifiée du système de combat des jeux Pokémon. Ce programme s'inspire donc du simulateur **Pokémon Showdown**.

![GB](https://i.ytimg.com/vi/p9B5IyC0yfI/hqdefault.jpg)
![SD](https://lh3.googleusercontent.com/nNVM-eEpuxenHf5OlCeuOINr-f7Gpg0jebk1He6liYO73bZ4thAYE8HfmDuhcCI7jWsQd3h80XZKBLb4heMYQxQynA=w640-h400-e365-rj-sc0x00ffffff)

## Adaptation du système 

Ce système de combat étant très complet, il est nécessaire de simplifier plusieurs mécaniques pour rendre le développement de ce projet possible dans le cadre de cette UE. 
Les mécaniques conservées sont les suivantes : 
- Dresseur : équipe de 1 à 6 Pokémon
- Liste des Pokémon : https://www.smogon.com/dex/rb/formats/ou/
- Pokémon : base stat (pas d'EV/IV, pas de Spé) + un seul type + 2 capacités prédéfinies 
- Capacité : puissance + précision + type + effet secondaire + priorité de l'attaque (pas de catégorie physique/spécial)
- Type : les 15 premiers types 
- Statuts : Poison, Sommeil, Paralysie
- Action : Attaquer ou Changer
