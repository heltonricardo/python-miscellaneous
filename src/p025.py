class LoggingMixin:
    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        with open(self.log_file, 'a', encoding="utf8") as file:
            file.write(f"[{self.__class__.__name__}] {message}\n")


class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} car is being driven.")


class LoggedCar(Car, LoggingMixin):
    def __init__(self, brand, log_file):
        Car.__init__(self, brand)
        LoggingMixin.__init__(self, log_file)


car = LoggedCar("Toyota", "car_log.txt")
car.drive()
car.log("This car is now being driven.")
