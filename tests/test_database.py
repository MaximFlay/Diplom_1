import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    @pytest.fixture
    def menu(self):
        return Database()

    def test_initialization_buns(self, menu):
        assert len(menu.buns) == 3
        assert menu.buns[0].get_name() == "black bun"
        assert menu.buns[1].get_name() == "white bun"
        assert menu.buns[2].get_name() == "red bun"
        assert menu.buns[0].get_price() == 100
        assert menu.buns[1].get_price() == 200
        assert menu.buns[2].get_price() == 300

    def test_initialization_ingredients(self, menu):
        assert len(menu.ingredients) == 6

        assert menu.ingredients[0].get_name() == "hot sauce"
        assert menu.ingredients[1].get_name() == "sour cream"
        assert menu.ingredients[2].get_name() == "chili sauce"

        assert menu.ingredients[3].get_name() == "cutlet"
        assert menu.ingredients[4].get_name() == "dinosaur"
        assert menu.ingredients[5].get_name() == "sausage"

        assert menu.ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert menu.ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert menu.ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE

        assert menu.ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert menu.ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert menu.ingredients[5].get_type() == INGREDIENT_TYPE_FILLING

    def test_available_buns(self, menu):
        buns = menu.available_buns()
        assert len(buns) == 3

    def test_available_ingredients(self, menu):
        ingredients = menu.available_ingredients()
        assert len(ingredients) == 6