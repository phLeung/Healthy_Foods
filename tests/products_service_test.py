import unittest
from services.products_service import ProductsService
from services.invalid_ingredient_handler import InvalidIngredientNameError

#global variable
#####################################
products_service = ProductsService()
#####################################
class ProductsServiceTest(unittest.TestCase):
    def setUp(self):
        self.maple = "Maple"
        self.organic_banana = "Organic Banana"
        self.tomato2 = "Tomato2"
        self.meat_ingredient = "MeatIngredient"
        self.beef_ingredient = "BeefIngredient"
        self.ingredient_error = "error"
        self.beef_stuff = "BeefStuff"
        self.meat_stuff = "MeatStuff"

    def test_get_matched_products_by_ingredient_name_against_maple_input(self):
        self.assertIsNotNone(products_service.getMatchedProductsByIngredientName(self.maple))

    def test_invalid_ingredient_name_error_against_meat_ingredient(self):
        self.assertRaises(InvalidIngredientNameError,lambda:products_service.getMatchedProductsByIngredientName(self.meat_ingredient))

    def test_get_matched_products_by_ingredient_name_against_orgranic_banana(self):
        self.assertIsInstance(products_service.getMatchedProductsByIngredientName(self.organic_banana),list)

    #unit test for no matching products with given ingredient name
    def test_no_matching_product_with_ingredient_name(self):
        self.assertEqual(len(products_service.getMatchedProductsByIngredientName(self.tomato2)),0)

    def test_invalid_ingredient_name_error_against_beef_ingredient(self):
        self.assertRaises(InvalidIngredientNameError,lambda:products_service.getMatchedProductsByIngredientName(self.beef_ingredient))

    def test_invalid_ingredient_name_error_against_ingredient_error(self):
        self.assertRaises(InvalidIngredientNameError,lambda:products_service.getMatchedProductsByIngredientName(self.ingredient_error))

    def test_invalid_ingredient_name_error_against_beef_stuff(self):
        self.assertRaises(InvalidIngredientNameError,lambda:products_service.getMatchedProductsByIngredientName(self.beef_stuff))

    def test_invalid_ingredient_name_error_against_meat_stuff(self):
        self.assertRaises(InvalidIngredientNameError,lambda:products_service.getMatchedProductsByIngredientName(self.meat_stuff))


if __name__ == '__main__':
    unittest.main()
