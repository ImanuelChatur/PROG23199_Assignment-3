class Animal:
    def __init__(self, name, required_food):
        self.name = name
        self.required_food = required_food
        self.hungry_count = 0
        self.food_consumed = 0
        self.feed_count = 0

    def __str__(self):
        return (f"{self.name} got hungry {self.hungry_count} time(s),"
                f" fed {self.feed_count} time(s) and"
                f" consumed {self.food_consumed} Kg food")

    def get_name(self):
        return self.name

    def get_hungry_count(self):
        return self.hungry_count

    def get_required_food(self):
        return self.required_food

    def get_feed_count(self):
        return self.feed_count

    def set_feeding_count(self, feeding_count):
        self.feed_count = feeding_count

    def set_hungry_count(self):
        self.hungry_count += 1

    def calculate_food_consumed(self):
        pass
