import streamlit as st
import Functions as cli
from PIL import Image

todos = cli.get_todos()
def add_todo(): 
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    cli.write_todos(todos)
   


st.title("Lonesume's Todo app")

image = Image.open("brian-pfp-2.JPG")
st.image("brian-pfp.JPG", caption="Brian Joseph (circa May 2024)", width=350 )

st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
   checkbox =  st.checkbox(todo, key=todo) 
   if checkbox :
       print(checkbox)
       todos.pop(index)
       cli.write_todos(todos)
       del st.session_state[todo]
       st.experimental_rerun()

st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key= "new_todo")
