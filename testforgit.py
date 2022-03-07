class Person:
    def __init__(self):
        self.name="John"
        self.height = Height(6,2)
    def __init__(self,name,height):
        self.name=name
        self.height=height
    def display(self):
        print(f"{self.name}")
        self.height.display()

class Height:
    def __init__(self):
        self.feet = 4
        self.inches = 5
    def __init__(self,feet,inches=0):
        self.feet = feet
        self.inches = inches
    def display(self):
        print(f"{self.feet}'{self.inches}\"")
person1 = Person("Greg", Height(2,11))
person2 = Person("Terry", Height(8))
person1.display()
person2.display()

