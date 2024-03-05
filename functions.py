"""Read a text file and return the list of to-do items"""
def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file:
            toods_local = file.readlines()
    return toods_local


"""Write the to-do items list in the text file"""
def write_todos(todos_local, filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_local)


if __name__ == '__main__':
     print('hello')
     print(get_todos())