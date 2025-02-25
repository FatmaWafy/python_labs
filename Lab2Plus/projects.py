import json

PROJECTS_FILE = "../Lab2Plus/projects.json"

def load_projects():
    """Load projects from projects.json if it exists, otherwise return an empty list."""
    try:
        with open(PROJECTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_projects(projects):
    """Save projects list to projects.json."""
    with open(PROJECTS_FILE, "w") as file:
        json.dump(projects, file, indent=4)

def create_project():
    """Create a new project."""
    projects = load_projects()
    
    title = input("Enter project title: ")
    description = input("Enter project description: ")
    total_target = input("Enter total target amount: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    project = {
        "title": title,
        "description": description,
        "total_target": total_target,
        "start_date": start_date,
        "end_date": end_date
    }

    projects.append(project)
    save_projects(projects)
    print("Project created successfully!")

def view_projects():
    """View all projects."""
    projects = load_projects()
    if not projects:
        print("No projects found.")
        return
    print("\nList of Projects:")
    for idx, project in enumerate(projects, start=1):
        print(f"{idx}. {project['title']} - {project['description']}")

def delete_project():
    """Delete a project by index."""
    projects = load_projects()
    if not projects:
        print("No projects available to delete.")
        return
    
    view_projects()
    try:
        choice = int(input("Enter project number to delete: ")) - 1
        if 0 <= choice < len(projects):
            deleted_project = projects.pop(choice)
            save_projects(projects)
            print(f"Project '{deleted_project['title']}' deleted successfully!")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

def manage_projects():
    """Project management menu."""
    while True:
        print("\nProject Management:")
        print("1. Create Project\n2. View Projects\n3. Delete Project\n4. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_project()
        elif choice == "2":
            view_projects()
        elif choice == "3":
            delete_project()
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")
