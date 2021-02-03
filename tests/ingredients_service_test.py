import unittest
from services.ingredients_service import IngredientsService
#global variable
###############################################
ingredients_service = IngredientsService()
###############################################
class IngredientsServiceTest(unittest.TestCase):
    def setUp(self):
        self.error = "invalid data"
        self.maple = "Maple"
        self.beef = "BeefStuff1"

    def test_get_ingredient_names_not_empty(self):
        ingredient_names = ingredients_service.getIngredientNames()
        self.assertNotEqual(len(ingredient_names),0)

    def test_get_ingredient_names_not_none(self):
        ingredient_names = ingredients_service.getIngredientNames()
        self.assertIsNotNone(ingredient_names)

    def test_get_ingredient_by_name_is_none(self):
        self.assertIsNone(ingredients_service.getIngredientByName(self.error))

    def test_get_ingredient_by_name_against_maple_input(self):
        self.assertIsInstance(ingredients_service.getIngredientByName(self.maple),dict)

    def test_get_ingredient_by_name_against_beef_input(self):
        self.assertIsNone(ingredients_service.getIngredientByName(self.beef))

if __name__ == '__main__':
    unittest.main()
