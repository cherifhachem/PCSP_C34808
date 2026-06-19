# 🚀 Mise en place d'un pipeline de Data Science structuré, reproductible et automatisé



## 📌 1. Création et Configuration de l'Environnement Virtuel



La toute première étape a consisté à isoler les dépendances du projet afin d’éviter les conflits de versions et garantir la reproductibilité de l’environnement de développement.



### 🔧 Informations de l’environnement



*\*Nom de l’environnement :\*\* `.venv`
*\*Emplacement absolu :\*\* `C:\\Users\\Hachem\\Desktop\\cherifH\\.venv\\`
*\*Interpréteur utilisé :\*\* `Python 3.13`



### ⚠️ Résolution d’un blocage technique



L’exécuteur de tests de PyCharm nécessitait l’installation de l’outil de distribution `setuptools`.



Commande utilisée :



```bash

python -m pip install setuptools

```




# 🏗️ 2. Architecture Technique du Projet (`cherifH`)



L’espace de travail a été structuré selon les standards modernes de l’ingénierie logicielle appliquée à la Data Science.



## 📂 Arborescence finale du projet



```text

cherifH/                        # Racine absolue du projet

│

├── .venv/                      # Environnement virtuel local (exclu de Git)

├── configs/                    # Centralisation des paramètres

│   └── config.yaml             # Graine (42), taille du test (0.2), etc.

├── data/                       # Répertoire des données brutes/propres

│   └── .gitkeep                # Force Git à conserver le dossier vide

├── src/                        # Code source principal

│   ├── \_\_init\_\_.py             # Rend le dossier importable

│   ├── preprocessing.py        # Nettoyage + scaling + split

│   └── utils.py                # Fonctions utilitaires

├── tests/                      # Validation qualité logicielle

│   └── test\_preprocessing.py   # Test pytest de reproductibilité

├── .gitignore                  # Fichiers exclus du versioning

├── installer.bat               # Installation automatique

└── main.py                     # Point d’entrée du pipeline



# ⚙️ 3. Développement du module de préparation (`src/preprocessing.py`)



Une fonction fondamentale nommée `split\_and\_scale()` a été développée afin de préparer les données destinées aux futurs modèles d’Intelligence Artificielle.


## 🔄 Pipeline appliqué


### 1. Séparation des variables

La fonction sépare :


* les \*\*variables explicatives\*\* (\*features\*)

* de la \*\*variable cible\*\* (`pm25`)


\---



### 2. Partitionnement des données



Le dataset est découpé en :



\* \*\*80 %\*\* pour l’entraînement

\* \*\*20 %\*\* pour le test



\---



### 3. Mise à l’échelle des données



Application d’un `StandardScaler` afin de :



* centrer les données

* réduire les écarts-types

* homogénéiser les ordres de grandeur



\---



## ✅ Correction majeure réalisée



Ajout de l’import indispensable :



```python

import pandas as pd

```



Cet import était nécessaire pour interpréter correctement l’annotation :



```python

df: pd.DataFrame

```



\---



# 🧪 4. Validation Mathématique de la Reproductibilité (`tests/`)



Afin de garantir la robustesse et le caractère déterministe du pipeline, un test unitaire automatisé a été conçu avec `pytest`.



## 🔬 Fonctionnement du test



Le script :



1\. génère une matrice fictive de \*\*100 lignes\*\*

2\. appelle `split\_and\_scale()` deux fois

3\. injecte la même configuration :



&#x20;  \* `random\_seed: 42`



\---



## 📏 Vérification stricte



La comparaison est réalisée via :



```python

np.testing.assert\_array\_equal

```



Le test n’est validé que si les matrices générées sont \*\*strictement identiques\*\*.



\---



## ✅ Résultat obtenu



```text

PASSED \[100%]

```



Le pipeline est donc officiellement \*\*reproductible\*\*.



\---



# 🔒 5. Configuration et Sécurisation Globale



## 🧾 Gestion du versioning avec Git



Le fichier `.gitignore` exclut :



```text

data/\*

\_\_pycache\_\_/

.ipynb\_checkpoints/

.venv/

```



Tout en conservant la structure du projet grâce au fichier `.gitkeep`.



\---



## 🚦 Point d’entrée principal (`main.py`)



Le pipeline principal a été sécurisé avec :



### ✅ Chargement dynamique des configurations



```python

os.path.join()

```



Permet une gestion robuste et portable des chemins système.



\---



### ✅ Fixation universelle des graines aléatoires



```python

set\_seed()

```



Garantit la reproductibilité complète des expériences.



\---



### ✅ Mode graphique non interactif



```python

matplotlib.use('Agg')

```



Permet :



* la génération automatique de graphiques

* l’exécution sur serveur

* l’absence de fenêtres bloquantes



\---



# ⚡ 6. Automatisation du Déploiement (`installer.bat`)



Toutes les dépendances du projet ont été figées dans :



```bash

requirements.txt

```



via :



```bash

python -m pip freeze > requirements.txt

```



\---



## 🖱️ Installation “En un clic”



Le script Windows `installer.bat` automatise entièrement :



* la création du `.venv`

* l’installation des dépendances

* la mise à jour des outils JetBrains

* la restauration complète de l’environnement



\---



## 🎯 Avantage principal



Pour réutiliser le projet sur une autre machine :



1\. Copier le dossier `cherifH`

2\. Double-cliquer sur `installer.bat`



➡️ Aucun besoin de retaper les commandes manuellement.



\---



\# ✅ Résultat Final



Le projet dispose désormais :



* d’une architecture professionnelle

* d’un pipeline reproductible

* d’un environnement isolé

* d’une automatisation complète

* d’une validation scientifique via tests unitaires



Le système est prêt pour :



* l’entraînement de modèles IA

* l’expérimentation scientifique

* le déploiement futur

* la collaboration Git/GitHub



\---



