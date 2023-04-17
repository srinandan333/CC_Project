from flask import Flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api, Resource

class Lcm(Resource):
	def get(a, b):
		if a == 0 or b == 0:
			return 0
		max_num = max(a, b)
		while True:
			if max_num % a == 0 and max_num % b == 0:
				lcm = max_num
				break
			max_num += 1
		return {'res': lcm}

app = Flask(__name__)
api = Api(app)
api.add_resource(Lcm, '/<a>/<b>')

if __name__ =="__main__":
		app.run(debug=True, port=5056, host="0.0.0.0")