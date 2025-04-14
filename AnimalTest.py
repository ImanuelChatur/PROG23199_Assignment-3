# Assignment: 3
# Course: PROG23199
# Submission date: 2025-04-13
# Name: Imanuel Chatur
# Sheridan ID: 991637637
# Instructors name: Syed Tanbeer
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
