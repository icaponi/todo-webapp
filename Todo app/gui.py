import functions

import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo")
add_button=sg.Button("Add")
edit_button =sg.Button("Edit")
complete_button =sg.Button("Complete/Remove")
teste=sg.Checkbox("")

window = sg.Window('My To-Do App',layout=[[[label], [input_box,add_button],[teste]]])
window.read()
window.close()