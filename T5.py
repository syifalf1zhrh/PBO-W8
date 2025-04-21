from collections import namedtuple

mealpreapp = namedtuple('mealpreapp', ['meal', 'prep_time', 'servings', 'calories'])

mealpreapp1 = mealpreapp(
    meal='Ayam Kukus Jahe',
    prep_time=30,
    servings=4,
    calories=400
)

mealpreapp2 = mealpreapp(
    meal='Overnight Oats',
    prep_time=20,
    servings=5,
    calories=300
)

print("This Week's Meal Prep Plan")
print("=====================================\n")

print(f"Meal 1: {mealpreapp1.meal}")
print(f"  Prep Time: {mealpreapp1.prep_time} minutes")
print(f"  Servings: {mealpreapp1.servings}")
print(f"  Calories: {mealpreapp1.calories}\n")

print(f"Meal 2: {mealpreapp2.meal}")
print(f"  Prep Time: {mealpreapp2.prep_time} minutes")
print(f"  Servings: {mealpreapp2.servings}")
print(f"  Calories: {mealpreapp2.calories}")

print("\nBy Syifa")