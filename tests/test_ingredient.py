import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:
    def test_ingredient_creation(self): #Проверка создания инградиента
        ingredient = Ingredient('SAUCE','Spicy-X',90.0)
        assert ingredient.type == 'SAUCE'
        assert ingredient.name == 'Spicy-X'
        assert ingredient.price == 90.0

    def test_ingredient_get_price(self):
        ingredient = Ingredient('FILLING','meat',988.0)
        assert ingredient.get_price() == 988.0

    def test_ingredient_ingredient_get_name(self):
        ingredient = Ingredient('SAUCE','Space Sause', 80.0)
        assert ingredient.get_price() == 80.0

    def test_ingredient_ingredient_get_type(self):
        ingredient = Ingredient('FILLING', 'Spicy-X', 88.0)
        assert ingredient.get_type() == 'FILLING'