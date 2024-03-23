"""
CP1404 - Practical 7
Name: <SAGUN LIMBU>
"""

from project import Project
import datetime


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip header
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            start_date = Project.parse_date(start_date)
            priority = int(priority)
            cost_estimate = float(cost_estimate)
            completion_percentage = int(completion_percentage)
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def save_projects(projects, filename):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(str(project) + '\n')


def display_projects(projects):
    """Display projects."""
    incomplete_projects = [project for project in projects if project.is_incomplete()]
    completed_projects = [project for project in projects if not project.is_incomplete()]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(
            f"{project.name}, start: {project.start_date}, priority {project.priority}, estimate: ${project.cost_estimate}, completion: {project.completion_percentage}%")

    print("\nCompleted projects:")
    for project in completed_projects:
        print(
            f"{project.name}, start: {project.start_date}, priority {project.priority}, estimate: ${project.cost_estimate}, completion: {project.completion_percentage}%")


def filter_projects_by_date(projects):
    """Filter projects by date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date = Project.parse_date(date_string)
    filtered_projects = [project for project in projects if project.is_started_after_date(date)]
    display_projects(filtered_projects)


def add_new_project(projects):
    """Add a new project."""
    name = input("Name: ")
    start_date = Project.parse_date(input("Start date (dd/mm/yyyy): "))
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Update a project."""
    print_projects(projects)
    choice = int(input("Project choice: "))
    project = projects[choice]
    new_percentage = int(input("New Percentage: "))
    new_priority = input("New Priority: ")
    if new_percentage:
        project.update_completion_percentage(new_percentage)
    if new_priority:
        project.update_priority(new_priority)


def main():
    """Main function."""
    projects_filename = 'projects.txt'
    projects = load_projects(projects_filename)
    print(f"Loaded {len(projects)} projects from {projects_filename}")

    while True:
        print("\nMenu:")
        print("(L)oad projects")
        print("(S)ave projects")
        print("(D)isplay projects")
        print("(F)ilter projects by date")
        print("(A)dd new project")
        print("(U)pdate project")
        print("(Q)uit")

        choice = input(">>> ").strip().lower()

        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(projects, filename)
            print(f"Projects saved to {filename}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_option = input("Would you like to save to projects.txt? ").strip().lower()
            if save_option.startswith('y'):
                save_projects(projects, projects_filename)
                print(f"Projects saved to {projects_filename}")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print("Welcome to Pythonic Project Management")
    main()
