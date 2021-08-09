from datetime import datetime

class FoodDiary:
    """
    This class will contain all methods associated with the food diary,
    including the control of foods being added and removed, the returning of requested valeus
    reading the food database ect
    """

    def __init__(self):
        self.diary = []

    def add(self, food=None, amount=1, type=1):
        self.diary.append({"food": Food(food),
                           "time": datetime.now().strftime("%H:%M"),
                           "portion": Portion(food,amount, type)
                           })


class Food:
    def __init__(self, food):
        self.food = food

# class Portion:
#     def __init__(self, food, amount, ptype):
#         self.food = food
#         self.amount = amount



