class Employee:
    def __init__(self, name, id_number, department, job_title, basic_salary, age, date_of_birth, passport_details):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title
        self.__basic_salary = basic_salary
        self.__age = age
        self.__date_of_birth = date_of_birth
        self.__passport_details = passport_details

    # Getters
    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def get_basic_salary(self):
        return self.__basic_salary

    def get_age(self):
        return self.__age

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_passport_details(self):
        return self.__passport_details

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def set_basic_salary(self, basic_salary):
        self.__basic_salary = basic_salary

    def set_age(self, age):
        self.__age = age

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def set_passport_details(self, passport_details):
        self.__passport_details = passport_details