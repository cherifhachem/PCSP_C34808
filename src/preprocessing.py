import pandas as pd  # <--- IL FAUT ABSOLUMENT CETTE LIGNE
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Ensuite viennent vos fonctions :
# def handle_missing_values(df: pd.DataFrame): ...
# def remove_outliers_iqr(df: pd.DataFrame): ...
# def split_and_scale(df: pd.DataFrame, config: dict): ...


# ... gardez vos fonctions handle_missing_values et remove_outliers_iqr ici ...

def split_and_scale(df: pd.DataFrame, config: dict):
    """
    Sépare les données en train/test et applique une mise à l'échelle (scaling).
    Utilise la graine aléatoire (seed) définie dans la configuration pour la reproductibilité.
    """
    target_col = config['data']['target_column']
    test_size = config['data']['test_size']
    seed = config['project']['random_seed']
    scale_features = config['preprocessing']['scale_features']

    # 1. Séparation Features (X) et Cible (y)
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # 2. Partitionnement Train/Test avec la graine (random_state)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=seed
    )

    # 3. Mise à l'échelle (Scaling) optionnelle
    scaler = None
    if scale_features:
        scaler = StandardScaler()
        # On ajuste sur le Train et on transforme Train ET Test
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test, scaler