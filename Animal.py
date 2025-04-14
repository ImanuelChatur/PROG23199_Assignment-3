# Assignment: 3
# Course: PROG23199
# Submission date: 2025-04-13
# Name: Imanuel Chatur
# Sheridan ID: 991637637
# Instructors name: Syed Tanbeer
class Animal:
    """
    Description:
        This class has functionalities for the Animal class

    Methods:
        get_name():
            returns name
        get_hungry_count():
            returns hungry count
        get_required_food():
            returns required food
        get_feed_count():
            returns feed count
        set_feeding_count():
            set feeding count
        set_hungry_count():
            set hungry count
        calculate_food_consumed():
            calculates food consumed
    """
    def __init__(self, name, required_food):
        """
        Initialize Animal Class
        :param name: Name of animal
        :param required_food: How much food it needs to eat to be fed
        """
        self.name = name
        self.required_food = required_food
        self.hungry_count = 0
        self.food_consumed = 0
        self.feed_count = 0

    def __str__(self):
        """
        Return Animal as formatted String
        :return: Animal as a string
        """
        return (f"{self.name} got hungry {self.hungry_count} time(s),"
                f" fed {self.feed_count} time(s) and"
                f" consumed {self.calculate_food_consumed()} Kg food")

    def get_name(self):
        """
        Get name
        :return: Name (str)
        """
        return self.name

    def get_hungry_count(self):
        """
        Get hungry count

        :return: hungry_count (int)
        """
        return self.hungry_count

    def get_required_food(self):
        """
        Get required food amount
        :return: required_food (int)
        """
        return self.required_food

    def get_feed_count(self):
        """
        get feed count
        :return: feed_count (int)
        """
        return self.feed_count

    def set_feeding_count(self, feeding_count):
        """
        Set feeding count
        :param feeding_count: feed count (int)
        """
        self.feed_count = feeding_count

    def set_hungry_count(self, hungry_count):
        """
        Set hungry count
        :param hungry_count: hungry count (int)
        """
        self.hungry_count = hungry_count

    def calculate_food_consumed(self):
        """
        Calculate food consumed in KGs
        :return: times fed times food required
        """
        return self.feed_count * self.required_food
