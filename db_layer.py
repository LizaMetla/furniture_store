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

def save(obj_list, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(obj_list, f)

def add_to_db_furniture(furniture: dict):
    furniture_list = get_from_db_furniture()
    furniture_list.append(furniture)
    save('Furniture.pickle', furniture_list)



def add_to_db_batch(batch: dict):
    batch_list = get_from_db_batch()
    batch_list.append(batch)
    save('Batch.pickle', batch_list)


def add_to_db_department(department: dict):
    department_list = get_from_db_department()
    department_list.append(department)
    save('Department.pickle', department_list)

