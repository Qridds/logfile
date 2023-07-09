```python
import tkinter as tk
from src.file_manager import uploadFile, updateFile
from src.search_function import searchFiles
from src.reminder_system import createTask, updateTask, setReminder

class UserInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Digital Organizer")

        self.fileListView = tk.Listbox(self.window)
        self.taskListView = tk.Listbox(self.window)
        self.searchBar = tk.Entry(self.window)
        self.fileUploadButton = tk.Button(self.window, text="Upload File", command=self.upload_file)
        self.taskCreateButton = tk.Button(self.window, text="Create Task", command=self.create_task)

        self.fileListView.pack()
        self.taskListView.pack()
        self.searchBar.pack()
        self.fileUploadButton.pack()
        self.taskCreateButton.pack()

    def upload_file(self):
        filename = tk.filedialog.askopenfilename()
        uploadFile(filename)
        self.update_file_list()

    def create_task(self):
        task_name = tk.simpledialog.askstring("Task Name", "Enter task name:")
        createTask(task_name)
        self.update_task_list()

    def update_file_list(self):
        self.fileListView.delete(0, tk.END)
        for file in userFiles:
            self.fileListView.insert(tk.END, file)

    def update_task_list(self):
        self.taskListView.delete(0, tk.END)
        for task in userTasks:
            self.taskListView.insert(tk.END, task)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
```