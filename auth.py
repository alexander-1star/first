class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def get_salary_info(self):
        return f"Salary {self.name}: {self.salary}: {self.role}"

employee = Employee("Bob", "Engineer", 1200)
print(employee.get_salary_info())

