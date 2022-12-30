def get_todos(filepath="todos.txt"):
    """Read a text file with a list of todos"""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    """Write the todo items to a text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
        return