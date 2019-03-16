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
