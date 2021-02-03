#!/usr/bin/python3
#command line solution
from services.products_service import ProductsService
from services.ingredients_service import IngredientsService
from services.invalid_ingredient_handler import InvalidIngredientNameError
#global variables
####################################################
ingredients = IngredientsService()
INGREDIENTS_DATA = ingredients.getIngredientNames()
####################################################

def invalid_ingredient_error(name):
    if name not in INGREDIENTS_DATA:
        raise InvalidIngredientNameError(name)

def matching_products_exist(products):
    if len(products) != 0:
        return True
    else:
        return False
def main():
    products_service = ProductsService()
    ingredient_name = input("Enter an ingredient name: ")
    invalid_ingredient_error(ingredient_name.title())
    matched_products = products_service.getMatchedProductsByIngredientName(ingredient_name.title())
    if not matching_products_exist(matched_products):
        print("Could not find products with given ingredient")
    else:
        print("Products with designated ingredient name: {0}".format(matched_products))

if __name__ == '__main__':
    main()
