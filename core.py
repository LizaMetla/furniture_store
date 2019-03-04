def get_worker():
    worker = {
        "id": None,
        "first_n": None,
        "last_n": None,
        "middle_n": None,
        "individual_position": None,
        "tel_number": None,
    }
    return worker


def get_product():
    product = {
        "id": None,
        "department": None,
        "name": None,
        "product_price": None,
    }
    return product


def get_workers_position():
    workers_position = {
        "position_id": None,
        "position": None,
        "salary": None,

    }
    return workers_position
def menu():
    menu_info = '''
    1. Просмотр 
    2. Удаление
    '''


def main():
    menu()
    get_product()
    get_workers_position()

#заменить слово "партия товаров"
#расписать функции пользователя(создать:1)партию 2) пользователя и тд)
#изменить структуру

if __name__ == '__main__':
    main()
