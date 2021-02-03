from flask import Flask
from flask import jsonify
import requests
from services.products_service import ProductsService
from services.ingredients_service import IngredientsService
from flask_restful import Resource, Api, abort
#global variables
##############################################################
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False #utf8 support
api = Api(app)
headers = {'Content-type': 'application/json'}
products_service = ProductsService()
ingredients_service = IngredientsService()
INGREDIENTS_DATA = ingredients_service.getIngredientNames()
ingredients_json_path = './data/ingredients.json'
##############################################################

#error handler for invalid ingredient name
#for implementation of rest api
def invalid_ingredient_name(name):
    if name not in INGREDIENTS_DATA:
        abort(404, message="{0} does not exist".format(name))

#handle case where there are no products with the given ingredient name
def no_product_with_matching_ingredient(products,name):
    if len(products) == 0:
        abort(200, message="Could not find products with the given ingredient named {0}.".format(name))

def invalid_json_products():
    if not products_service.valid_products_handler():
        abort(400, message="JSON data for products is invalid")

def invalid_json_ingredients():
    if not ingredients_service.valid_ingriedients_handler():
        abort(400, message="JSON data for ingredients is invalid")

class ProductsWithMatchingIngredient(Resource):
    #issue a get request
    #using the title
    def get(self, name):
        invalid_json_ingredients()
        invalid_json_products()
        if not name:
            product_names = products_service.getProductNames()
            return product_names
        invalid_ingredient_name(name.title())#capitalize every first letter of word after each space of word
        ingredient_name = ingredients_service.getIngredientByName(name.title())["name"]
        product_names = products_service.getMatchedProductsByIngredientName(ingredient_name)
        no_product_with_matching_ingredient(product_names,ingredient_name)
        return jsonify(result=product_names)

    def post(self, name):
        pass


class IngredientNames(Resource):
    def get(self):
        invalid_json_ingredients()
        return INGREDIENTS_DATA

    def post(self,name,id):
        pass



#set up Api resource routing
api.add_resource(IngredientNames,'/api/ingredientnames')
api.add_resource(ProductsWithMatchingIngredient, '/api/ingredientnames/products/search/ingredient/<name>')


if __name__ == '__main__':
    app.run(debug=True)
