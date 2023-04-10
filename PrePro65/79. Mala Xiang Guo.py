'''food'''

def mala():
    '''mala'''
    food = ["celery stalks", "carrots", "potatoes", "mushrooms", "tofu", "lotus root", "cabbage", \
    "instant noodles", "glass noodle", "wonton", "beef", "pork loin", "chicken", "fish balls", \
    "cheese ball", "octopus", "fish", "shrimp", "mussels", "1", "2", "3", "4"]
    ingredient = []
    level = ["1", "2", "3", "4"]
    inp = input().lower()
    while inp != "stop":
        ingredient.append(inp)
        inp = input().lower()
    for i in range(len(ingredient)):
        if ingredient[i] not in food:
            print("Get out!")
            return
        if ingredient[i] in level and ingredient[i - 1] in level and ingredient[0] not in level:
            print("Please choose a spicy level!")
            return
    if len(ingredient) == 0 or (ingredient[0] in level and len(ingredient) == 1):
        print("Huh? you didn't order anything!")
        return
    if ingredient[-1] not in level:
        print("Please choose a spicy level!")
    else:
        if ingredient[-1] == "1":
            print("Mild Mala xiang guo is here.")
        elif ingredient[-1] == "2":
            print("Medium Mala xiang guo is here.")
        elif ingredient[-1] == "3":
            print("Hot Mala xiang guo is here.")
        elif ingredient[-1] == "4":
            print("Extra hot Mala xiang guo is here.")
mala()
