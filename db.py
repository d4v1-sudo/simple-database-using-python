import sqlite3

# Connect to the 'todo-app' database
# If the database does not exist, it will be created
conn = sqlite3.connect("test.db")

def create_todo_table():
    """Create the 'task' table if it does not exist."""
    cursor = conn.cursor()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS task (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        completed INTEGER
    )
    """)

def add_task(description):
    """Add a new task."""
    conn.execute("INSERT INTO task (description, completed) VALUES (?, 0)", (description,))
    conn.commit()

def remove_task(task_id):
    """Remove the task from the table."""
    conn.execute("DELETE FROM task WHERE task_id = ?", (task_id,))
    conn.commit()

def complete_task(task_id):
    """Mark the task as completed."""
    conn.execute("UPDATE task SET completed = 1 WHERE task_id = ?", (task_id,))
    conn.commit()

def exit_program():
    quit()

def get_tasks():
    """Return the list of registered tasks."""
    return conn.execute("SELECT task_id, description, completed FROM task")
