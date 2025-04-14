import pytest
from Animal import Animal

a = Animal("Giraffe", 10)


def test_calculate_food_consumed():
    food_count = 10
    a.set_feeding_count(10)
    print(a.calculate_food_consumed())

    assert a.calculate_food_consumed() == food_count * a.get_required_food()


@pytest.mark.skip
def test_calculate_food_consumed():
    food_count = 10
    a.set_feeding_count(10)
    print(a.calculate_food_consumed())

    assert a.calculate_food_consumed() == food_count * a.get_required_food()
