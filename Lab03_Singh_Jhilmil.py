class Employee:

    def __init__(self, ssn, fname, lname):
        self.__first_name = fname
        self.__last_name = lname
        self.__social = ssn

    def get_social(self):
        return self.__social

    def set_first_name(self, fname):
        self.__first_name = fname

    def set_last_name(self, lname):
        self.__last_name = lname        

    def get_full_name(self):
        return '{:s} {:s}'.format(
            self.__first_name, self.__last_name)

    def __str__(self):
        return 'Name: {:s} SSN: {:d}'.format(
            self.get_full_name(), self.get_social())

class HourlyEmployee(Employee):

    def __init__(self, ssn, fname, lname, hourly_rate):
        super().__init__(ssn, fname, lname)
        self.__hourly_rate = hourly_rate

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate

    def get_hourly_rate(self):
        return self.__hourly_rate

    def __str__(self):
        s = super().__str__()
        s = s + ' Hourly rate: ' + str(self.__hourly_rate)
        return s

class SalariedEmployee(Employee):

    def __init__(self, ssn, fname, lname, salary):
        super().__init__(ssn, fname, lname)
        self.__salary = salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def __str__(self):
        s = super().__str__()
        s = s + ' Salary: ' + str(self.__salary)
        return s
    
def main():

    HEmp1 = HourlyEmployee(123456, 'Sam', 'Hourly Employee', 20)
    SEmp1 = SalariedEmployee(67890, 'Tia', 'Salaried Employee', 75000)

    print(HEmp1)
    print(SEmp1)
    
main()
