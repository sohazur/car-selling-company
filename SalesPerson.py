from Employee import Employee

class Salesperson(Employee):
    def __init__(self, name, id_number, department, job_title, basic_salary):
        super().__init__(name, id_number, department, job_title, basic_salary)
        self.sales = []

    def add_sale(self, sale):
        self.sales.append(sale)

    def calculate_salary(self):
        total_profit = sum(sale.profit for sale in self.sales)
        commission = 0.065 * total_profit
        return self.basic_salary + commission