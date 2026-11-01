import json
import os

FILENAME = "todo_list.json"

def load_tasks():
    """Load tasks from a JSON file if it exists, otherwise return an empty list."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save the current task list to a JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    """Display all current tasks with their completion status."""
    if not tasks:
        print("\nYour to-do list is empty!")
        return
    print("\n--- YOUR TO-DO LIST ---")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['title']}")
    print("-" * 24)

def add_task(tasks):
    """Add a new task to the list."""
    title = input("\nEnter the task description: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print(f"Task '{title}' added successfully!")
    else:
        print("Task description cannot be empty.")

def complete_task(tasks):
    """Mark a specific task as completed."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("\nEnter the number of the task to mark as complete: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task from the list."""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("\nEnter the number of the task to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main application loop."""
    tasks = load_tasks()
    while True:
        print("\n=== COMMAND-LINE TO-DO APP ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()