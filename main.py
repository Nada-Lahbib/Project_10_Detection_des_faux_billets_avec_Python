import joblib  # Pour les anciennes versions de scikit-learn
import pandas as pd
import sys
import os

from functions import preprocess_and_predict

def main(input_file):
    # Charger le fichier CSV
    input_folder = "data/source/"
    output_folder = "data/output/"
    df_test = pd.read_csv(os.path.join(input_folder, input_file), sep=',')

    # Appliquer la fonction preprocess_and_predict
    predictions = preprocess_and_predict(df_test)

    # Créer la colonne des prédictions
    df_test['Predictions'] = predictions

    # Enregistrer les prédictions dans un nouveau fichier CSV
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
