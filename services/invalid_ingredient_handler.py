#!/usr/bin/python3
class InvalidIngredientNameError(Exception):
    #Raised when ingredient input name is invalid or can't be found within the ingredients json dataset
    """
    ingredient_name -- input ingredient name which caused the error
    message -- explanation of error
    """
    def __init__(self,ingredient_name, message="Ingredient name is invalid or cannot be found"):
        self.ingredient_name = ingredient_name
        self.message = message
        super().__init__(self.message)
