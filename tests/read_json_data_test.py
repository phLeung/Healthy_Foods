import unittest
from utils.read_json_data_util import read_json_data, read_from_file
from utils.read_json_data_util import get_json_data, parse_json_data

class ReadJSONDataTest(unittest.TestCase):
    def setUp(self):
        self.error = "error"
        self.daily_harvest = "DailyHarvest"
        self.products = 'products'
        self.ingredients = 'ingredients'

    def test_read_products_json(self):
        self.assertIn('.json',read_from_file(self.products))

    def test_read_products_name(self):
        self.assertIn(self.products,read_from_file(self.products))

    def test_read_ingredients_name(self):
        self.assertIn(self.ingredients,read_from_file(self.ingredients))

    def test_read_ingredients_json(self):
        self.assertIn('.json',read_from_file(self.ingredients))

    def test_read_from_file_against_invalid_input(self):
        self.assertNotIn('invalidinput',read_from_file(self.products))

    def test_read_from_file_against_bad_input(self):
        self.assertNotIn('ingredients and ID',read_from_file(self.products))

    def test_read_from_file_using_products_and_id_input(self):
        self.assertNotIn('products and ID',read_from_file(self.ingredients))

    def test_read_from_products_file_using_ingredients_input(self):
        self.assertNotIn(self.ingredients,read_from_file(self.products))

    def test_read_from_ingredients_file_using_products_input(self):
        self.assertNotIn(self.products,read_from_file(ingredients))

    def test_get_json_data_for_products(self):
        self.assertIn(self.products,get_json_data(self.products))

    def test_get_json_data_for_ingredients(self):
        self.assertIn(self.ingredients,get_json_data(self.ingredients))

    def test_get_json_data_not_none_ingredients(self):
        self.assertIsNotNone(get_json_data(self.ingredients))

    def test_get_json_data_not_none_products(self):
        self.assertIsNotNone(get_json_data(self.products))

    def test_parse_json_data_file_not_found_for_error_input(self):
        self.assertRaises(FileNotFoundError,lambda:parse_json_data(self.error))

    def test_parse_json_data_file_not_found_for_daily_harvest(self):
        self.assertRaises(FileNotFoundError,lambda:parse_json_data(self.daily_harvest))




if __name__ == '__main__':
    unittest.main()
