# ToDo List

todos = []

# add todo with user input in a loop
while True:
    todo = input("Enter a todo: ")
    todos.append(todo)
    print("Todo added:", todo)
    # print the list of todos
    print("CurrentTodos:", todos)
    choice = input("Do you want to add another todo? (y)es or (n)o: ")
    if choice.lower() != "y":
        break

# print the list of todos
print("All Todos:", todos)