recipe = {
    "flour": 500,
    "sugar": 200,
    "eggs": 3,
    "milk": 100,
    "vanilla": 5
}

pantry = {
    "flour": 400,       # We have some, but not enough (need 100 more)
    "eggs": 10,         # We have plenty (need 0)
    "milk": 100,        # We have exact amount (need 0)
    # sugar is missing completely (need 200)
    # vanilla is missing completely (need 5)
}
def recipe_gen(recipe, pantry):
    shopping_list = {}
    for item, amount in recipe.items():
    
        if item not in pantry:
            shopping_list[item] = amount
        elif recipe[item] > pantry[item]:
            shopping_list[item] = recipe[item] - pantry[item]
        
    for item2, amount in shopping_list.items():
        print(f"{item2}: {amount}")
recipe_gen(recipe, pantry)


    