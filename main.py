import json


class Todo:
    def __init__(self) -> None:
        self.items: list[str] = []
        self._get_tasks()
        self.sort: bool = False

    def _get_tasks(self) -> None:
        with open("data.json") as f:
            data = json.load(f)
            self.items = [task["name"] for task in data["tasks"]]

    @staticmethod
    def delete_task(idx: int) -> bool:
        with open("data.json", "r+") as f:
            data = json.load(f)
            try:
                del data["tasks"][idx-1]
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
            except IndexError:
                print(f"Task with given index ({idx}) is not in the list")
                return False
        return True

    @staticmethod
    def add_task(name: str) -> bool:
        with open("data.json", "r+") as f:
            data = json.load(f)
            data["tasks"].append({"name": name})
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        return True

    def __str__(self) -> str:
        self._get_tasks()
        if not self.items:
            return "Todo list is empty. Add something to it!"
        result: str = ""
        for idx, value in enumerate(self.items):
            result += f"{idx + 1}. {value}\n"
        return result


COMMAND_LIST = "- ADD: Add a task\n- DELETE: Delete task\n" \
               "- DISPLAY: Display tasks\n- EXIT: Exit program\n" \
               "- HELP: Show commands\n"


def run() -> None:
    print("TODO LIST")
    todo_list = Todo()
    print("Available commands: ")
    print(COMMAND_LIST)
    while True:
        command = str(input("Select command: "))
        if command == "EXIT" or command not in ["ADD", "DELETE", "DISPLAY",
                                                "HELP"]:
            print("Thank you for using my program :)")
            exit(0)

        match command:
            case "ADD":
                task_name = str(input("Task name: "))
                if todo_list.add_task(task_name):
                    print("Added task")
                else:
                    print("Could not add task")
            case "DELETE":
                task_id = int(input("Task id: "))
                if todo_list.delete_task(task_id):
                    print("Removed task")
                else:
                    print("Could not remove task")
            case "DISPLAY":
                print(todo_list)
            case "HELP":
                print(COMMAND_LIST)


if __name__ == "__main__":
    run()
