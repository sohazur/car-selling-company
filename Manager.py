from Employee import Employee

class Manager(Employee):
    def __init__(self, name, id_number, department, job_title, basic_salary, age, date_of_birth, passport_details):
        super().__init__(name, id_number, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.__salespersons = []

    # Getters
    def get_salespersons(self):
        return self.__salespersons

    # Setters
    def set_salespersons(self, salespersons):
        self.__salespersons = salespersons

    def assign_sale(self, sale):
        for salesperson in self.get_salespersons():
            if sale.get_salesperson() == salesperson:
                break
        else:
            # If the salesperson is not in the list, add them
            tmp = self.get_salespersons()
            tmp.append(sale.get_salesperson())
            self.set_salespersons(tmp)

    def calculate_salary(self):
        # Calculati total profit from sales
        total_profit = sum(sale.get_profit() for salesperson in self.get_salespersons() for sale in salesperson.get_sales() if salesperson.get_department() == self.get_department())
        # Calculate commission
        commission = 0.035 * total_profit
        return self.get_basic_salary() + commission