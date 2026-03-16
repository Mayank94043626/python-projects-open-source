import tkinter as tk
from tkinter import simpledialog, messagebox

def add_task():
    task = simpledialog.askstring("Add Task", "Enter a new task:")
    if task:
        todo_list.append(task)
        update_display()

def remove_task():
    if not todo_list:
        messagebox.showinfo("No Tasks", "No tasks to remove.")
        return

    task_num = simpledialog.askinteger("Remove Task", "Enter the task number to remove:", minvalue=1, maxvalue=len(todo_list))
    if task_num:
        del todo_list[task_num - 1]
        update_display()

def update_display():
    task_display.config(state=tk.NORMAL)
    task_display.delete(1.0, tk.END)
    for index, task in enumerate(todo_list, start=1):
        task_display.insert(tk.END, f"{index}. {task}\n")
    task_display.config(state=tk.DISABLED)

def quit_app():
    window.destroy()

# Initialize the main window
window = tk.Tk()
window.title("Fancy ToDo List")
window.geometry("500x500")  # Set the window dimensions

# Create a canvas with gradient background
canvas = tk.Canvas(window, bg="#002855", width=500, height=500)
canvas.pack()

# Create GUI elements with customized appearance
add_button = tk.Button(window, text="Add Task", command=add_task, bg="#4286f4", fg="white", font=("Helvetica", 12))
remove_button = tk.Button(window, text="Remove Task", command=remove_task, bg="#e74c3c", fg="white", font=("Helvetica", 12))
quit_button = tk.Button(window, text="Quit", command=quit_app, bg="#34495e", fg="white", font=("Helvetica", 12))
task_display = tk.Text(window, wrap=tk.WORD, state=tk.DISABLED, bg="#f2f2f2", font=("Helvetica", 12))

# Organize GUI elements using the grid layout
add_button_window = canvas.create_window(100, 30, window=add_button)
remove_button_window = canvas.create_window(250, 30, window=remove_button)
quit_button_window = canvas.create_window(400, 30, window=quit_button)
task_display_window = canvas.create_window(250, 250, window=task_display, width=400, height=300)

# Initialize the to-do list
todo_list = []

# Start the GUI event loop
window.mainloop()