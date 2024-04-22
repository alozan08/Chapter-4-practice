'''A half-life is the amount of time it takes for a substance or entity to fall to half its original value.
Caffeine has a half-life of about 6 hours in humans. Given caffeine amount (in mg) as input, output the caffeine
level after 6, 12, and 24 hours. Use a string formatting expression with conversion specifiers to output the
caffeine amount as floating-point numbers.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')
'''

caffeine_6_hours = 0
caffeine_12_hours = 0
caffeine_24_hours = 0

initial_caffeine = float(input("Enter your initial caffeine amount:"))
caffeine_6_hours = initial_caffeine / 2
caffeine_12_hours = caffeine_6_hours / 2
caffeine_24_hours = caffeine_12_hours / 4

print(f'Caffeine level after 6 hours: {caffeine_6_hours:.2f}')
print(f'Caffeine level after 12 hours: {caffeine_12_hours:.2f}')
print(f'Caffeine level after 24 hours: {caffeine_24_hours:.2f}')
