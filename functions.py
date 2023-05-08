FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Legge un file di testo e ritorna una lista di to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Scrive ls lista di to-do item nel file di testo"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
