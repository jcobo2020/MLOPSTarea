from flask import Flask
from flask_restful import Resource, Api
import json
import requests
from singleton import singleton

app = Flask(__name__)
api = Api(app)



class CaracteristicasRiesgo(Resource):
    def get(self, user_id):
        
        df = singleton.model_train
        
        resultado = df[df.id==int(user_id)]
        resultado.sort_values('nb_previous_loans',ascending=False,inplace=True)
        #id,age,years_on_the_job,nb_previous_loans,avg_amount_loans_previous,flag_own_car,status
        #devuelve un solo registro en base a nb_previous_loans el mayor valor 
        resultado=resultado.iloc[0,[3,4,1,2,5]].to_json()
        resultado = json.loads(resultado)

        return resultado

class Prediccion(Resource):
    def get(self, user_id):

        url = 'http://127.0.0.1:5001/api/user/' + user_id + '/caracteristicasriesgo'
        r = requests.get(url)
        camposresult = r.json()
        
        #armar el diccionario del user_id 
        d = {str(user_id): [camposresult['nb_previous_loans'], 
            camposresult['avg_amount_loans_previous'], camposresult['age'],camposresult['years_on_the_job'],
            camposresult['flag_own_car']]}
        
        resultado = singleton.modelo.predict([d[user_id]])
        
        lists = resultado.tolist()
        json_str = json.dumps(lists)

        return {'resultado': json.loads(json_str) }

api.add_resource(CaracteristicasRiesgo, '/api/user/<string:user_id>/caracteristicasriesgo')
api.add_resource(Prediccion, '/api/user/<string:user_id>/prediccion')

if __name__ == '__main__': 
    app.run(debug=False, host='0.0.0.0', port=5001)