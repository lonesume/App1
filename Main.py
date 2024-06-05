todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit : ").strip()

    match user_action :
        case 'add':
            todo = input("Enter a todo:").strip() + "\n"

            with open('todos.txt', 'r') as file :
                todos = file.readlines()
            
            # print(f"todos before insertion: {todos}")
            todos.append(todo)
            # print(f"todos after insertion: {todos}")

            with open('todos.txt', 'w') as file :
                file.writelines(todos)

        case 'show':
            with open('todos.txt','r') as file :
                todos = file.readlines()
             
            new_todos = [item.strip('\n') for item in todos] 

            for index, item in enumerate(new_todos):
                 row = f"{index + 1 }.{item}"
                 print(row)
        case 'edit':
            number = int(input("Number of the todo edit: "))
            number = number - 1
            with open('todos.txt','r') as file :
                todos = file.readlines()
            new_todo = input("Enter new todo:")
            todos[number] = new_todo
            print("New todo:",new_todo)
            with open('todos.txt', 'w') as file :
                file.writelines(todos)
        
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            with open('todos.txt','r') as file :
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('')
            todos.pop(number -1)
            with open('todos.txt', 'w') as file :
                file.writelines(todos)
            message = f"Todo {todo_to_remove}  has been completed!"
            print(message)
            
            
        
        case 'exit':
            break

print("Thank You!")
