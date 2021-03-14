def calc(a, b):
    return a + b

def sub_nums(a, b):
    return a - b

def mul_nums(a, b):
    return a * b

def div_nums(a, b):
    return a // b

def main():
    num1 = int(input('Введите число А: '))
    num2 = int(input('Введите число В: '))
    operator = input('Введите операцию: ')
    if operator == '+':
        print(calc(num1, num2))
    elif operator == '-':
        print(sub_nums(num1, num2))
    elif operator == '*':
        print(mul_nums(num1, num2))
    elif operator == '/':
        print(div_nums(num1, num2))


if __name__ == '__main__':
    main()