import json


def get_products():
    with open('data.json', 'r') as file:
        data = json.loads(file.read())
        products = data['products']
        categories = data['categories']
        for product in products:
            results = list(filter(lambda category: category['id'] == product['category'], categories))
            product['category'] = results[0]

        return products
    return []


def get_product(id):
    with open('data.json', 'r') as file:
        data = json.loads(file.read())
        products = data['products']
        categories = data['categories']
        for product in products:
            if product['id'] == id:
                results = list(filter(lambda category: category['id'] == product['category'], categories))
                product['category'] = results[0]
                return product

        return None


def get_categories():
    with open('data.json', 'r') as file:
        data = json.loads(file.read())
        return data['categories']
    return []


def get_category(id):
    with open('data.json', 'r') as file:
        data = json.loads(file.read())
        categories = data['categories']
        results = list(filter(lambda category: category['id'] == id, categories))
        if len(results) > 0:
            return results[0]
    return None


def create_product(name, price, category_id):
    with open('data.json', 'r') as file:
        data = json.loads(file.read())
        products = data['products']
        product = {
            'id': products[-1]['id'] + 1,
            'name': name,
            'price': price,
            'category': category_id
        }
        products.append(product)

        with open('data.json', 'w') as file_for_write:
            data['products'] = products
            file_for_write.write(json.dumps(data))

        product['category'] = get_category(category_id)
        return product


def delete_product(id):
    with open('data.json', 'r') as file:
        data = json.loads(file.read())
        products = data['products']
        with open('data.json', 'w') as file_for_write:
            data['products'] = list(filter(lambda product: product['id'] != id, products))
            file_for_write.write(json.dumps(data))

