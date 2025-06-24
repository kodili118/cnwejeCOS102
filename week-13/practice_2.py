class Internship:

    #constructor
    def __init__(self, name, course, age, reg_no, salary):
        # Public instance variable
        self.name = name 
        self.course = course 



        # private instance variables
        self.__age = age
        self.__reg_no = reg_no 
        self.__salary = salary 
    
    def show (self):
        print('Intern Info:', self.name, self.course, self.__age, self.__reg_no, self.__salary)

    # getter methods
    def get_name(self):
        return self.name
    
    def get_course(self):
        return self.course
    
    def get_age(self):
        return self.__age
    
    def get_reg_no(self):
        return self.__reg_no
    
    def get_salary(self):
        return self.__salary
    
    # setter methods
    def set_age(self, years):
        if years > 25:
            print('Invalid Age. Please enter right age. ')
        else:
            self.__age = years

    def set_reg_no(self, number):
        if number > 2000:
            print('Invalid Reg no. Please enter right Reg no. ')
        else:
            self.__reg_no = number


# creating objects of the class
Info1 = Internship('Chukwudumebi', 'Computer Science', 18, 1062, 1000000)

Info2 = Internship('Ifolochukwu', 'Mass Communication', 17, 1105, 90000)

print(Info1.name)
print(Info1.course)
Info2.show()
print(Info1.get_salary)
