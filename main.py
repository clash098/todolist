import json
import os

# This is where I'll keep my tasks
TODO_FILE = 'my_todo_list.json'

def load_tasks():
    """Load tasks from the JSON file or create a new list if it doesn't exist."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save my tasks to the JSON file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    """Show my current tasks."""
    if tasks:
        print("Here's what I need to do:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Looks like my to-do list is empty!")

def add_task(tasks, task):
    """Add a new task to my list."""
    tasks.append(task)
    save_tasks(tasks)
    print(f'Added: "{task}" to my to-do list!')

def remove_task(tasks, index):
    """Remove a task from my list by its index."""
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f'Got rid of: "{removed}" from my list.')
    else:
        print("Oops! That's not a valid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nWhat do I want to do?")
        print("1. View my tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            task = input("What task do I want to add? ")
            add_task(tasks, task)
        elif choice == '3':
            display_tasks(tasks)
            try:
                task_index = int(input("Which task number do I want to remove? ")) - 1
                remove_task(tasks, task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Thanks for checking my to-do list! Bye!")
            break
        else:
            print("Hmm, that doesn't seem right. Please try again.")

if __name__ == "__main__":
    main()

# Credits
print("\nCredits: Shoutout to Clash for the inspiration!")
