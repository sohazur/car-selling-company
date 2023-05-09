from Employee import Employee

class Manager(Employee):
    def __init__(self, name, id_number, department, job_title, basic_salary, age, date_of_birth, passport_details):
        super().__init__(name, id_number, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.salespersons = []

    def assign_sale(self, sale):
        for salesperson in self.salespersons:
            if sale.salesperson == salesperson:
                salesperson.add_sale(sale)
                break
        else:
            self.salespersons.append(sale.salesperson)
            sale.salesperson.add_sale(sale)

    def calculate_salary(self):
        total_profit = sum(sale.profit for salesperson in self.salespersons for sale in salesperson.sales if salesperson.department == self.department)
        commission = 0.035 * total_profit
        return self.basic_salary + commission