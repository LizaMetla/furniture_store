from base_structure import get_furniture, get_batch, get_department
from db_layer import get_from_db_furniture, get_from_db_department, get_from_db_batch, save, add_to_db
from menu_info import main_menu_info, search_choice, add_menu_info


def menu_input(menu_info):
    while 1:
        print(menu_info)
        answer = input('Выберите пункт меню: ')
        try:
            return int(answer)
        except ValueError:
            print('Повторите ввод!')


def dict_print(dict_obj):
    if dict_obj is not None:
        for key, value in dict_obj.items():
            print(f'{key}: {value}')


def filter_by_id():
    answer = menu_input(search_choice)
    if answer == '0':
        return None
    db_objects = {1: get_from_db_furniture,
                  2: get_from_db_department,
                  3: get_from_db_batch}.get(answer, send_error)()
    for db_object in db_objects['db_objects']:
        dict_print(db_object)
        print('*' * 30)
    id = input('Введите id: ')
    return search_by_id(id, db_objects), db_objects


def filter_by_id_menu():
    result, _ = filter_by_id()
    return result


def search_by_id(obj_id, db_objects):
    for db_object in db_objects['db_objects']:
        if db_object['id_product'] == obj_id:
            return db_object


def delete_by_id():
    result, db_objects = filter_by_id()
    db_objects["db_objects"].remove(result)
    save(db_objects, db_objects['db_name'])
    return result, db_objects


def add_menu():
    answer = menu_input(add_menu_info)
    if answer == '0':
        return None
    db_objects = {1: get_from_db_furniture,
                  2: get_from_db_department,
                  3: get_from_db_batch}.get(answer, send_error)()
    empty_db_obj = {1: get_furniture,
                    2: get_batch,
                    3: get_department}.get(answer, send_error)()
    fill_shop_instance(empty_db_obj, db_objects['db_name'])
    add_to_db(db_objects, empty_db_obj)


# функции заполнения данными

def fill_shop_instance(data, db_name):
    for key in data:
        if db_name == "Furniture.pickle" and key == "id_batch":
            answer = None
            while answer is None:
                pass #TODO
        data[key] = input(f'{key}: ')


def edit_db_obj_menu():
    result, db_objects = delete_by_id()
    flag_exit = 'Д'
    while (flag_exit == "Д"):
        key = input('Введите имя поля для редактирования: ')
        while (key not in result):
            print('Ошибка! Повторите ввод!!!')
            key = input('Введите имя поля для редактирования: ')
        result[key] = input('Введите новое поле: ')
        flag_exit = input('Продолжить редактирование Д/н')
    add_to_db(db_objects, result)


def delete_by_id_menu():
    result, _ = delete_by_id()
    return result


def main():
    while True:
        answer = menu_input(main_menu_info)
        result = {1: filter_by_id_menu,
                  2: delete_by_id_menu,
                  3: add_menu,
                  4: edit_db_obj_menu,
                  0: exit}.get(answer, send_error)()
        dict_print(result)


def send_error(*args, **kwargs):
    print("Ввод параметров неверный!")
    return {}


if __name__ == '__main__':
    main()

# функция для просмотра содержимого
#
#
# def filter_(shop_instance_list, **kwargs):
#     search_result = []
#     for instance in shop_instance_list:
#         if all(param in instance for param in kwargs):
#             for param in kwargs:
#                 if instance[param] == kwargs[param] and instance not in search_result:
#                     search_result.append(instance)
#     return search_result
