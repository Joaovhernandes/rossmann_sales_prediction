import os
import pickle
import pandas as pd
from flask import Flask, request, Response

from rossmann.Rossmann import Rossmann

# Carregando o modelo
model = pickle.load(
    open('model/model_rossman.pkl', 'rb'))

# Inicializando a API
app = Flask(__name__)


@app.route('/rossmann/predict', methods=['POST'])
def rossman_predict():
    test_json = request.get_json()

    if test_json:  # Se houver dados

        if isinstance(test_json, dict):  # Único exemplo
            test_raw = pd.DataFrame(test_json, index=0)

        else:  # Multiplos exemplos
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        # Instanciando a classe Rossmann
        pipeline = Rossmann()

        # Data Cleaning
        df1 = pipeline.data_cleaning(test_raw)

        # Feature Engineering
        df2 = pipeline.feature_engineering(df1)

        # Data Preparation
        df3 = pipeline.data_preparation(df2)

        # Prediction
        df_response = pipeline.get_prediction(model, test_raw, df3)

        return df_response



    else:
        return Response('{}', status=200, mimetype='application/json')


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)