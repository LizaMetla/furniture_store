import pickle


def get_from_db_furniture() -> dict:
    try:
        with open('Furniture.pickle', 'rb') as f:
            furniture_new = pickle.load(f)
            return furniture_new
    except EOFError:
        return {'db_name': 'Furniture.pickle',
                'db_objects': []}


def get_from_db_batch() -> dict:
    try:
        with open('Batch.pickle', 'rb') as f:
            batch_new = pickle.load(f)
            return batch_new
    except EOFError:
        return {'db_name': 'Batch.pickle',
                'db_objects': []}


def get_from_db_department() -> dict:
    try:
        with open('Department.pickle', 'rb') as f:
            department_new = pickle.load(f)
            return department_new
    except EOFError:
        return {'db_name': 'Department.pickle',
                'db_objects': []}


def save(objects, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(objects, f)


def add_to_db(db_objects: dict, instance: dict):
    db_objects['db_objects'].append(instance)
    save(db_objects, db_objects['db_name'])
