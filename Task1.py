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
    pprint(cook_book)

recipe('data.txt')
