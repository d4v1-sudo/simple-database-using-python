import os
import db

INITIAL_MENU = 99
EXIT = 4

def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def display_header():
    clear_console()
    COLUMN_COUNT = 60
    print("-" * COLUMN_COUNT)
    print("{:^60}".format("TASKS"))
    print("-" * COLUMN_COUNT)
    print("{:^60}".format("Enter 99 to return to the initial menu, [CTRL+C] to exit"))
    print("-" * COLUMN_COUNT)

def display_tasks(tasks):
    print("-" * 60)
    print("{:<6} {:<50} {:<3}".format("ID", "Task Description", "Done"))
    print("-" * 60)
    for task in tasks:
        task_id, description, completed = task
        check = u'\u2713' if completed == 1 else " "
        print("{:<6} {:<50} {:<3}".format(task_id, description, check))
    print("-" * 60)

def show_new_task_option():
    task_description = input("Describe the task => ")
    print("Adding task -> " + str(task_description))
    if task_description != str(INITIAL_MENU):
        db.add_task(task_description)

def show_complete_task_option():
    task_id = int(input("Which task do you want to mark as complete? Enter the ID => "))
    print("Completing task -> " + str(task_id))
    if task_id != INITIAL_MENU:
        db.complete_task(task_id)

def show_delete_task_option():
    task_id = int(input("Which task do you want to delete? Enter the ID => "))
    print("Deleting task -> " + str(task_id))
    if task_id != INITIAL_MENU:
        db.remove_task(task_id)

def exit_program():
    choice = input("Do you want to exit? (y/n): ")
    if choice.lower() in ("yes", "y"):
        db.exit_program()
    else:
        return
