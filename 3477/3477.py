""" Pad Thai """
ingredients = set()
tastes = set()
allowed = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
    "Bean Sprouts", "Noodle", "Chives", "Lime", "Egg",
    "Oil", "Peanuts"
}

while True:
    s = input()
    if s == "Cook":
        break
    ingredients.add(s)

while True:
    s = input()
    if s == "End":
        break
    tastes.add(s)

if not ingredients.issubset(allowed):
    print("This is not Pad Thai!!!")
elif ingredients != allowed:
    print("This is bad!")
elif tastes == {"Sweet", "Sour", "Salty"}:
    print("Delicious!")
else:
    print("Not Bad...")
