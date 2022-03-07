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

    def display(self):
        print(f"{self.feet}'{self.inches}\"")
person1 = Person("Greg", Height(2,11))
person4 = Person("John", Height(5))
person2 = Person("Terry", Height(6))
person1.display()
person2.display()

person3 = Person("Chris", Height(6,2))
person3.display()


# I like making changes

person5 = Person("Edgar", Height())