import pickle


def get_from_db_furniture() -> list:
    try:
        with open('Furniture.pickle', 'rb') as f:
            furniture_new = pickle.load(f)
            return furniture_new
    except EOFError:
        return []


def get_from_db_batch() -> list:
    try:
        with open('Batch.pickle', 'rb') as f:
            batch_new = pickle.load(f)
            return batch_new
    except EOFError:
        return []


def get_from_db_department() -> list:
    try:
        with open('Department.pickle', 'rb') as f:
            department_new = pickle.load(f)
            return department_new
    except EOFError:
        return []


def save_to_db_furniture(furniture: dict):
    furniture_list = get_from_db_furniture()
    furniture_list.append(furniture)
    with open('Furniture.pickle', 'wb') as f:
        pickle.dump(furniture_list, f)


def save_to_db_batch(batch: dict):
    batch_list = get_from_db_batch()
    batch_list.append(batch)
    with open('Batch.pickle', 'wb') as f:
        pickle.dump(batch_list, f)


def save_to_db_department(department: dict):
    department_list = get_from_db_department()
    department_list.append(department)
    with open('Department.pickle', 'wb') as f:
        pickle.dump(department_list, f)
