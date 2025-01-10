import tkinter as tk
from tkinter import messagebox

# Functionality for the To-Do List
def add_task():
    task = task_input.get()
    if task.strip() == "":
        messagebox.showwarning("Input Error", "Task cannot be empty!")
    else:
        task_list.insert(tk.END, task)
        task_input.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def clear_tasks():
    task_list.delete(0, tk.END)

# Creating the GUI
root = tk.Tk()
root.title("To-Do List")

# Task Input Section
task_input_frame = tk.Frame(root)
task_input_frame.pack(pady=10)

task_input = tk.Entry(task_input_frame, width=40)
task_input.pack(side=tk.LEFT, padx=5)
add_task_button = tk.Button(task_input_frame,bg="light green", text="Add Task", command=add_task)
add_task_button.pack(side=tk.RIGHT)

# Task List Section
task_list_frame = tk.Frame(root)
task_list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(task_list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_list = tk.Listbox(task_list_frame,bg="orange", width=50, height=15, yscrollcommand=scrollbar.set)
task_list.pack(side=tk.LEFT)
scrollbar.config(command=task_list.yview)

# Buttons Section
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

delete_task_button = tk.Button(buttons_frame,bg="red", text="Delete Task", command=delete_task)
delete_task_button.grid(row=0, column=0, padx=5)

clear_tasks_button = tk.Button(buttons_frame,bg="red", text="Clear All", command=clear_tasks)
clear_tasks_button.grid(row=0, column=1, padx=5)

# Running the Application
root.mainloop()
