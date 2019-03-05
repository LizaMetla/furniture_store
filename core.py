def get_worker():
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
    }
    return furniture


def get_batch():  # партия
    batch = {
        "batch_id": None,  # идент. партии
        "delivery_date": None,  # дата привоза партии
        "batch_number": None,  # количество партии
        "batch_price": None,  # цена партии

    }
    return batch


def menu():
    menu_info = '''
    1. Просмотр 
    2. Удаление
    3. Добавление
    4. Редактирование
    '''


def save_to_db_furniture(data: dict):
    pass


def save_to_db_position(data: dict):
    pass


def save_to_db_worker(data: dict):
    pass


def get_from_db_furniture() -> dict:
    pass


def get_from_db_position() -> dict:
    pass


def get_from_db_worker() -> dict:
    pass


def main():
    menu()
    get_furniture()
    get_batch()


if __name__ == '__main__':
    main()
