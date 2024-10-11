def contents(file_name):
    with open(file_name, 'rb') as f:
        data = f.read()
    return data