import functions

import FreeSimpleGUI as sg

app=functions.TodoApp()
label = sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo", key = 'todo')
add_button=sg.Button("Add")
edit_button =sg.Button("Edit")
complete_button =sg.Button("Complete/Remove")


window = sg.Window('My To-Do App',
                   layout=[[[label], [input_box,add_button]]], 
                   font=('Helvetica',10))

while True:
    event,values= window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            app.list_todos()
            

window.close()