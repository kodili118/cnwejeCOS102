class Employee:

   # constructor
   def __init__(self, name, salary):
      # public instance variable
      self.name = name 


      # private variable
      self.__salary = salary

# creating object of a class
emp = Employee('Ugochi Mbaekwe', 10000)

# accessing public instance variable
print("Name: ",emp.name)

#accessing private instance variable
print('Salary: ', emp._Employee__salary)