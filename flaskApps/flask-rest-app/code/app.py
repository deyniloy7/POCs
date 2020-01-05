from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'secret'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item is not None else 404
    
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'error': 'Item with name "{}" alrady exists'.format(name)}, 400
        data = request.get_json()
        if data == None:
            return {'error': 'Request Body Not Valid/ Not Found'}, 400
        item = {
            'name': name,
            'price': data['price']
        }
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return { 'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(debug=True)
