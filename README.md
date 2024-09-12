## tristan_nouzille_projet4

# Gestion des Tournois d'Échecs

## Description
Ce projet est une application de gestion de tournois d'échecs qui permet de créer des tournois, d'ajouter des joueurs, de lancer des matchs et de générer des rapports sur les joueurs et les tournois.

## Fonctionnalités
- Créer un nouveau tournoi
- Ajouter des joueurs
- Afficher tous les joueurs et tous les tournois
- Lancer un tournoi et gérer les matchs
- Générer des rapports pour les joueurs et les tournois avec leurs matchs

## Prérequis
Avant de commencer, assurez vous d'avoir Python 3.x installé sur votre machine. Vous pouvez vérifier cela en exécutant :

```bash
python --version

```
## Installation

1. Clonez le dépôt :

  ```
  git clone https://github.com/tristan-nouzille/tristan_nouzille_projet4
  ```

  Ensuite accédez au dossier en tapant cette ligne :

  ```
  cd tristan_nouzille_projet4
  ```
2. Créez un environnement virtuel (optionnel mais recommandé) :

# Sur macOS et Linux
a. installer virtualenv:

 ```
 python3 -m pip install virtualenv
 ```
b. créez votre dossier d'environnement virtuel:

 ```
 python3 -m virtualenv venv
 ```
c. Activez votre environnement avec :

  ```
  source venv/bin/activate 
  ```
  une fois effectuer, votre terminal s'affichera comme ceci :

  ```
  (env)
  NOM_de_votre_pc-PC ~/nom_de_votre_dossier/tristan_nouzille_projet4
  ```

3. Installez les dépendances nécessaires :
   
   ```
    pip install -r requirements.txt
   ``` 
 si vous souhaitez voir toutes les dépendances installé, voici la ligne à taper:

  ```
  pip freeze
  ```
  
4. Lancez l'application :

 ```
 python main.py
 ```

# Sur Windows
 
a. installer virtualenv:

 ```
 pip install virtualenv
 ```
b. créez votre dossier d'environnement virtuel:

 ```
 python -m venv env
 ```
c. Activez votre environnement avec :

  ```
  source env\Scripts\activate  
  ```
une fois effectuer, votre terminal s'affichera comme ceci :
  ```
  (env)
  NOM_de_votre_pc-PC ~/nom_de_votre_dossier/tristan_nouzille_projet4
  ```

3. Installez les dépendances nécessaires :
   
   ```
   pip install -r requirements.txt
   ```

  si vous souhaitez voir toutes les dépendances installé, voici la ligne à taper:

  ```
  pip freeze
  ```
  
4. Lancez l'application :

 ```
 python main.py
 ```

## Utilisation

Lorsque l'application est lancée, un menu principal apparaîtra vous permettant de choisir parmi différentes options de gestion des tournois. Suivez les instructions à l'écran pour naviguer et découvrir les différentes fonctionnalités.

# Style de Code
Pour maintenir un code de qualité, utilisez flake8 pour vérifier le style de votre code. Voici comment utiliser :

Tout d'abord vérifier dans votre dépendance si vous avez flake8 et flake8-html avec : 

 ```
  pip freeze
 ```
 
Pour vérifier le style de votre code, exécutez la commande suivante dans le répertoire de votre projet :

 ```
 flake8 --format=html --htmldir=rapport_flake8
 ```

Après cette ligne exécuté un nouveau dossier sous le nom de "rapport_flake8" cera créé dans votre dossier principal.

Si vous avez déjà un dossier pour les rapports flake8, tapez tout simplement cette ligne :

 ```
 flake8 --htmldir rapport_flake8/
 ```
Voilà pour le lancement des rapports.

Pour tout autre information concernant la norme PEP8 je vous invite à lire la documentation en suivant ce lien "https://peps.python.org/pep-0008/"
En ce qui concerne l'aide à l'exécution de flake8, vous pouvez taper cette ligne de commande :

 ```
 flake8 -h
 ```
