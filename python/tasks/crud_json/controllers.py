from folder.views import get_products


def list_of_products():
    products = get_products()
    for product in products:
        pass
        # print('\t', product)
