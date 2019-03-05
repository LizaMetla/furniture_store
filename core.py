import pickle


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


def save_to_db_furniture(furniture: dict):
    with open('furniture.pickle', 'wb') as f:
        pickle.dump(furniture, f)


def save_to_db_batch(batch: dict):
    with open('batch.pickle', 'wb') as f:
        pickle.dump(batch, f)


def save_to_db_department(department: dict):
    with open('department.pickle', 'wb') as f:
        pickle.dump(department, f)


def get_from_db_furniture() -> dict:
    with open('furniture.pickle', 'rb') as f:
        furniture_new = pickle.load(f)
        return furniture_new


def get_from_db_batch() -> dict:
    with open('batch.pickle', 'rb') as f:
        batch_new = pickle.load(f)
        return batch_new


def get_from_db_department() -> dict:
    with open('department.pickle', 'rb') as f:
        department_new = pickle.load(f)
        return department_new


def main():
    menu()
    get_furniture()
    get_batch()


if __name__ == '__main__':
    main()
