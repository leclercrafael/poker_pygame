Creating a poker game using pygame

This project is made by Pierre-Guillaume Petitmangin and Rafaël Leclerc, both student at Mines Paris PSL.

---

# ♠️ Projets Pygame : Poker Orienté Objet (POO) ♣️

## Table des Matières
1.  [Aperçu du Projet](#aperçu-du-projet)
2.  [Concepts Clés de la POO](#concepts-clés-de-la-poo)
3.  [Structure du Répertoire](#structure-du-répertoire)
4.  [Installation et Démarrage](#installation-et-démarrage)
5.  [Dépendances](#dépendances)
6.  [Développement et Contribution](#développement-et-contribution)

---

## 1. Aperçu du Projet

Ce projet est la création d'un jeu de poker (logiciel) développé en **Python** en utilisant la bibliothèque **Pygame** pour l'interface graphique.

L'objectif principal est d'appliquer les principes de la **Programmation Orientée Objet (POO)** pour garantir un code modulaire, maintenable et évolutif. Le jeu se concentre sur les mécanismes de base du poker, notamment la gestion des cartes, des mains, des joueurs, et l'évaluation des combinaisons.

### Objectifs Techniques

* **POO Solide :** Utilisation intensive des classes, de l'héritage et des classes abstraites.
* **Modularité :** Chaque élément du jeu (carte, joueur, jeu, table) est une classe distincte.
* **Performance :** Utilisation d'outils Python optimisés (comme `itertools`) pour l'analyse rapide des mains de poker.

---

## 2. Concepts Clés de la POO

Le code est structuré autour de plusieurs classes, dont les plus importantes implémentent des concepts fondamentaux de la POO :

| Concept POO | Classe(s) Concernée(s) | Rôle dans le Projet |
| :--- | :--- | :--- |
| **Abstraction** | `GameObject` (classe abstraite) | Définit un **contrat** de base. Tout élément graphique du jeu doit en hériter et implémenter une méthode `draw()` pour être affichable à l'écran. |
| **Encapsulation** | `Carte`, `Joueur` | Les attributs sensibles (ex: `__solde` d'un joueur, les détails d'une carte) sont masqués ou protégés (utilisant `_` ou `__`) et ne sont modifiables que via des méthodes spécifiques (getters/setters). |
| **Héritage** | `JoueurIA(Joueur)`, `CartePhysique(Carte)` | Permet de construire des classes spécialisées à partir d'un modèle général (ex: un joueur IA hérite du comportement de base d'un `Joueur` mais ajoute sa propre logique de décision). |
| **Polymorphisme** | Méthode `draw()` | Permet à chaque objet graphique (`Carte`, `Jeton`, `Bouton`) d'être dessiné via le même appel de fonction (`objet.draw()`), bien que la logique interne soit différente pour chaque type d'objet. |

---

## 3. Structure du Répertoire

Voici les fichiers et dossiers clés du projet :
