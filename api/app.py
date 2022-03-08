from flask import Flask
from flask_restful import Resource, Api
import pandas as pd
from joblib import  load
import json
import requests


app = Flask(__name__)
api = Api(app)

class CaracteristicasRiesgo(Resource):
    def get(self, user_id):
        
        df = pd.read_csv('../data/output/train_model.csv')
        
        resultado = df[df.id==int(user_id)]
        resultado.sort_values('nb_previous_loans',ascending=False,inplace=True)
        #id,age,years_on_the_job,nb_previous_loans,avg_amount_loans_previous,flag_own_car,status
        resultado=resultado.iloc[0,[3,4,1,2,5]].to_json()
        resultado = json.loads(resultado)

        return resultado

class Prediccion(Resource):
    def post(self, user_id):

        my_model = load('../train_models/model_risk.joblib') 

        url = 'http://127.0.0.1:5000/api/user/' + user_id + '/caracteristicasriesgo'
        r = requests.get(url)
        camposresult = r.json()
        
        d = {str(user_id): [camposresult['nb_previous_loans'], camposresult['avg_amount_loans_previous'], camposresult['age'],camposresult['years_on_the_job'],camposresult['flag_own_car']]}
        
        resultado = my_model.predict([d[user_id]])
        
        lists = resultado.tolist()
        json_str = json.dumps(lists)

        return {'resultado': json.loads(json_str) }

api.add_resource(CaracteristicasRiesgo, '/api/user/<string:user_id>/caracteristicasriesgo')
api.add_resource(Prediccion, '/api/user/<string:user_id>/prediccion')
if __name__ == '__main__':
    app.run(debug=False)