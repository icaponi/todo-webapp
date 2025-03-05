import functions
def main():
    app = functions.TodoApp()
    
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