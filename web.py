import streamlit as st
import functions
import time

todos = functions.get_todos()


    
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    if todo not in todos:
        todos.append(todo)
        functions.write_todos(todos)
    else:
        placeholder.markdown (
                                """
                                <div style="background-color: red; padding: 10px; border-radius: 5px;">
                                    <p style="color: white; text-align: center;">This todo is already listed! Try another one...</p>
                                </div>
                                """
                                ,
                                unsafe_allow_html=True
                             )
        time.sleep(3)
        placeholder.empty()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
     
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()              
    
        

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

placeholder=st.empty()

#st.session_state