# Задача №1.
def making_cook_book(file):
    with open(file, 'r', encoding='UTF-8') as f:
        cook_book = {}
        for line in f:
            receipe_name = line.strip()
            ingredients_count = f.readline()
            ingredients = []
            for _ in range(int(ingredients_count)):
                receipe = f.readline().strip().split(' | ')
                ingredient_name, quantity, measure = receipe
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            f.readline()
            cook_book[receipe_name] = ingredients
    return cook_book


# Задача №2.
def get_shop_list_by_dishes(dishes, person_count):
    ingredients_book = {}
    for dish in dishes:
        if dish in cook_book:
            for idx in range(len(cook_book[dish])):
                one_dish = cook_book[dish][idx]
                dish_name = one_dish['ingredient_name']
                quantity = one_dish['quantity']
                measure = one_dish['measure']
                if dish_name in ingredients_book:
                    ingredient_book = {dish_name: {'measure': measure, 'quantity': int(quantity) * person_count * len(dishes)}}
                else:
                    ingredient_book = {dish_name: {'measure': measure, 'quantity': int(quantity) * person_count}}
                ingredients_book.update(ingredient_book)
            print(ingredients_book)
        else:
            print('Такого блюда нет.')

cook_book = making_cook_book('recipes.txt')

get_shop_list_by_dishes(['Омлет'], 2)

# Задача №3

