class Cat:
    def __init__(self, name, type, color, age, stepsWalk, stepsRun):
        self.name = name
        self.type = type
        self.color = color
        self.age = age
        self.stepsWalk = stepsWalk
        self.stepsRun = stepsRun

    def walks(self):
        result = self.code()
        result += f" and i walk  {self.stepsWalk}"
        print(f"{self.code()} and i walk {self.stepsWalk} meters/second")

    def runs(self):
        print(f"{self.code()} and i runs {self.stepsRun} meters/second")

    def code(self):
        result = f" i am {self.name}"
        result += f" i am {self.age} years old "
        result += f" my color is  {self.color}"
        result += f" i am  a {self.type}"
        return result


input("enter eny key for exit .......")
