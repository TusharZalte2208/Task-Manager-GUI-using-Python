import tkinter as tk
from tkinter import messagebox


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("400x500")
        self.root.config(bg="#2C3E50")

        self.tasks = []

        # Title
        tk.Label(root, text="Task Manager", font=("Arial", 18, "bold"), bg="#2C3E50", fg="white").pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.task_entry.pack(pady=5)

        # Buttons
        tk.Button(root, text="Add Task", command=self.add_task, font=("Arial", 12), bg="#27AE60", fg="white").pack(
            pady=5)
        tk.Button(root, text="Update Task", command=self.update_task, font=("Arial", 12), bg="#F1C40F",
                  fg="black").pack(pady=5)
        tk.Button(root, text="Delete Task", command=self.delete_task, font=("Arial", 12), bg="#E74C3C",
                  fg="white").pack(pady=5)

        # Task List
        self.task_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
        self.task_listbox.pack(pady=5)

        # View Button
        tk.Button(root, text="View Tasks", command=self.view_tasks, font=("Arial", 12), bg="#3498DB", fg="white").pack(
            pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.view_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def update_task(self):
        try:
            selected_task = self.task_listbox.get(self.task_listbox.curselection())
            new_task = self.task_entry.get()
            if new_task:
                index = self.tasks.index(selected_task)
                self.tasks[index] = new_task
                self.task_entry.delete(0, tk.END)
                self.view_tasks()
            else:
                messagebox.showwarning("Warning", "New task cannot be empty!")
        except:
            messagebox.showwarning("Warning", "Please select a task to update!")

    def delete_task(self):
        try:
            selected_task = self.task_listbox.get(self.task_listbox.curselection())
            self.tasks.remove(selected_task)
            self.view_tasks()
        except:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
