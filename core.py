from db_layer import *  # чтобы доставать информацию из файла,не перечисляя все ф-ии
from menu_info import *
from base_structure import *


# функции заполнения данными


def fill_shop_instance(data):
    for key in data:
        data[key] = input(f'{key}: ')


# фунции поиска элемента для осуществления просмотра/редактирования/удаления

def search_furniture_by_id(id_furniture):
    appointments = get_from_db_furniture()
    for furniture in appointments:
        if furniture['id_product'] == id_furniture:
            return furniture


def search_department_by_id(id_department):
    departments = get_from_db_department()
    for department in departments:
        if department['id_department'] == id_department:
            return department


def search_batch_by_id(id_batch):
    batches = get_from_db_batch()
    for batch in batches:
        if batch['id_batch'] == id_batch:
            return batch


# created new menu


# здесь нужно создать подменю , в котором мы выбираем какое поле изменить (?)
# Возможно ли его создать в editing_menu ?


# это отдельная функция по фильтрации продуктов по id

# функции по добавлению элементов


def add_furniture():
    furniture = get_furniture()
    fill_shop_instance(furniture)
    add_to_db_furniture(furniture)


def add_batch():
    batch = get_batch()
    fill_shop_instance(batch)
    add_to_db_batch(batch)


def add_department():
    department = get_department()
    fill_shop_instance(department)
    add_to_db_department(department)


def add_menu():
    answer = menu(add_menu_info)
    {1: add_furniture,
     2: add_department,
     3: add_batch,
     0: ''}.get(answer, send_error)()


# функция для просмотра содержимого


def filter_(shop_instance_list, **kwargs):
    search_result = []
    for instance in shop_instance_list:
        if all(param in instance for param in kwargs):
            for param in kwargs:
                if instance[param] == kwargs[param] and instance not in search_result:
                    search_result.append(instance)
    return search_result


def main():
    main_menu()


def main_menu():
    answer = menu(main_menu_info)
    {1: filter_by_id,
     2: '',
     3: add_menu,
     4: '',
     5: '',
     0: ''}.get(answer, send_error)()


def menu(menu_info):
    while 1:
        print(menu_info)
        answer = input('Выберите пункт меню: ')
        try:
            return int(answer)
        except ValueError:
            print('Повторите ввод!')


def filter_by_id():
    answer = menu(search_choice)
    id = input('Введите id: ')
    dict_print({1: search_furniture_by_id,
                2: search_department_by_id,
                3: search_batch_by_id}.get(answer, send_error)(id))


def dict_print(dict_obj):
    for key, value in dict_obj.items():
        print(key, value)


def send_error(*args, **kwargs):
    print("Ввод параметров неверный!")
    return {}


if __name__ == '__main__':
    main()
