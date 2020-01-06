import contextmanager as cm

cook_book = {}


def split_ingredient(ingredient):
    _ingredient = {}
    _res = ingredient.split(' | ')
    _ingredient['ingredient_name'] = _res[0]
    _ingredient['quantity'] = _res[1]
    _ingredient['measure'] = _res[2]
    return _ingredient


with cm.CustomCM('recipes.txt') as f:
    dish, dish_number = None, 0
    ingredients, ingredients_number = [], None
    ingredients_use = 0

    for i, line in enumerate(f):
        line = line.strip()
        if i == dish_number:
            dish = line
        elif i == (dish_number + 1):
            ingredients_number = int(line)
            dish_number = ingredients_number + i + 2
        else:
            if line and (ingredients_use != ingredients_number):
                res = split_ingredient(line)
                ingredients.append(res)
                ingredients_use = ingredients_use + 1
            if ingredients_use == ingredients_number:
                cook_book[dish] = ingredients
                ingredients_use = 0
                ingredients = []


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_list = {}
    for _dish in dishes:
        for ingredient in cook_book[_dish]:
            if ingredient.get('ingredient_name') in ingredients_list:
                duplicate_ingredient = ingredients_list.get(ingredient.get('ingredient_name'))
                _quantity = duplicate_ingredient.get('quantity') + int(ingredient.get('quantity')) * person_count
            else:
                _quantity = int(ingredient.get('quantity')) * person_count

            item = dict(measure=ingredient.get('measure'),
                        quantity=_quantity)
            ingredients_list[ingredient.get('ingredient_name')] = item

    print(ingredients_list)


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
