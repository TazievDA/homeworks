import os
from operator import itemgetter

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
    cook_book = making_cook_book('recipes.txt')
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for idx in range(len(cook_book[dish])):
                one_dish = cook_book[dish][idx]
                dish_name = one_dish['ingredient_name']
                quantity = one_dish['quantity']
                measure = one_dish['measure']
                if dish_name in shop_list:
                    ingredient_book = {dish_name: {'measure': measure, 'quantity': int(quantity) * person_count * len(dishes)}}
                else:
                    ingredient_book = {dish_name: {'measure': measure, 'quantity': int(quantity) * person_count}}
                shop_list.update(ingredient_book)
            print(shop_list)
        else:
            print('Такого блюда нет.')

get_shop_list_by_dishes(['Омлет'], 2)

# Задача №3

def getting_files_info():
    files = []
    for filename in os.listdir('files for 3rd task'):
        file = os.path.join(os.getcwd(), 'files for 3rd task', filename)
        with open(file, 'r', encoding='UTF-8') as f:
            lines = f.readlines()
            info = {'filename': filename, 'lines_length': len(lines), 'lines': lines}
            files.append(info)
    return files

def sorting_files():
    files_dict = getting_files_info()
    return sorted(files_dict, key=itemgetter('lines_length'))

def writing_new_file():
    with open('merged.txt', 'w', encoding='UTF-8') as m:
        sorted_list = sorting_files()
        for idx, file in enumerate(sorted_list):
            m.write(f"{sorted_list[idx].get('filename')}\n{sorted_list[idx].get('lines_length')}\n{''.join(sorted_list[idx].get('lines'))}\n")

writing_new_file()