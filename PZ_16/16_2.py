# Создайте класс "Автомобиль", который содержит информацию о марке, модели и годе выпуска.
# Создайте класс "Грузовик", который наследуется от класса "Автомобиль" и содержит информацию о грузоподъемности.
# Создайте класс "Легковой автомобиль", который наследуется от класса "Автомобиль" и
# содержит информацию о количестве пассажиров.
try:
    class Car:
        def __init__(self, brand, model, year):
            self.brand = brand
            self.model = model
            self.year = year

        def info(self):
            return f"{self.brand} {self.model}, {self.year}"


    class Truck(Car):
        def __init__(self, brand, model, year, load_capacity):
            super().__init__(brand, model, year)
            self.load_capacity = load_capacity

        def info(self):
            return f"{super().info()}, load capacity: {self.load_capacity} kg"


    class PassengerCar(Car):
        def __init__(self, brand, model, year, passenger_capacity):
            super().__init__(brand, model, year)
            self.passenger_capacity = passenger_capacity

        def info(self):
            return f"{super().info()}, passengers: {self.passenger_capacity}"


    truck = Truck("Kamaz", "6520", 2020, 15000)
    passenger_car = PassengerCar("Toyota", "Camry", 2022, 5)

    print(truck.info())
    print(passenger_car.info())

except ValueError:
    print("Ошибка")