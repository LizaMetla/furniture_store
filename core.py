def get_worker():
    department = {
        "id_department": None, # идент. отдела
        "department_name": None, # название отдела
        "department_leader": None, # управляющий отделом

    }
    return department


def get_furniture():
    furniture = {
        "id_product": None,  # идент. продукта
        "id_department": None, # идент. отдела
        "birthday": None,  # дата создания продукта
        "name": None, # название продукта
        "product_price": None, # цена продукта
    }
    return furniture


def get_batch(): # партия
    batch = {
        "batch_id": None, # идент. партии
        "delivery_date": None, # дата привоза партии
        "batch_number": None, # количество партии
        "batch_price": None, # цена партии

    }
    return batch
def menu():
    menu_info = '''
    1. Просмотр 
    2. Удаление
    3. Добавление
    4. Редактирование
    '''


def main():
    menu()
    get_furniture()
    get_batch()

#заменить слово "партия товаров"
#расписать функции пользователя(создать:1)партию 2) пользователя и тд)
#изменить структуру

if __name__ == '__main__':
    main()
