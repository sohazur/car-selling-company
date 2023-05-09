from Car import Car
from Manager import Manager
from Sale import Sale
from Salesperson import Salesperson

class SalesManagement:
    def __init__(self):
        self.__employees = {}
        self.__cars = {}
        self.__sales = []

    # Getters
    def get_employees(self):
        return self.__employees

    def get_cars(self):
        return self.__cars

    def get_sales(self):
        return self.__sales

    # Setters
    def set_employees(self, employees):
        self.__employees = employees

    def set_cars(self, cars):
        self.__cars = cars

    def set_sales(self, sales):
        self.__sales = sales

    def add_employee(self, name, id_number, department, job_title, basic_salary, age, date_of_birth, passport_details):
        # Job title is only valid if it is either "manager" or "salesperson"
        if job_title.lower() == "manager":
            employee = Manager(name, id_number, department, job_title, basic_salary, age, date_of_birth, passport_details)
        elif job_title.lower() == "salesperson":
            employee = Salesperson(name, id_number, department, job_title, basic_salary, age, date_of_birth, passport_details)
        else:
            print("Invalid job title. Employee not added.")
            return
        # Add employee to list of employees
        tmp = self.get_employees()
        tmp[id_number] = employee
        self.set_employees(tmp)
        tmp = self.get_employees()
        tmp[id_number] = employee
        self.set_employees(tmp)

    def add_car(self, name, id_number, price, car_type):
        car = Car(name, id_number, price, car_type)
        tmp = self.get_cars()
        tmp[id_number] = car
        # Add car to list of cars
        self.set_cars(tmp)

    def add_sale(self, employee_id, car_id, sale_price):
        try:
            employee = self.get_employees()[employee_id]
            car = self.get_cars()[car_id]

            if isinstance(employee, Salesperson):
                sale = Sale(employee, car, sale_price)
                tmp = self.get_sales()
                tmp.append(sale)
                self.set_sales(tmp)

                # Add sale to salesperson's sales list
                employee.add_sale(sale)

                # Assign sale to the manager if applicable
                manager = self.find_manager(employee)
                if manager:
                    manager.assign_sale(sale)
            else:
                return "Invalid Employee ID"
        except KeyError:
            return "Invalid Employee/Car ID"
    
    def modify_employee(self, id_number, attribute, new_value):
        try:
            employee = self.get_employees()[id_number]
            if attribute == "name":
                employee.set_name(new_value)
            elif attribute == "id_number":
                employee.set_id_number(new_value)
            elif attribute == "department":
                employee.set_department(new_value)
            elif attribute == "job_title":
                employee.set_job_title(new_value)
            elif attribute == "basic_salary":
                employee.set_basic_salary(new_value)
            elif attribute == "age":
                employee.set_age(new_value)
            elif attribute == "date_of_birth":
                employee.set_date_of_birth(new_value)
            elif attribute == "passport_details":
                employee.set_passport_details(new_value)
            else:
                return "Invalid attribute"
        except KeyError:
            return "Invalid Employee ID"

    def delete_employee(self, id_number):
        try:
            del self.get_employees()[id_number]
        except KeyError:
            return "Invalid Employee ID"

    def modify_car(self, id_number, attribute, new_value):
        try:
            car = self.get_cars()[id_number]
            if attribute == "name":
                car.set_name(new_value)
            elif attribute == "ID":
                car.set_ID(new_value)
            elif attribute == "price":
                car.set_price(float(new_value))
            elif attribute == "car_type":
                car.set_car_type(new_value)
            else:
                return "Invalid attribute"
        except KeyError:
            return "Invalid Car ID"

    def delete_car(self, id_number):
        try:
            del self.get_cars()[id_number]
        except KeyError:
            return "Invalid Car ID"

    # finding manager for a given employee
    def find_manager(self, employee):
        for manager in self.get_employees().values():
            if isinstance(manager, Manager) and manager.get_department() == employee.get_department():
                return manager
        return None

    def calculate_salaries(self):
        salaries = {}
        # Calculate salaries for all employees
        for employee in self.get_employees().values():
            if isinstance(employee, Salesperson):
                salaries[employee.get_id_number()] = employee.calculate_salary()
            elif isinstance(employee, Manager):
                salaries[employee.get_id_number()] = employee.calculate_salary()

        return salaries