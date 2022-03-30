from pprint import pprint


def recipe(file_name: str):
    cook_book = {}
    with open(file_name) as file:
        for string in file:
            if "|" not in string and len(string) > 3:
                quantity = int(file.readline())
                cook_book[string.split('\n')[0]] = []
                for ingr in range(quantity):
                    ingr = file.readline().split('|')
                    cook_book[string.split('\n')[0]].append(dict([
                        ('ingredients_name', ingr[0]),
                        ('quantity', int(ingr[1])),
                        ('measure', ingr[2].split('\n')[0])
                    ]))
    return cook_book


recipe('data.txt')


def ingredients(dishes: list, person: int):
    cook_book = recipe('data.txt')
    result = {}
    for keys in dishes:
        if keys in cook_book:
            menu = cook_book[keys]
            for i in range(0, len(menu)):
                result[menu[i].get('ingredients_name')] = dict(
                    [('quantity', menu[i].get('quantity') * person), ('measure', menu[i].get('measure'))])
    pprint(result)


ingredients(['Омлет', 'Утка по-пекински'], 3)
