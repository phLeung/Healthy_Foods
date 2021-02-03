from utils.read_json_data_util import read_json_data
from utils.read_json_data_util import json_validator
from .invalid_ingredient_handler import InvalidIngredientNameError
class IngredientsService:
    def __init__(self,json_data=read_json_data('ingredients')):
        self.ingredients = json_data

    def _getIngredients(self):
        return self.ingredients

    def valid_ingriedients_handler(self):
        return json_validator('ingredients')

    def getIngredientNames(self):
        ingredients_data = self._getIngredients()
        data_length = len(ingredients_data)
        ingredient_names = [ingredients_data[i]["name"] for i in range(data_length)]
        return ingredient_names

    #get the ingredient by name and return the dictionary object
    #of the ingredient by name
    def getIngredientByName(self,name):
        if not isinstance(name,str):
            raise InvalidIngredientNameError(name)
        data_length = len(self.ingredients)
        try:
            for i in range(data_length):
                if self.ingredients[i]["name"] == name:
                    return self.ingredients[i]
        except InvalidIngredientNameError as invalid_ingredient:
            print(invalid_ingredient)
