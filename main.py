def calc(a, b):
    return a + b


def main():
    num1 = int(input('Введите число А: '))
    num2 = int(input('Введите число В: '))
    operator = input('Введите операцию: ')
    if operator == '+':
        print(calc(num1, num2))

if __name__ == '__main__':
    main()