from folder.views import get_products, get_product, get_categories, get_category, create_product, delete_product


def list_of_products():
    products = get_products()
    for product in products:
        print(f"{product['id']}) {product['name']} - ${product['price']} - {product['category']['name']}")


def list_of_categories():
    categories = get_categories()
    for category in categories:
        print(f"{category['id']}) {category['name']}")


def get_product_by_id():
    id = int(input('Enter product ID: '))
    product = get_product(id)
    if product is not None:
        print(f"{product['id']}) {product['name']} - ${product['price']} - {product['category']['name']}")
    else:
        print(f'The product with id {id} doesn\'t exist')


def create_new_product():
    name = input('Enter product name: ')
    price = int(input('Enter product price: '))

    while True:
        print('\n')
        list_of_categories()
        category_id = int(input('\nEnter product category id: '))
        category = get_category(category_id)
        if category is not None:
            break
        print(f'The category with id {category_id} does not exist, enter again!')

    product = create_product(
        name,
        price,
        category_id
    )

    print(f"{product['id']}) {product['name']} - ${product['price']} - {product['category']['name']}. is successfully created")


def delete_product_by_id():
    list_of_products()
    id = int(input('\nEnter product ID: '))
    product = get_product(id)
    if product:
        delete_product(id)
        print(f"The product with ID {id} is deleted successfully")
    else:
        print(f"The product with ID {id} does not exist")


def update_product_by_id():
    list_of_products()
    id = int(input('\nEnter product ID: '))

    product = get_product(id)
    if not product:
        print(f"The product with ID {id} does not exist")

    name = input('Enter product name: ')
    if name:
        product['name'] = name

    price = input('Enter product price: ')
    if price:
       product['price'] = int(price)

    while True:
        print('\n')
        list_of_categories()
        category_id = input('\nEnter product category id: ')
        if category_id == '':
            break
        category = get_category(int(category_id))
        if category is not None:
            product['category'] = category
            break
        print(f'The category with id {category_id} does not exist, enter again!')





