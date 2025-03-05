class TodoApp:
    def __init__(self, filename="todos.txt"):
        self.filename = filename
        self.todos = self.load_todos()

    def load_todos(self):
        """Load todos from file, create file if it doesn't exist"""
        try:
            with open(self.filename, 'r') as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            return []

    def save_todos(self):
        """Save todos to file"""
        with open(self.filename, 'w') as f:
            for todo in self.todos:
                f.write(f"{todo}\n")

    def add_todo(self, task):
        """Add a new todo"""
        self.todos.append(task)
        self.save_todos()
        print(f"Added: {task}")

    def remove_todo(self, index):
        """Remove a todo by index"""
        try:
            removed_task = self.todos.pop(index - 1)
            self.save_todos()
            print(f"Removed: {removed_task}")
        except IndexError:
            print("Invalid task number!")

    def edit_todo(self, index, task):
        """Edit a todo by index"""
        try:
            
            self.todos[index - 1]=task
            self.save_todos()
            
        except IndexError:
            print("Invalid task number!")

    def list_todos(self):
        """Display all todos"""
        if not self.todos:
            print("No tasks in your TODO list!")
            return
        
        print("\nYour TODO List:")
        print("-" * 40)
        for i, task in enumerate(self.todos, 1):
            print(f"{i}. {task}")
        print("-" * 40)
