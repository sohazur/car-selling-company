import pickle
import os
import tkinter as tk
from tkinter import messagebox, simpledialog
from Salesperson import Salesperson

class AddEmployeeDialog(simpledialog.Dialog):
    def body(self, master):
        self.title("Add Employee")

        tk.Label(master, text="Name:").grid(row=0)
        tk.Label(master, text="ID:").grid(row=1)
        tk.Label(master, text="Department:").grid(row=2)
        tk.Label(master, text="Job Title:").grid(row=3)
        tk.Label(master, text="Basic Salary:").grid(row=4)
        tk.Label(master, text="Age:").grid(row=5)
        tk.Label(master, text="Date of Birth (YYYY-MM-DD):").grid(row=6)
        tk.Label(master, text="Passport Details:").grid(row=7)

        self.name_entry = tk.Entry(master)
        self.id_entry = tk.Entry(master)
        self.department_entry = tk.Entry(master)
        self.job_title_entry = tk.Entry(master)
        self.basic_salary_entry = tk.Entry(master)
        self.age_entry = tk.Entry(master)
        self.date_of_birth_entry = tk.Entry(master)
        self.passport_details_entry = tk.Entry(master)

        self.name_entry.grid(row=0, column=1)
        self.id_entry.grid(row=1, column=1)
        self.department_entry.grid(row=2, column=1)
        self.job_title_entry.grid(row=3, column=1)
        self.basic_salary_entry.grid(row=4, column=1)
        self.age_entry.grid(row=5, column=1)
        self.date_of_birth_entry.grid(row=6, column=1)
        self.passport_details_entry.grid(row=7, column=1)

        return self.name_entry

    def apply(self):
        name = self.name_entry.get()
        id = self.id_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        basic_salary = int(self.basic_salary_entry.get())
        age = int(self.age_entry.get())
        date_of_birth = self.date_of_birth_entry.get()
        passport_details = self.passport_details_entry.get()

        self.result = (name, id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        

class AddCarDialog(simpledialog.Dialog):
    def body(self, master):
        self.title("Add Car")

        tk.Label(master, text="Name:").grid(row=0)
        tk.Label(master, text="ID:").grid(row=1)
        tk.Label(master, text="Price:").grid(row=2)
        tk.Label(master, text="Type:").grid(row=3)

        self.name_entry = tk.Entry(master)
        self.id_entry = tk.Entry(master)
        self.price_entry = tk.Entry(master)
        self.type_entry = tk.Entry(master)

        self.name_entry.grid(row=0, column=1)
        self.id_entry.grid(row=1, column=1)
        self.price_entry.grid(row=2, column=1)
        self.type_entry.grid(row=3, column=1)

        return self.name_entry

    def apply(self):
        name = self.name_entry.get()
        id = self.id_entry.get()
        price = int(self.price_entry.get())
        car_type = self.type_entry.get()
        self.result = (name, id, price, car_type)
        

class AddSaleDialog(simpledialog.Dialog):
    def body(self, master):
        self.title("Add Sale")

        tk.Label(master, text="Employee ID:").grid(row=0)
        tk.Label(master, text="Car ID:").grid(row=1)
        tk.Label(master, text="Sale Price:").grid(row=2)

        self.employee_id_entry = tk.Entry(master)
        self.car_id_entry = tk.Entry(master)
        self.sale_price_entry = tk.Entry(master)

        self.employee_id_entry.grid(row=0, column=1)
        self.car_id_entry.grid(row=1, column=1)
        self.sale_price_entry.grid(row=2, column=1)

        return self.employee_id_entry

    def apply(self):
        employee_id = self.employee_id_entry.get()
        car_id = self.car_id_entry.get()
        sale_price = int(self.sale_price_entry.get())
        self.result = (employee_id, car_id, sale_price, None)
        
        
# Save data function
def save_data(sales_management):
    with open("employees.pickle", "wb") as employee_file:
        pickle.dump(sales_management.employees, employee_file)

    with open("cars.pickle", "wb") as car_file:
        pickle.dump(sales_management.cars, car_file)

    with open("sales.pickle", "wb") as sale_file:
        pickle.dump(sales_management.sales, sale_file)
        

class Application(tk.Tk):
    def __init__(self, sales_management):
        super().__init__()
        self.title("Car Sales Management")
        self.geometry("400x200")

        self.sales_management = sales_management

        self.create_widgets()

    def create_widgets(self):
        # Create buttons for various actions
        add_employee_button = tk.Button(self, text="Add Employee", command=self.add_employee)
        add_employee_button.pack(fill=tk.X)

        add_car_button = tk.Button(self, text="Add Car", command=self.add_car)
        add_car_button.pack(fill=tk.X)

        add_sale_button = tk.Button(self, text="Add Sale", command=self.add_sale)
        add_sale_button.pack(fill=tk.X)

        show_employee_details_button = tk.Button(self, text="Show Employee Details", command=self.show_employee_details)
        show_employee_details_button.pack(fill=tk.X)

        show_car_details_button = tk.Button(self, text="Show Car Details", command=self.show_car_details)
        show_car_details_button.pack(fill=tk.X)

        show_employee_sales_button = tk.Button(self, text="Show Employee Sales", command=self.show_employee_sales)
        show_employee_sales_button.pack(fill=tk.X)

        show_salaries_button = tk.Button(self, text="Show Salaries", command=self.show_salaries)
        show_salaries_button.pack(fill=tk.X)

        save_button = tk.Button(self, text="Save", command=self.save_data)
        save_button.pack(fill=tk.X)

    def add_employee(self):
        dialog = AddEmployeeDialog(self)
        if dialog.result:
            name, id_number, department, job_title, basic_salary, age, date_of_birth, passport_details = dialog.result
            self.sales_management.add_employee(name, id_number, department, job_title, basic_salary, age, date_of_birth, passport_details)

    def add_car(self):
        dialog = AddCarDialog(self)
        if dialog.result:
            name, id, price, car_type = dialog.result
            self.sales_management.add_car(name, id, price, car_type)

    def add_sale(self):
        dialog = AddSaleDialog(self)
        if dialog.result:
            employee_id, car_id, sale_price, error_message = dialog.result
            error_message = self.sales_management.add_sale(employee_id, car_id, sale_price)
            if error_message:
                messagebox.showerror("Error", error_message)

    def show_salaries(self):
        salaries = self.sales_management.calculate_salaries()
        salary_text = "\n".join(f"{self.sales_management.employees[employee_ID].name}: ${salary:.2f}" for employee_ID, salary in salaries.items())
        messagebox.showinfo("Salaries", salary_text)

    def show_employee_details(self):
        employee_id = simpledialog.askstring("Employee Details", "Enter Employee ID:")
        try:
            employee = self.sales_management.employees[employee_id]
            details = f"Name: {employee.name}\nID: {employee.id_number}\nDepartment: {employee.department}\nJob Title: {employee.job_title}\nBasic Salary: ${employee.basic_salary}\nAge: {employee.age}\nDate of Birth: {employee.date_of_birth}\nPassport Details: {employee.passport_details}"
            messagebox.showinfo("Employee Details", details)
        except KeyError:
            messagebox.showerror("Error", "Invalid Employee ID")

    def show_car_details(self):
        car_id = simpledialog.askstring("Car Details", "Enter Car ID:")
        try:
            car = self.sales_management.cars[car_id]
            details = f"Name: {car.name}\nID: {car.ID}\nPrice: ${car.price}\nType: {car.car_type}"
            messagebox.showinfo("Car Details", details)
        except KeyError:
            messagebox.showerror("Error", "Invalid Car ID")

    def show_employee_sales(self):
        employee_id = simpledialog.askstring("Employee Sales", "Enter Employee ID:")
        try:
            employee = self.sales_management.employees[employee_id]
            if isinstance(employee, Salesperson):
                sales_details = "\n".join(f"Car: {sale.car.name} (ID: {sale.car.ID}), Sale Price: ${sale.sale_price}, Profit: ${sale.profit}" for sale in employee.sales)
                if sales_details:
                    messagebox.showinfo("Employee Sales", sales_details)
                else:
                    messagebox.showinfo("Employee Sales", "No sales found for this employee.")
            else:
                messagebox.showerror("Error", "Invalid Employee ID")
        except KeyError:
            messagebox.showerror("Error", "Invalid Employee ID")

    def save_data(self):
        save_data(self.sales_management)
        messagebox.showinfo("Success", "Data saved successfully.")