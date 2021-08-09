from main.classes.FoodDiary import FoodDiary, Food
from mamba import description, it, context
from expects import expect, equal
from datetime import datetime

with description("The food diary") as self:
    with it("should initialise an empty list when created"):
        food_diary = FoodDiary()
        expect(food_diary.diary).to(equal([]))

    with it("should add a food entry to the food diary when add_food is called"):
        food_diary = FoodDiary()
        food_diary.add("Chips")
        expect(food_diary.diary[0]["food"].food).to(equal("Chips"))

    with it("should return the time that the entry was added at"):
        food_diary = FoodDiary()
        food_diary.add("Chips")
        now = datetime.now()
        expect(food_diary.diary[0]["time"]).to(equal(now.strftime("%H:%M")))

#with description("The Individual food entry"):
