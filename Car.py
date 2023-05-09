class Car:
    def __init__(self, name, ID, price, car_type):
        self.__name = name
        self.__ID = ID
        self.__price = price
        self.__car_type = car_type

        # Getters

    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__ID

    def get_price(self):
        return self.__price

    def get_car_type(self):
        return self.__car_type

        # Setters

    def set_name(self, name):
        self.__name = name

    def set_ID(self, ID):
        self.__ID = ID

    def set_price(self, price):
        self.__price = price

    def set_car_type(self, car_type):
        self.__car_type = car_type