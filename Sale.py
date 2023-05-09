class Sale:
    def __init__(self, salesperson, car, sale_price):
        self.__salesperson = salesperson
        self.__car = car
        self.__sale_price = sale_price

    # Getters
    def get_sale_price(self):
        return self.__sale_price

    def get_car(self):
        return self.__car

    def get_salesperson(self):
        return self.__salesperson

    def get_profit(self):
        # Calculate profit
        return self.__sale_price - self.__car.get_price()

    # Setters
    def set_sale_price(self, sale_price):
        self.__sale_price = sale_price

    def set_car(self, car):
        self.__car = car

    def set_salesperson(self, salesperson):
        self.__salesperson = salesperson