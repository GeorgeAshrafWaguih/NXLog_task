def addition():
    num1 = float(input("Enter first number for the addition: "))
    num2 = float(input("Enter second number for the addition: "))
    result = num1 + num2
    return print(f'The result of addition is {result}')


def division():
    try:
        num1 = float(input("Enter first number for the division: "))
        num2 = float(input("Enter second number for the division: "))
        result = num1 / num2
        return print(f'The result of division is {result}')
    except ZeroDivisionError as e:
        return print('Unable to divide by Zero')


class Nxlog:

    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    addition()
    division()





