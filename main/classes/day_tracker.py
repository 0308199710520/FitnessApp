

class Day:
    def __init__(self):
        self.weight = None
        self.food_diary = FoodDiary()
        pass
    def add_weight(self, weight):
        self.weight = weight