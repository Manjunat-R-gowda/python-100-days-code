class Car:
    def __init__(self,car_name,model):
        self.car_name=car_name
        self.__model=model

    def engine(self):
        print(f"engine started {self.car_name} {self.__model}")

    def move(self):
        print("car is moving")

    def place(self):
        print("car is placed")

d = Car("toyoto",2008)

dv = Car("red car",2022)
d.engine()
d.move()
d.place()
dv.engine()
dv.move()
dv.place()




