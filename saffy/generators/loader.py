import pickle

def loader(file_name):
    # TODO some check if data is valid
    with open(file_name, 'rb') as f:
        data = pickle.load(f)

    return data


