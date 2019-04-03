from base_structure import get_furniture, get_batch, get_department
from db_layer import get_from_db_furniture, get_from_db_department, get_from_db_batch, save, add_to_db
from menu_info import main_menu_info, search_choice, add_menu_info


# нужно добавить сортировку
def menu_input(menu_info):
    while True:
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
    sorted(db_objects['db_objects'], key=max, reverse=False)  # Сортировка перед выводом на экран
    for db_object in db_objects['db_objects']:
        dict_print(db_object)
        print('*' * 30)
    id = input('Введите id: ')
    return search_by_id(id, db_objects), db_objects


def filter_by_id_menu():
    result, db_objects = filter_by_id()
    if db_objects['db_name'] == 'Batch.pickle':  # Если поиск по поставком
        furniture_objects = filter_(get_from_db_furniture(), id_batch=result[
            'id_batch'])  # Ищем всю мебель, в которой id отдела совпадает с id поставки
        department_objects = get_from_db_department() # Получаем всю ммебель
        batch_to_department = [] # Создаём пустой список связанных объектов поставки и отдела
        for furniture_object in furniture_objects:
            batch_to_department.append(search_by_id(furniture_object['id_department'], department_objects)) # Ищем все отделы, в которых id совпадает с id отдела в найденной мебели
        print('Список связанных с поставкой отделов:')
        for department in batch_to_department:
            dict_print(department) # Печать отелов на экран
    return result


def search_by_id(obj_id, db_objects):
    for db_object in db_objects['db_objects']:
        if db_object.get('id_product') == obj_id or db_object.get('id_batch') == obj_id or db_object.get(
                'id_department') == obj_id:
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
                    2: get_department,
                    3: get_batch}.get(answer, send_error)()
    fill_shop_instance(empty_db_obj, db_objects['db_name'])
    add_to_db(db_objects, empty_db_obj)


# функции заполнения данными

def fill_shop_instance(data, db_name):
    for key in data:
        value = input(f'{key}: ')
        if db_name == "Furniture.pickle":
            if key == "id_batch":
                while not filter_(get_from_db_batch(), id_batch=value):
                    print('Поставка с данным id ещё не создана.', 'Введите id снова - ')
                    value = input(f'{key}: ')

            elif key == "id_department":
                while not filter_(get_from_db_department(), id_department=value):
                    print('Отдел с данным id ещё не создан.', 'Введите id снова - ')
                    value = input(f'{key}: ')

        data[key] = value


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
        print('Результат действия: \n')
        dict_print(result)


def send_error(*args, **kwargs):
    print("Ввод параметров неверный!")
    return {}


# функция для просмотра содержимого


def filter_(shop_instance_list, **kwargs):
    search_result = []
    for instance in shop_instance_list['db_objects']:
        if all(param in instance for param in kwargs):
            for param in kwargs:
                if instance[param] == kwargs[param] and instance not in search_result:
                    search_result.append(instance)
    return search_result


if __name__ == '__main__':
    main()
