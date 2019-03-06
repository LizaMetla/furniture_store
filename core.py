from db_layer import *   # чтобы доставать информацию из файла,не перечисляя все ф-ии


# функции заполнения данными


def get_department():
    department = {
        "id_department": None,  # идент. отдела
        "department_name": None,  # название отдела
        "department_leader": None,  # управляющий отделом

    }
    return department


def get_furniture():
    furniture = {
        "id_product": None,  # идент. продукта
        "id_department": None,  # идент. отдела
        "birthday": None,  # дата создания продукта
        "name": None,  # название продукта
        "product_price": None,  # цена продукта
        "id_batch": None
    }
    return furniture


def get_batch():  # партия
    batch = {
        "id_batch": None,  # идент. партии
        "delivery_date": None,  # дата привоза партии
        "batch_number": None,  # количество партии
        "batch_price": None,  # цена партии

    }
    return batch


def fill_shop_instance(data):
    for key in data:
        data[key] = input(f'{key}: ')


def menu(menu_info):
    while 1:
        print(menu_info)
        answer = input('Выберите пункт меню: ')
        try:
            return int(answer)
        except ValueError:
            print('Повторите ввод!')


def main_menu():
    menu_info = '''
    1. Просмотр 
    2. Удаление
    3. Добавление
    4. Редактирование
    
    0. Выход.
    '''
    answer = menu(menu_info)
    {1: '',
     2: '',
     3: add_menu,
     4: '',
     0: ''}.get(answer, "Ввод параметров неверный!")()


# added functions for all shop instance


def add_furniture():
    furniture = get_furniture()
    fill_shop_instance(furniture)
    save_to_db_furniture(furniture)


def add_batch():
    batch = get_batch()
    fill_shop_instance(batch)
    save_to_db_batch(batch)


def add_department():
    department = get_department()
    fill_shop_instance(department)
    save_to_db_department(department)


def add_menu():
    add_menu_info = """
    1. Добавить мебель.
    2. Добавить отдел.
    3. Добавить партию товара.
    
    0. Выход
    """
    answer = menu(add_menu_info)
    {1: add_furniture,
     2: add_department,
     3: add_batch,
     0: ''}.get(answer, "Ввод параметров неверный!")()


def search_dict_in_list_by_id(id, shop_instance_list):
    pass


def main():
    main_menu()


if __name__ == '__main__':
    main()
