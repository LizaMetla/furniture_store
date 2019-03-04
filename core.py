def get_worker():
    worker = {
        "id": None,
        "first_n": None,
        "last_n": None,
        "middle_n": None,
        "position": None,
        "tel_number": None,
    }
    return worker


def get_product():
    product = {
        "id": None,
        "department": None,
        "name": None,
        "price": None,
    }
    return product


def get_workers_position():
    workers_position = {
        "id": None,
        "position": None,
        "price": None,
    }
    return workers_position


def main():
    get_worker()
    get_product()
    get_workers_position()
    pass


if __name__ == '__main__':
    main()
