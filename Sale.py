class Sale:
    def __init__(self, salesperson, car, sale_price):
        self.salesperson = salesperson
        self.car = car
        self.sale_price = sale_price
        self.profit = sale_price - car.price