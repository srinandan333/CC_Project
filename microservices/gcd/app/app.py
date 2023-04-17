from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api, Resource

class Gcd(Resource): 
	def gcd(a, b):
		while(b):
			a, b = b, a % b
		return {'res': a}

app = Flask(__name__)
api = Api(app)
api.add_resource(Gcd, '/<a>/<b>')

if __name__ =="__main__":
	app.run(debug=True, port=5055, host="0.0.0.0")