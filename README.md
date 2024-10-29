# **Algorithmes de Tri avec Visualisation**

Bienvenue dans ce projet qui implémente plusieurs algorithmes de tri classiques en Python, avec une visualisation graphique dynamique utilisant Matplotlib. L'objectif est d'aider à comprendre visuellement le fonctionnement de ces algorithmes de tri grâce à des animations.

## **Fonctionnalités**

- **Algorithmes de tri disponibles** :
  - **Bogo Sort** : Un algorithme inefficace mais amusant qui tente de trier les éléments en les mélangeant aléatoirement jusqu'à ce qu'ils soient triés.
  - **Bubble Sort** : Un algorithme plus classique qui compare les éléments adjacents et les échange si nécessaire, triant la liste de manière itérative.

- **Visualisation dynamique** :
  - Les algorithmes sont accompagnés d'une visualisation graphique en temps réel qui montre les étapes de tri.
  - Les barres représentant les éléments sont mises à jour au fur et à mesure que l'algorithme effectue ses comparaisons et ses échanges.

- **Paramètres configurables** :
  - Choisissez le nombre d'éléments à trier.
  - Sélectionnez la vitesse de l'animation.
  - Choisissez l'algorithme de tri souhaité.

## **Installation**

### Prérequis
Assurez-vous d'avoir Python installé (version 3.6 ou supérieure). Ensuite, vous devrez installer les dépendances Python listées dans le fichier `requirements.txt`.

1. Clonez ce dépôt :
   git clone https://github.com/Ceyrocx/tri.git

2. Installez les dépendances requises :
   pip install -r requirements.txt

### Dépendances

Les principales dépendances de ce projet sont :

- `matplotlib` : Pour la visualisation graphique des algorithmes de tri.
- `numpy` : Pour gérer les séquences numériques (utilisé pour les axes dans les graphiques).

## **Utilisation**

Ce projet peut être utilisé en ligne de commande avec des arguments permettant de configurer l'algorithme, le nombre d'éléments à trier, et la vitesse de la visualisation.

### Commande de base

python run.py -n nombre d'éléments -t algorithme -s vitesse

### Exemples

- **Trier 10 éléments avec le tri Bogo à une vitesse de 0,05 secondes entre chaque étape** :
  python run.py -n 100 -t "bubble" -s 0.05

### Options disponibles

- `-n`, `--amount` : Nombre d'éléments à trier (par défaut : 5).
- `-t`, `--tri` : Algorithme de tri à utiliser (`bogo` ou `bubble`, par défaut : `bogo`).
- `-s`, `--speed` : Temps de pause (en secondes) entre chaque étape de la visualisation (par défaut : 0,01).

## **Organisation du Projet**

- **`run.py`** : Point d'entrée du projet, gère les arguments de la ligne de commande et lance le tri sélectionné.
- **`bogo.py`** : Contient l'implémentation et la visualisation du Bogo Sort.
- **`bubble.py`** : Contient l'implémentation et la visualisation du Bubble Sort.
- **`visualisationTri.py`** : Fournit les fonctions de visualisation pour les algorithmes de tri.
- **`requirements.txt`** : Fichier listant les dépendances nécessaires au projet.

## **Améliorations Futures**

Voici quelques idées pour améliorer ce projet :

- Ajouter d'autres algorithmes de tri tels que QuickSort, MergeSort, Insertion Sort, etc.
- Améliorer l'interface utilisateur pour rendre les visualisations plus interactives.
- Permettre de personnaliser davantage les couleurs et les animations.
- Ajouter des tests unitaires pour assurer le bon fonctionnement des algorithmes.

## **Contact**

Si vous avez des questions ou des suggestions, n'hésitez pas à ouvrir une issue ou à me contacter directement.
