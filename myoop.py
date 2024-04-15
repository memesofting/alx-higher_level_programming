class Car:
    def __init__(self, color, weight, ev):
        print("The init function is called")
        print(color, weight, ev)

        self.color = color
        self.weight = weight
        self.isEv = ev

car1 = Car("blue", 34, True)
