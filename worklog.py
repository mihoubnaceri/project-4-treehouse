import os
import task

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def main():

    while True:
        clear()

        print("Welcome to Your Work Log")
        print("""
    Here is you menu choose one of them :
    a) add a Task
    b) search through tasks
    c) quit
        """)
        answer = input("> ")
        if answer.lower() == "a":
            task.add_task()
        elif answer.lower() == "c":
            input("good bye you sure?? ")
            break
        elif answer.lower() == "b":
            print("""What Do you Want to Search by :
a) name
b) task name
c)Minutes spent on Task
e) text from any where
d) date """)
            ask_choice = input("> ")
            if ask_choice == "a":
                clear()

                task.search_task("name")
            elif ask_choice == "b":
                clear()
                task.search_task("task_name")
            elif ask_choice == "c":
                clear()
                task.search_task("minutes")
            elif ask_choice == "d":
                clear()
                task.search_task("date")
            elif ask_choice.lower() == "e":
                clear()
                task.search_task("notes")




            input("done ")
if __name__ == "__main__":
    main()
