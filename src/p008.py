import sys

from p007 import read_as_json, write_as_json


FILE_PATH = 'tasks.json'


def show(tasks):
    active_tasks = list(filter(lambda t: t["active"], tasks))
    if not active_tasks:
        print("- Empty list -")
        return
    active_tasks_values = map(lambda t: f"* {t['value']}", active_tasks)
    print(*active_tasks_values, sep='\n', end='\n')


def undo(tasks):
    try:
        first_active_task = next(
            filter(lambda t: t["active"], reversed(tasks)))
    except StopIteration:
        print("- Nothing to undo -")
    else:
        first_active_task["active"] = False
        write_as_json(FILE_PATH, tasks)
        print("Undone:", first_active_task["value"])


def redo(tasks):
    try:
        first_inactive_task = next(
            filter(lambda t: not t["active"], reversed(tasks)))
    except StopIteration:
        print("- Nothing to redo -")
    else:
        first_inactive_task["active"] = True
        write_as_json(FILE_PATH, tasks)
        print("Redone:", first_inactive_task["value"])


def add(entered_task, tasks):
    tasks.append({"value": entered_task, "active": True})
    write_as_json(FILE_PATH, tasks)
    print("Added:", entered_task)


try:
    tasks = read_as_json(FILE_PATH)
except FileNotFoundError:
    tasks = []

while True:

    print("Commands: show | undo | redo | exit")
    user_input = input("Enter a task or a command: ").strip()

    commands = {
        "show": lambda: show(tasks),
        "undo": lambda: undo(tasks),
        "redo": lambda: redo(tasks),
        "exit": lambda: sys.exit(),
    }

    command = commands.get(user_input) or (lambda: add(user_input, tasks))
    command()

    print()
