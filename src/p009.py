class Engine:
    def __init__(self, power):
        self.power = power

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        self.__power = power


class Manufacture:
    def __init__(self, legal_name):
        self.legal_name = legal_name

    @property
    def legal_name(self):
        return self.__legal_name

    @legal_name.setter
    def legal_name(self, legal_name):
        self.__legal_name = legal_name


class Car:
    def __init__(self, model):
        self.model = model
        self.engine = None
        self.manufacture = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine):
        self.__engine = engine

    @property
    def manufacture(self):
        return self.__manufacture

    @manufacture.setter
    def manufacture(self, manufacture):
        self.__manufacture = manufacture


e50cv = Engine("50cv")
volks = Manufacture("Volkwagem")

beetle = Car("Beetle")
beetle.engine = e50cv
beetle.manufacture = volks

print(beetle.model, beetle.engine.power, beetle.manufacture.legal_name)
