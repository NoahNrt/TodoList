'''
This is my  TODO list. Just for practice.
v0.0.0.1
'''
# Task could propebly be an object, because i dont want to make those manually for each task.
# What should a task include? Surely a name and maybe a description? 


class Task:

    id_counter = 0

    def __init__ (self, title, description): # if ready add some Timestamp, priority and tags.
        Task.id_counter += 1
        self.id = Task.id_counter
        self.title = title
        self.description = description

    def update (self, title=None, description=None): # Updater for updating a tasks values
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        # I think u will not edit a fucking id.. How dare you! 

    def status (self): # For getting a status
        print(f"{self.title} {self.description} {self.id}")

    def __str__ (self): # just for the ID - I will maybe transform this to a UUID but a shorted one :D
        return f"{self.id}"


aufgabe1 = Task("Jesus", "Bitte bring mich um")
aufgabe1.status()
aufgabe2 = Task("Jesus", "Bitte bring mich um")
aufgabe2.status()
