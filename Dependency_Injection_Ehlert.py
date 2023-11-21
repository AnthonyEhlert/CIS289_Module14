"""
Program Name: Dependency_Injection_Ehlert.py
Author: Tony Ehlert
Date: 11/21/2023

Program Description:  This program contains two classes CrossFitCoach and Certification.  The CrossFitCoach class
utilizes dependency injection of the Certification class.  The program creates a Certification object that is then used
in the creation of a CrossFitCoach object.
"""


#### Create a class of your choice with at least 3 attributes and 1 method
class CrossFitCoach:
    def __init__(self, name, age, certification):
        self.name = name
        self.age = age
        self.certification = certification

    def encourage_client(self):
        return 'You\'re doing great!'

    def __repr__(self):
        return f"CrossFitCoach('{self.name}', {self.age}, {self.certification.__repr__()})"


#### Create another class that your initial class relies on for one of the attributes
class Certification:
    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return f"Certification('{self.type}')"


#### Create an object from your class
crossfit_kids_cert = Certification('CrossFit Kids')

#### Use dependency injection to create another object
morning_coach = CrossFitCoach('Tony Ehlert', 37, crossfit_kids_cert)

print(morning_coach)
