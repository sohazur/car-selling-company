import pickle
import os
from SalesManagement import SalesManagement
from GUI import Application

# Load data function
def load_data():
    sales_management = SalesManagement()

    try:
        with open("employees.pickle", "rb") as employee_file:
            sales_management.employees = pickle.load(employee_file)

        with open("cars.pickle", "rb") as car_file:
            sales_management.cars = pickle.load(car_file)

        with open("sales.pickle", "rb") as sale_file:
            sales_management.sales = pickle.load(sale_file)
    except FileNotFoundError:
        pass

    return sales_management


def load_sample_data(sales_management):
    # Add employees
    if not (os.path.exists("employees.pickle") and os.path.exists("cars.pickle") and os.path.exists("sales.pickle")):
        sales_management.add_employee("Susan Meyers", "47899", "IT", "Manager", 37500)
        sales_management.add_employee("Mark Jones", "39119", "IT", "Salesperson", 26000)
        sales_management.add_employee("Joy Rogers", "81774", "Manufacturing", "Salesperson", 24000)

        # Add cars
        sales_management.add_car("Jazz", "VX3", 55000, "Hatch")
        sales_management.add_car("Mark3", "SX3", 84000, "Sedan")
        sales_management.add_car("Wagoner", "ZX3", 125000, "SUV")

        # Add sales
        sales_management.add_sale("81774", "ZX3", 155000)
        sales_management.add_sale("81774", "VX3", 57800)
        sales_management.add_sale("81774", "VX3", 55000)
        sales_management.add_sale("81774", "SX3", 89000)
        sales_management.add_sale("81774", "SX3", 93000)
        sales_management.add_sale("39119", "VX3", 58000)
        sales_management.add_sale("39119", "VX3", 58000)
        sales_management.add_sale("39119", "ZX3", 158000)
        sales_management.add_sale("39119", "ZX3", 158000)
        sales_management.add_sale("39119", "ZX3", 158000)
        

if __name__ == "__main__":
    sales_management = load_data()

    # Load sample data for testing
    load_sample_data(sales_management)

    app = Application(sales_management)
    app.mainloop()