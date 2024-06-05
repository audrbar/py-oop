from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_pay(self):
        pass

    @abstractmethod
    def get_role(self):
        pass


class Manager(Employee):

    def calculate_pay(self):
        pass

    def get_role(self):
        pass


class Engineer(Employee):

    def calculate_pay(self):
        pass

    def get_role(self):
        pass


class Intern(Employee):

    def calculate_pay(self):
        pass

    def get_role(self):
        pass
