from mamba import description, context, it
from main.classes.day_tracker import Day
from expects import expect, equal

with description("A day tracker") as self:
    with context("weight"):
        with it("stores the weight when add_weight is called"):
            day = Day()
            day.add_weight(100)
            expect(day.weight).to(equal(100))
    with context("Food Diary"):
        day = Day()
        expect(day.food_diary).to(equal([]))