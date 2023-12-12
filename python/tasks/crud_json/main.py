# import folder.views as views
# from folder import views as v
from controllers import list_of_products

option_messages = '''

    Welcome!
    Select option:
        1. List of products
        2. Get the product by id
        3. Create new product
        4. Edit the product by id
        5. Delete the product by id
        6. Exit

'''


def bootstrap():
    while True:
        option = int(input(option_messages))
        if option == 1:
            list_of_products()

        elif option == 2:
            list_of_products()

        elif option == 3:
            list_of_products()

        elif option == 4:
            list_of_products()

        elif option == 5:
            list_of_products()

        else:
            print('Good bye!')
            break


if __name__ == '__main__':
    bootstrap()
