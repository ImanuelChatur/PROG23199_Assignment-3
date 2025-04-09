class Animal:
    def __init__(self, name, required_food):
        self.name = name
        self.required_food = required_food
        self.hungry_count = 0
        self.food_consumed = 0

    def get_name(self):
        return self.name

    def get_required_food(self):
        return self.required_food

    def set_feeding_count(self, feeding_count):
        pass

    def set_hungry_count(self):
        self.hungry_count += 1

    def calculate_food_consumed(self):
        pass
