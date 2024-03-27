"""
MAIN FILE == > CONEVNTION RAJOUTER INFO DU FICHIER QUESTCE QUE CA FAIT 1 seule ligne
"""

import os
import sys

import pandas as pd
import joblib  # Pour les anciennes versions de scikit-learn

from src.functions import preprocess_and_predict

# ==> PB IMPORTS
# 1 Les builtin (existe deja dans python de base )
# 2 les lib installées
# 3 le packages / sous packages modules sous modules du code
# ==> Utiliser isort
# ==> UTILISER black


def main(input_file):
    """Add a docstring  : https://www.datacamp.com/tutorial/docstrings-python"""

    # Charger le fichier CSV ==> EN ANGLAIS
    input_folder = "data/source/"
    output_folder = "data/output/"
    df_test = pd.read_csv(os.path.join(input_folder, input_file), sep=",")

    # Appliquer la fonction preprocess_and_predict CSV ==> EN ANGLAIS
    predictions = preprocess_and_predict(df_test)

    # Créer la colonne des prédictions CSV ==> EN ANGLAIS
    df_test["Predictions"] = predictions

    # Enregistrer les prédictions dans un nouveau fichier CSV CSV ==> EN ANGLAIS
    df_test.to_csv(os.path.join(output_folder, input_file), index=False)
    print("Predictions saved")


if __name__ == "__main__":

    # Vérifier si un fichier CSV est fourni en argument
    if len(sys.argv) != 2:
        print("Usage: python main.py input_file.csv")
        sys.exit(1)
    else:
        input_file = sys.argv[1]
        main(input_file)
