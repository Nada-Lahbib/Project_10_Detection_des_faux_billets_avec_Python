import joblib  # Pour les anciennes versions de scikit-learn
import pandas as pd
import sys
import os

# Importer model_1, scaler_1, model_2, scaler_2 et predict_with_threshold depuis les fichiers sauvegardés
model_1 = joblib.load('notebooks/model_1.pkl')
scaler_1 = joblib.load('notebooks/scaler_1.pkl')
scaler_2 = joblib.load('notebooks/scaler_2.pkl')
best_model = joblib.load('notebooks/best_model.pkl')

# Créer une fonction de prédiction personnalisée
def predict_with_threshold(X):
    # Prédire les probabilités
    y_proba = best_model.predict_proba(X)
    # Appliquer le seuil personnalisé pour obtenir les classes prédites
    y_pred = (y_proba[:, 1] > 0.26).astype(int)
    return y_pred

# Définir la fonction preprocess_and_predict
def preprocess_and_predict(df_test):
    # Vérifier les valeurs manquantes dans la colonne 'margin_low'
    null_indices = df_test['margin_low'].isnull()
    
    # Remplacer les valeurs manquantes dans la colonne 'margin_low' avec les prédictions de model_1 si nécessaire
    if null_indices.any():
        df_test.loc[null_indices, 'margin_low'] = model_1.predict(scaler_1.transform(df_test.loc[null_indices, ['diagonal', 'height_left', 'height_right', 'margin_up', 'length']]))
    
    # Appliquer scaler_2 sur les caractéristiques
    scaled_features = scaler_2.transform(df_test[['diagonal', 'height_left', 'height_right', 'margin_low', 'margin_up', 'length']])
    
    # Faire des prédictions en utilisant model_2
    predictions = predict_with_threshold(scaled_features)
    
    return predictions