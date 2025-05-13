import json

def load_task():
    try:
        with open('tasks.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []

def save_task_helper(tasks):
    with open('tasks.txt', 'w') as file:
        json.dump(tasks, file)

def get_time_input():
    while True:
        time_input = input("Enter Video time (HH:MM): ")
        if ":" in time_input:
            hh, mm = time_input.split(":")
            if hh.isdigit() and mm.isdigit():
                hh = int(hh)
                mm = int(mm)
                if 0 <= mm < 60:
                    return f"{hh:02d}:{mm:02d}"
        print("Invalid time format. Please use HH:MM where hours can be any number and minutes 0–59.")


def list_all_tasks(tasks):
    print("\n")
    print("_" * 70)
    for index, video in enumerate(tasks, start=1):
        print(f"{index}. {video['name']}, Duration {video['time']}")
    print("\n")
    print("_" * 70)

def add_task(tasks):
    name = input("Enter Video name: ").capitalize()
    time = get_time_input()
    tasks.append({'name': name, 'time': time})
    save_task_helper(tasks)
    print("🎉 Success! Your video has been added to the library.")

def search_task(tasks):
    search_term = input("Enter video name to search: ").capitalize()
    found = False

    for index, video in enumerate(tasks, start=1):
        if search_term in video['name'].capitalize():
            print(f"\n✅ Found: {index}. {video['name']}, Duration {video['time']}")
            found = True

    if not found:
        print("❌ No video found with that name.")


def update_task(tasks):
    list_all_tasks(tasks)
    index = int(input("Enter the Video number to update: "))
    if 1 <= index <= len(tasks):
        name = input("Enter Video name: ").capitalize()
        time = get_time_input() 
        tasks[index-1] = {'name':name, 'time': time}
        save_task_helper(tasks)
        print("- Success! Your video has been updated. -")
    else:
        print("Invalid index selected")

def delete_task(tasks):
    list_all_tasks(tasks)
    index = int(input("Enter the Video number to delete: "))
    if 1 <= index <= len(tasks):
        del tasks[index-1]
        save_task_helper(tasks)
        print("🗑️ Video deleted successfully!")
    else:
        print("Invalid video index selected")

def sort_tasks(tasks):
    print("Sort by:\n1. Name\n2. Duration")
    choice = input("Enter choice (1/2): ")
    
    if choice == '1':
        sorted_tasks = sorted(tasks, key=lambda x: x['name'].lower())
    elif choice == '2':
        sorted_tasks = sorted(tasks, key=lambda x: x['time'])
    else:
        print("Invalid choice")
        return
    
    print("\nSorted Videos:")
    list_all_tasks(sorted_tasks)

def main():
    tasks = load_task()
    while True:
        print("\n YOUTUBE MANAGER 💼🚀")
        print("Choose an option:")
        print("1. List all youtube Videos")
        print("2. Add a youtube Video ")
        print("3. Search youtube Video details ")
        print("4. Update a youtube Video details ")
        print("5. Delete a youtube Video ")
        print("6. Check status ")
        print("7. Exit the app ")

        option = input("Enter your choice: ")

        match option:
            case '1':
                list_all_tasks(tasks)
            case '2':
                add_task(tasks)
            case '3':
                search_task(tasks)
            case '4':
                update_task(tasks)
            case '5':
                delete_task(tasks)
            case '6':
                sort_tasks(tasks)
            case '7':
                break
            case _:
                print("Invalid Choice")

if __name__ ==  "__main__":
    main()                