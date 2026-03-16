'''
This is my  TODO list. Just for practice.
v0.0.0.1
'''
# Task could propebly be an object, because i dont want to make those manually for each task.
# What should a task include? Surely a name and maybe a description? 


class Task:
    def __init__(self, title, description, id): # if ready add some Timestamp, priority and tags.
        self.title = title
        self.description = description
        self.id = id

    def status(self):
        print(f"{self.title} {self.description} {self.id}")

aufgabe1 = Task("Jesus", "Bitte bring mich um", 0)

aufgabe1.status()

