pizzaAmount = 1

data = input()
data = data.split()
ingredientAmount = int(data[0])
mismatchPairAmount = int(data[1])

mismatchPairs = {}
for i in range(0, mismatchPairAmount):
    data = input()
    data = data.split()
    ingredientOne = int(data[0])
    ingredientTwo = int(data[1])

    if ingredientOne not in mismatchPairs:
        mismatchPairs[ingredientOne] = [ingredientTwo]
    else:
        mismatchPairs[ingredientOne].append(ingredientTwo) 
    
    if ingredientTwo not in mismatchPairs:
        mismatchPairs[ingredientTwo] = [ingredientOne]
    else:
        mismatchPairs[ingredientTwo].append(ingredientOne)
def validatePizza(current_ingredients, ingredient_index):
    activeIngredientIndexes = [index for index, value in enumerate(current_ingredients) if value == 1]
    for i in activeIngredientIndexes:
        if ingredient_index + 1 in mismatchPairs and i+1 in mismatchPairs[ingredient_index + 1]:
            return False
    return True

def makePizza(current_ingredients, ingredient_index):
    global pizzaAmount
    if ingredient_index == ingredientAmount:
        return True
   
    if validatePizza(current_ingredients, ingredient_index):
        pizzaAmount += 1
        current_ingredients[ingredient_index] = 1
        makePizza(current_ingredients, ingredient_index+1)
    current_ingredients[ingredient_index] = 0
    makePizza(current_ingredients, ingredient_index+1)

makePizza([0] * ingredientAmount, 0)
print(pizzaAmount)
