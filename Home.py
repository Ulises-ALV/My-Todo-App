import streamlit as st
import functions
import time

todos = functions.get_todos()

st.set_page_config(layout="wide")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

st.text_input(label="Enter a todo", label_visibility="hidden", placeholder="Add new todo:",
              on_change=add_todo, key="new_todo")

# Esta parte del codigo hace que se borren los elementos
# de la lista cuando se hace click en ellos

#    for index, toodo in enumerate(todos):
#        checkbox = st.checkbox(toodo, key=toodo)
#        if checkbox:
#            todos.pop(index)
#            functions.write_todos(todos)
#            del st.session_state[toodo]
#            st.experimental_rerun()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

