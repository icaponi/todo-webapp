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

def main():
    app = TodoApp()
    
    while True:
        print("\nTODO App Menu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            task = input("Enter task: ")
            app.add_todo(task)
        
        elif choice == '2':
            app.list_todos()
            if app.todos:
                try:
                    index = int(input("Enter task number to remove: "))
                    app.remove_todo(index)
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == '3':
            app.list_todos()
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()