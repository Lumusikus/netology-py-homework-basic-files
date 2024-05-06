# задание 1
cook_book = {}
with open('recipies.txt', 'r', encoding='utf-8') as f:
    file_lines = f.readlines()
index = 0
while index < len(file_lines):
    dish = file_lines[index].strip() # название блюда
    index += 1
    ingridients_count = int(file_lines[index].strip()) # количество ингридиентов
    ingridients = []
    for _ in range(ingridients_count):
        index += 1
        ingr_data = file_lines[index].strip() # строка с описанием ингридиента
        parts = ingr_data.split(' | ')
        ingr_dict = {'ingredient_name': parts[0], 'quantity': int(parts[1]), 'measure': parts[2]}
        ingridients.append(ingr_dict)
    cook_book[dish] = ingridients
    index += 2 # пропус строки-разделителя
for k,v in cook_book.items():
    print(k, ':', v)
print()

# задание 2
def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book.keys(): # если блюдо есть в рецептах
            recipe = cook_book[dish] # список словарей с ингредиентами
            for ingridient in recipe:
                name = ingridient['ingredient_name']
                measure = ingridient['measure']
                quantity = ingridient['quantity'] * person_count
                result[name] = {'measure' : measure, 'quantity' : quantity}
    return result

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
for k,v in shop_list.items():
    print(k, ':', v)
print()