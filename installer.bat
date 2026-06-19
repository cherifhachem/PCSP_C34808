@echo off
echo ====================================================
echo   INSTALLATION ET CONFIGURATION AUTOMATIQUE (.VENV)
echo ====================================================
echo.

:: 1. Création de l'environnement virtuel
echo [1/4] Creation de l'environnement virtuel .venv...
python -m venv .venv
if %errorlevel% neq 0 (
    echo Erreur : Python n'est pas installe ou pas accessible dans le PATH.
    pause
    exit /b
)

:: 2. Mise à jour de base et installation de setuptools pour PyCharm
echo [2/4] Preparation des outils de base...
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install setuptools

:: 3. Installation de tous les packages du projet
echo [3/4] Installation des packages de Data Science (requirements.txt)...
if exist requirements.txt (
    .venv\Scripts\python.exe -m pip install -r requirements.txt
) else (
    echo Erreur : Le fichier requirements.txt est introuvable !
    pause
    exit /b
)

:: 4. Fin de la configuration
echo [4/4] Environnement configure avec succes !
echo.
echo Vous pouvez maintenant ouvrir ce dossier dans PyCharm.
echo ====================================================
pause