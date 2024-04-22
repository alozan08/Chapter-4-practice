'''
Given 4 floating-point numbers. Use a string formatting expression with conversion specifiers to
output their product and their average as integers (rounded), then as floating-point numbers.

Output each rounded integer using the following:
print(f'{your_value:.0f}')

Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.3f}')'''

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

result = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4
print(f'{result:.0f} {average:.0f}')
print(f'{result:.3f} {average:.3f}')