import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.fixture
    def create_bun(self):
        return Bun("Копченая", 1255.1)

    @pytest.mark.parametrize("expected_name", [
        ("black bun"),
        ("white bun"),
        ("red bun")
    ])
    def test_get_name(self, expected_name): # проверка имени булочки
        create_bun = Bun(expected_name,1255.1)
        assert create_bun.get_name() == expected_name

    @pytest.mark.parametrize("expected_price", [
        (100),
        (200),
        (300)
    ])
    def test_get_price(self,expected_price): #проверка цены булочки
        create_bun = Bun("Копченая", expected_price)
        assert create_bun.get_price() == expected_price

    def test_name_type(self,create_bun): #проверка типа имени булочки
        assert isinstance(create_bun.get_name(), str)


    def test_price_type(self, create_bun): #проверка типа цены булочки
        assert isinstance(create_bun.get_price(), float)

