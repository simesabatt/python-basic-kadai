class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は大人です")
        else:
            print(f"{self.name}は未成年です")

people = [
    Human("Alice", 25),
    Human("Bob", 17),
    Human("Charlie", 30),
    Human("Diana", 19)
]

for person in people:
    person.check_adult()
