

print('Calculator App')

operator = input('Choose | + | - | * | / | : ')
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

add = '+'
minus = '-'
multiply = '*'
divide = '/'

if operator == add:
    print(num1, add, num2, ' = ', num1 + num2)
elif operator == minus:
    print(num1, minus, num2, ' = ', num1 - num2)
elif operator == multiply:
    print(num1, multiply, num2, ' = ', num1 * num2)
elif operator == divide:
    print(num1, divide, num2, ' = ', num1 / num2)
else:
    print('Invalid Operator')
