"""Ce fichier main.py contient le point d'entrée principal de l'application, chargement d'un fichier CSV, traitement des données et enregistrement des prédictions."""

import os
import sys

import joblib
import pandas as pd

from src.functions import preprocess_and_predict



def main(input_file):
    """
    Main function to process CSV file, make predictions, and save results.

    Parameters:
        input_file (str): The name of the CSV file to process.
    """

    # Define input and output folders
    input_folder = "data/source/"
    output_folder = "data/output/"

    df_test = pd.read_csv(os.path.join(input_folder, input_file), sep=",")

    # Application of the function preprocess_and_predict
    predictions = preprocess_and_predict(df_test)

    # Create the column of the prediction
    df_test["Predictions"] = predictions

    # Save the predictions to a new CSV file
    df_test.to_csv(os.path.join(output_folder, input_file), index=False)
    print("Predictions saved")


if __name__ == "__main__":

    # Check if a CSV file is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python main.py input_file.csv")
        sys.exit(1)
    else:
        input_file = sys.argv[1]
        main(input_file)
