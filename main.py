'''
This is my  TODO list. Just for practice.
v0.0.0.1
'''
# Task could propebly be an object, because i dont want to make those manually for each task.
# What should a task include? Surely a name and maybe a description? 


class Task:
    def __init__(self, name, description, tag):  #ToDo  What should a task include? Surely a name and maybe a description? I Also added a tag for a status like 'done' true or false, or whatever
        self.name = name
        self.description = description
        self.tag = False

    def __str__ (self): # __str__ is for the string-apperance of an Object
        return f"{self.name, self.description}" # seems like he have to give back a string, so just give him a format.



task1 = Task("Penis", "Das männliche Glied", False)
print(task1) # Is printing the Adress of the Object but why?!
task2 = Task("ding", "einführen", False)
print(task2.tag)
