# Employee and Production Worker Class
# Gerald Brady
# 11/23/2022

class Employee:

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def set_name(self, name):
        self.name = name

    def set_number(self, number):
        self.number = number

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number


class ProductionWorker(Employee):

    def __init__(self, name, number, shift_num, pay_rate):
        Employee.__init__(self, name, number)
        self.shift_num = shift_num
        self.pay_rate = pay_rate

    def set_shift_num(self, shift_num):
        self.shift_num = shift_num

    def set_pay_rate(self, pay_rate):
        self.pay_rate = pay_rate

    def get_shift_num(self):
        return self.shift_num

    def get_pay_rates(self):
        return self.pay_rate


def main():
    print('Please enter employee info...')

    employee_name = input("Employee's Name: ")
    employee_num = input("Employee's Number: ")
    shift_num = input("Employee's Shift Number: ")
    pay_rate = input("Employee's Pay Rate: ")

    employee = ProductionWorker(employee_name, employee_num, shift_num, pay_rate)

    print('Employee:' + employee.get_name(), 'Number:' + employee.get_number(),
          'Shift:' + employee.get_shift_num(), '$' + employee.get_pay_rates() + '/hr')


if __name__ == '__main__':
    main()
