from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json
from ntuity.ntuityprac import *

app = Flask(__name__)
api=Api(app)

class Kamau(Resource):

    def post(self):
        jsonval=request.get_json()
        content=jsonval.get("number")
        sum=10*content
        bestie=["welcome", 525, "kiza"]
        return jsonify({"sum":sum,"kenya":bestie})

class Kithome(Resource):
    p=NtuityPrac()
    getval=p.get_square
    getsum=p.get_sum

    filename = 'housecsv.csv'
    def post(self):
        jsonval = request.get_json()
        content = jsonval.get("number")
        get_add=self.getsum(content)
        get_sum=self.getval(content)
        return jsonify({"square":get_sum, "sum":get_add})


api.add_resource(Kamau,'/kama')
api.add_resource(Kithome,'/kithome')
if __name__ == '__main__':
    app.run()
