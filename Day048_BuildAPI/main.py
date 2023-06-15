from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, name, test):
        return {"passed string": name, "passed integer": test}
#         my_string = "Hello "+name+"...   "
#         my_string = my_string * test
#         return {"passed string": name, "passed integer": test, "greeting": my_string}

    
    def post(self):
        return {"Hello world": "posted"}

api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")

if __name__ == "__main__":
    app.run(debug=True)
    
    
