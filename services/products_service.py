from utils.read_json_data_util import read_json_data
from utils.read_json_data_util import json_validator
from .ingredients_service import IngredientsService
from .invalid_ingredient_handler import InvalidIngredientNameError
class ProductsService:
    def __init__(self,json_data=read_json_data('products')):
        self.products = json_data

    def valid_products_handler(self):
        return json_validator('products')

    def _getMatchedProductsByIngredientId(self,matching_id):
        if not isinstance(matching_id,int):
            raise TypeError("ID number should be an integer")
        data_length = len(self.products)
        matching_products = [self.products[i]["name"] for i in range(data_length) if matching_id in self.products[i]["ingredientIds"]]
        return matching_products

    def getProductNames(self):
        data_length = len(self.products)
        product_names = [self.products[i]["name"] for i in range(data_length)]
        return product_names

    def getMatchedProductsByIngredientName(self,name):
        if not isinstance(name,str):
            raise InvalidIngredientNameError(name)
        ingredient = IngredientsService()
        ingredient_name = ingredient.getIngredientByName(name)
        if not ingredient_name:
            raise InvalidIngredientNameError(name)
        return self._getMatchedProductsByIngredientId(ingredient_name["id"])
