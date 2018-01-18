from peewee import *
import datetime


db = SqliteDatabase('tasks.db')

class Task(Model):
    name = CharField(max_length = 255)
    task_name = CharField(max_length = 255)
    minutes = IntegerField()
    notes = TextField()
    time_stamp = DateField(default = datetime.datetime.now().date)
    class Meta:
        database = db

db.connect()
db.create_tables([Task],safe = True)

def add_task():
    name = input("Type on your name ")
    task_name = input("Type in the name of Task ")
    minutes = int(input("Minutes Spent on task: "))
    notes = input("Additional notes ? (optional) ")

    Task.create(name = name,task_name =task_name,minutes = minutes,notes = notes)

def search_task(search_query =None):
    entries = Task.select()
    if search_query:
        if search_query == "date":
            while True:
                date = input("Type in date to search Pleas use MM/DD/YYYY HH:MM FORMAT ")
                try:
                    local_date =datetime.datetime.strptime(date, "%Y-%m-%d")
                except ValueError:
                    print("{} aint a valid format for date ".format(date))
                else:

                    entries = entries.where(Task.time_stamp == date)
                    break
        elif search_query == "name":
            name = input("name to search : ")
            entries = entries.where(Task.name.contains(name))
        elif search_query == "task_name":
            name = input("Task name to search : ")
            entries = entries.where(Task.task_name.contains(name))
        elif search_query == "minutes":
            name = int(input("minutes spent to search : "))

            entries = entries.where(Task.minutes == name)
        elif search_query == "notes":
            ask = input("Text to look for ")
            entries = entries.where(Task.notes.contains(ask) | Task.name.contains(ask) | Task.task_name.contains(ask)  )
    for entry in entries:
        print("""name is: {},
Task name : {} ,
Minutes Spent : {},
Notes : {} ,
Date on : {} """.format(entry.name,entry.task_name,entry.minutes,entry.notes,entry.time_stamp))
        print("\n" * 3)
