import json

def custom_filter(func, iterable_obj):
    print('Custom filter got this iterable_obj', iterable_obj)
    results = []
    for item in iterable_obj:
        res = func(item)
        if res:
            results.append(item)
    return results


def get_products():
    with open('data.json', 'r') as file:
        data = json.loads(file.read())
        products = data['products']
        categories = data['categories']
        for product in products:

            # def category_filter(category):
            #     return category['id'] == product['category']

            category_filter = lambda category: category['id'] == product['category']

            results = custom_filter(category_filter, categories)
            print(results)

        return products
    return []
