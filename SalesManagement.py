from Car import Car
from Manager import Manager
from Sale import Sale
from Salesperson import Salesperson

class SalesManagement:
    def __init__(self):
        self.employees = {}
        self.cars = {}
        self.sales = []

    def add_employee(self, name, id_number, department, job_title, basic_salary, age, date_of_birth, passport_details):
        if job_title.lower() == "manager":
            employee = Manager(name, id_number, department, job_title, basic_salary, age, date_of_birth, passport_details)
        elif job_title.lower() == "salesperson":
            employee = Salesperson(name, id_number, department, job_title, basic_salary, age, date_of_birth, passport_details)
        else:
            print("Invalid job title. Employee not added.")
            return
        self.employees[id_number] = employee

    def add_car(self, name, id_number, price, car_type):
        car = Car(name, id_number, price, car_type)
        self.cars[id_number] = car

    def add_sale(self, employee_id, car_id, sale_price):
        try:
            employee = self.employees[employee_id]
            car = self.cars[car_id]

            if isinstance(employee, Salesperson):
                sale = Sale(employee, car, sale_price)
                self.sales.append(sale)

                # Add sale to salesperson's sales list
                employee.add_sale(sale)

                # Assign sale to the manager if applicable
                manager = self.find_manager(employee)
                if manager:
                    manager.assign_sale(sale)
            else:
                return "Invalid Employee ID"
        except KeyError:
            return "Invalid Employee ID"

    def find_manager(self, employee):
        for manager in self.employees.values():
            if isinstance(manager, Manager) and manager.department == employee.department:
                return manager
        return None

    def calculate_salaries(self):
        salaries = {}
        for employee in self.employees.values():
            if isinstance(employee, Salesperson):
                salaries[employee.id_number] = employee.calculate_salary()
            elif isinstance(employee, Manager):
                salaries[employee.id_number] = employee.calculate_salary()

        return salaries