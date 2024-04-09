class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary


employee = Employee("John", 50000)
print("Employee Name:", employee.name)
print("Employee Salary:", employee.salary)

employee.salary = 60000
print("Updated Salary:", employee.salary)
