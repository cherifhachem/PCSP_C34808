# Project-PCSP
Mise en place d'un pipeline de Data Science structuré, reproductible et automatisé
1.	Création et Configuration de l'Environnement Virtuel
La toute première étape a consisté à isoler les dépendances de mon projet pour éviter les conflits de versions.
•	Nom de l'environnement : .venv
•	Emplacement absolu : C:\Users\Hachem\Desktop\cherifH\.venv\
•	Interpréteur sous-jacent : Python 3.13
•	Résolution du blocage technique : L'exécuteur de tests de PyCharm nécessitait l'outil de distribution setuptools. configuré via la commande : 
python -m pip install setuptools
2.	Architecture Technique du Projet (cherifH)
L’espace de travail est structuré selon les standards de l'ingénierie logicielle en Data Science. Voici l'arborescence finale située sur le bureau :

cherifH/                        # Racine absolue du projet
│
├── .venv/                      # Environnement virtuel local (exclu de Git)
│
├── configs/                    # Centralisation des paramètres
│   └── config.yaml             # Contient la graine (42), la taille du test (0.2), etc.
│
├── data/                       # Répertoire des données brutes/propres
│   └── .gitkeep                # Force Git à conserver le dossier même s'il est vide
│
├── src/                        # Code source (Cœur logique)
│   ├── __init__.py             # Rend le dossier importable en tant que module Python
│   ├── preprocessing.py        # Nettoyage, IQR, et fonction split_and_scale()
│   └── utils.py                # Fonctions d'aide (load_config, set_seed)
│
├── tests/                      # Validation de la qualité logicielle
│   └── test_preprocessing.py   # Script pytest vérifiant la reproductibilité
│
├── .gitignore                  # Règles d'exclusion (cache, .venv, données lourdes)
├── installer.bat               # Script d'automatisation d'environnement "En un clic"
└── main.py                     # Point d'entrée unique de votre pipeline d'exécution

3.	Développement du Code de Préparation (src/preprocessing.py)
On a développé et corrigé la fonction fondamentale split_and_scale chargée de préparer la matière première pour les futurs modèles d'Intelligence Artificielle.
Cette fonction applique le flux de traitement suivant :
1.	Séparation : Elle sépare les variables explicatives (features) de la variable cible (la colonne de pollution pm25).
2.	Partitionnement : Elle découpe le jeu de données en un ensemble d'entraînement (80%) et un ensemble de test (20%).
3.	Mise à l'échelle (Scaling) : Elle applique un StandardScaler (centrage-réduction) pour harmoniser l'ordre de grandeur des données.
•	Correction majeure : Ajout de l'import import pandas as pd indispensable à la lecture de l'annotation de type df: pd.DataFrame.
4.	Validation Mathématique de la Reproductibilité (tests/)
Pour prouver que votre code est robuste et déterministe, nous avons conçu un test unitaire automatisé avec le framework pytest dans test_preprocessing.py.
•	Mécanisme : Le test génère une matrice fictive de 100 lignes et appelle la fonction split_and_scale deux fois de suite en lui injectant la même configuration (verrouillée sur la graine aléatoire random_seed: 42).
•	Assertion : Grâce à np.testing.assert_array_equal, le script ne valide que si les matrices générées lors du premier et du deuxième appel sont strictement identiques, au pixel près.
•	Résultat : PASSED [100%]. Le code est officiellement certifié reproductible.
5.	Configuration et Sécurisation Globale (.gitignore & main.py)
•	Gestion du Code Source via Git : Le fichier .gitignore scientifique masque les éléments locaux lourds ou temporaires (data/*, __pycache__/, .ipynb_checkpoints/) tout en préservant la structure du projet.
•	Fermeture du Pipeline Principal (main.py) : On a programmé le point d'entrée de l'application :
	Chargement dynamique de configs/config.yaml via un chemin système sécurisé (os.path.join).
	Fixation universelle des graines de hasard (set_seed).
	Activation du mode graphique non-interactif matplotlib.use('Agg') pour permettre la génération et la sauvegarde de graphiques de pollution en arrière-plan sans ouvrir de pop-up bloquante.
6.	Automatisation du Déploiement "En un Clic" (installer.bat)
Pour finir, on a figé l'intégralité de nos dépendances dans un fichier requirements.txt (python -m pip freeze > requirements.txt) et créé un script d'automatisation Windows nommé installer.bat.
Désormais, pour travailler sur une autre machine, il suffit de copier ce dossier et de double-cliquer sur installer.bat. Le script se charge seul de recréer le .venv, de mettre à jour les outils JetBrains, et d'installer l'intégralité des packages de calcul à l'identique, sans taper une seule commande.

