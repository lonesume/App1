import Functions 
import FreeSimpleGUI as sg
import time

sg.theme("DarkGrey4")
clock= sg.Text(key = "clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
listbox = sg.Listbox(values=Functions.get_todos(), key="todos",
                      enable_events=True, size=[45,10])
window = sg.Window('My To-Do App', 
                   layout=[[clock],
                    [label],[input_box, add_button],
                           [listbox,edit_button, complete_button],
                           [exit_button]], 
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    
    match event:
        case 'Add':
            todos = Functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            Functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Complete":
            try :
                todo_complete = values["todos"][0]
                todos = Functions.get_todos()
                todos.remove(todo_complete)
                Functions.write_todos(todos)
                window["todos"].update(values = todos)
            except IndexError :
                sg.popup("Please select a ToDo first.", font=("Helvetica", 20))

        case "Edit": 
              try :
                todo_edit = values["todos"][0]
                new_todo = values["todo"]


                todos = Functions.get_todos()
                index = todos.index(todo_edit)
                todos[index]= new_todo
                Functions.write_todos(todos)
                window["todos"].update(values=todos)
              except IndexError :
                  sg.popup("Please select a ToDo first.", font=("Helvetica", 20))
        case "Exit": 
            break 
        case "todos":
            window["todo"].update(value=values["todos"][0])
            window["todo"].update(value= "")
        
        case sg.WIN_CLOSED :
            break
window.close()