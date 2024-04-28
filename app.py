import db
import messages as msg

def main():
    try:
        while True:
            msg.display_header()
            tasks = db.get_tasks()
            msg.display_tasks(tasks)
            option = int(input("What would you like to do? 1. New task | 2. Complete task | 3. Delete task | 4. Exit => "))

            if option == 1:
                msg.show_new_task_option()
            elif option == 2:
                msg.show_complete_task_option()
            elif option == 3:
                msg.show_delete_task_option()
            elif option == 4:
                msg.exit_program()
            else:
                print("Option not recognized, please enter a valid number")
    except KeyboardInterrupt:
        print("\nExiting program!")

if __name__ == "__main__":
    db.create_todo_table()
    main()