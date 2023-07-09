```python
import tkinter as tk
from tkinter import filedialog, messagebox
from src.file_manager import uploadFile, updateFile
from src.search_function import searchFiles
from src.reminder_system import createTask, updateTask

class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Digital Organizer")
        self.userFiles = []
        self.userTasks = []

        self.fileListView = tk.Listbox(self.root)
        self.taskListView = tk.Listbox(self.root)
        self.searchBar = tk.Entry(self.root)
        self.fileUploadButton = tk.Button(self.root, text="Upload File", command=self.upload_file)
        self.taskCreateButton = tk.Button(self.root, text="Create Task", command=self.create_task)

        self.fileListView.pack()
        self.taskListView.pack()
        self.searchBar.pack()
        self.fileUploadButton.pack()
        self.taskCreateButton.pack()

    def upload_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            file = uploadFile(filename)
            self.userFiles.append(file)
            self.fileListView.insert(tk.END, file['name'])
            messagebox.showinfo("File Uploaded", "File has been uploaded successfully!")

    def create_task(self):
        task_name = simpledialog.askstring("Input", "What is the task?")
        if task_name:
            task = createTask(task_name)
            self.userTasks.append(task)
            self.taskListView.insert(tk.END, task['name'])
            messagebox.showinfo("Task Created", "Task has been created successfully!")

    def search_files(self, event):
        query = self.searchBar.get()
        results = searchFiles(query, self.userFiles)
        self.fileListView.delete(0, tk.END)
        for file in results:
            self.fileListView.insert(tk.END, file['name'])

    def run(self):
        self.searchBar.bind('<Return>', self.search_files)
        self.root.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
```