"""
Program Name: Simple_Factory_Ehlert.py
Author: Tony Ehlert
Date: 11/20/2023

Program Description: This program utilizes the Factory Method pattern to create objects of two different classes.
"""


#### Build a class that includes a factory
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __repr__(self):
        return f"Employee('{self.first_name}', '{self.last_name}', {self.salary})"

    @classmethod
    def employee_factory(cls, class_name):
        return type(class_name, (cls,),
                    {'__repr__': lambda self: f"{class_name}('{self.first_name}', '{self.last_name}', {self.salary})"})


#### Create an object from the class
basic_employee = Employee('Tony', 'Stark', 50000)

#### Print the object attributes
print('basic_employee object attributes:')
print(f'First Name: {basic_employee.first_name}')
print(f'Last Name: {basic_employee.last_name}')
print(f'Salary: ${basic_employee.salary}')
print()

#### Utilize the factory to create a new class
Supervisor = Employee.employee_factory('Supervisor')

#### Create an object from the new class
morning_supervisor = Supervisor('Steve', 'Rogers', 75000)

#### Print the object attributes
print('morning_supervisor object attributes:')
print(f'First Name: {morning_supervisor.first_name}')
print(f'Last Name: {morning_supervisor.last_name}')
print(f'Salary: ${morning_supervisor.salary}')
