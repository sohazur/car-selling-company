from Employee import Employee

class Salesperson(Employee):
    def __init__(self, name, id_number, department, job_title, basic_salary, age, date_of_birth,passport_details):
        super().__init__(name, id_number, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.__sales = []

    def get_sales(self):
        return self.__sales

    def set_sales(self, sales):
        self.__sales = sales

    def add_sale(self, sale):
        tmp = self.get_sales()
        tmp.append(sale)
        # Update the sales list
        self.set_sales(tmp)

    def calculate_salary(self):
        # Calculate total profit from sales
        total_profit = sum(sale.get_profit() for sale in self.get_sales())
        # Calculate commission
        commission = 0.065 * total_profit
        return self.get_basic_salary() + commission