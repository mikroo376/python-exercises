class Car():
    def __init__(self, productionYear, brand):
        self.productionYear = productionYear
        self.model = brand
    def startEngine(self):
        return print("Starting engine...")
    def StopEngine(self):
        return print("Stopping engine...")


class Honda(Car):
    def __init__(self, model, productionYear, brand):
        self.model = model
        super().__init__(productionYear, brand)



my_car = Car(2010, "Honda")
my_car2 = Car(2018, "BMW")

honda = Honda("Civic", 1995, "Honda")



print(honda.productionYear)