import sys
import os
import matplotlib

# --- Complété : Basculement sur le backend non-interactif ’Agg ’ ---
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from src.utils import load_config, set_seed


def main():
    # --- Complété : Chargement du fichier de configuration configs/config.yaml ---
    # On définit le chemin vers le fichier de config
    config_path = os.path.join("configs", "config.yaml")
    config = load_config(config_path)

    # Fixation universelle des graines pour la reproductibilite
    set_seed(config['project']['random_seed'])

    print("[RUN ] Execution du pipeline scientifique ...")
    # Le reste du code execute les etapes de pretraitement et d’apprentissage ...


if __name__ == "__main__":
    main()