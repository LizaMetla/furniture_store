from db_layer import *  # чтобы доставать информацию из файла,не перечисляя все ф-ии


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

# фунции поиска элемента для осуществления просмотра/редактирования/удаления

def search_furniture(id_furniture):
    appointments = get_from_db_furniture()
    for furniture in appointments:
        if furniture['id_furniture'] == id_furniture:
            return appointments


def search_department(id_department):
    departments = get_from_db_department()
    for department in departments:
        if department['id_department'] == id_department:
            return departments


def search_batch(id_batch):
    batches = get_from_db_batch()
    for batch in batches:
        if batch['id_batch'] == id_batch:
            return batches


def main_menu():
    menu_info = '''
    1. Просмотр 
    2. Удаление
    3. Добавление
    4. Редактирование
    5. Фильтрация коренного списка
    
    0. Выход.
    '''
    answer = menu(menu_info)
    {1: filter,
     2: '',
     3: add_menu,
     4: '',
     5: '',
     0: ''}.get(answer, "Ввод параметров неверный!")()

# created new menu


def view_menu():
    view_menu_info = '''
    Осуществить просмотр информации о продукте:
    1. По ID Продукта  
    2. По названию продукта 
    3. Выйти в основное меню 
    
    0. Выход.
    '''

def delete_menu():
    delete_menu_info = '''
    Осуществить удаление по:
    1. По ID продукта
    2. По названию 
    3. Выйти в основное меню 
    
    0. Выход.
    '''

def editing_menu():
    editing_menu_info = '''
    1. Введите конкретный продукт информацию о котором вы хотите изменить:
    2. Выйти в основное меню 
    
    0. Выход.
    '''
# здесь нужно создать подменю , в котором мы выбираем какое поле изменить (?)
# Возможно ли его создать в editing_menu ?


def filter_by_id():
    pass
# это отдельная функция по фильтрации продуктов по id

# функции по добавлению элементов


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


# функция для просмотра содержимого


def filter(shop_instance_list, **kwargs):
    search_result = []
    for instance in shop_instance_list:
        if all(param in instance for param in kwargs):
            for param in kwargs:
                if instance[param] == kwargs[param] and instance not in search_result:
                    search_result.append(instance)
    return search_result


def main():
    main_menu()


if __name__ == '__main__':
    main()
