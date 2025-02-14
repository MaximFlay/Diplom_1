from unittest.mock import Mock
import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    @pytest.fixture
    def setup_burger(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Sesame Bun"
        mock_bun.get_price.return_value = 200

        burger.set_buns(mock_bun)

        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "Ketchup"
        mock_ingredient1.get_price.return_value = 50
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE

        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "Chicken"
        mock_ingredient2.get_price.return_value = 150
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        return burger

    def test_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert len(burger.ingredients) == 0

    def test_set_buns(self, setup_burger):
        burger = setup_burger
        assert burger.bun.get_name() == "Sesame Bun"

    def test_add_ingredient(self, setup_burger):
        burger = setup_burger
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "Mustard"
        mock_ingredient.get_price.return_value = 30
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE

        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 3
        assert burger.ingredients[2].get_name() == "Mustard"

    def test_remove_ingredient(self, setup_burger):
        burger = setup_burger
        assert len(burger.ingredients) == 2
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == "Chicken"

    def test_move_ingredient(self, setup_burger):
        burger = setup_burger
        burger.move_ingredient(0, 1)  # Move Ketchup to index 1
        assert burger.ingredients[1].get_name() == "Ketchup"
        assert burger.ingredients[0].get_name() == "Chicken"

    def test_get_price(self, setup_burger):
        burger = setup_burger
        assert burger.get_price() == (200 * 2) + 50 + 150  # 400 + 50 + 150 = 600

    def test_get_receipt(self, setup_burger):
        burger = setup_burger
        expected_receipt = (
            "(==== Sesame Bun ====)\n"
            "= sauce Ketchup =\n"
            "= filling Chicken =\n"
            "(==== Sesame Bun ====)\n"
            "\n"
            "Price: 600"
        )
        assert burger.get_receipt() == expected_receipt
