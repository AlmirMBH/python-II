# List
food = ['pizza', 'bread', 'eggs', 'veal']

# food[0] = 'sushi'
food.append('sushi')
food.remove('pizza')
food.pop(0)
food.insert(0, 'lamb')

for food in food:
    print(food)

drinks = ['coffee', 'mineral water', 'juice']
dinner = ['salad', 'fish', 'potato']
desserts = ['fruit salad', 'ice-cream', 'cake']

foods = [drinks, dinner, desserts]

for food in foods:
    for meal in food:
        print(meal)
