'''
1. Calculates the user's age in minutes and seconds.
2. Estimates the approximate number of times the user's heart
has beat in his/her lifetime using an average heart rate of
72 beats per minute.
3. Estimates the number of times the person has sneezed in his/her lifetime.
4. Estimates the number of calories that the person has expended in his/her
lifetime (research on the Internet to obtain a daily estimate). Also calculate
the number of sandwiches (or other common food item) that equals that number of calories.
Be creative: Pick several other interesting health-related statistics.
Try searching the Internet to determine how to calculate that data, and
create a program to perform that calculation. The program can ask the user t
o enter any information needed to perform the calculation.
'''

user_age_years = int(input('enter your age in years:\n'))

user_age_days = user_age_years  * 365
user_age_minutes = user_age_days * 1440
user_age_seconds = user_age_minutes * 60

heart_beats_lifetime = 72 * user_age_minutes
print(f'your heart has beat about {heart_beats_lifetime} times in your lifetime')

average_sneezes_lifetime = user_age_days * 4
print(f'your have sneezed about {average_sneezes_lifetime} times in your lifetime')

average_calories_lifetime = user_age_days * 1300
print(f'You have burned about {average_calories_lifetime} calories in your lifetime')

calorie_cookie_count = average_calories_lifetime / 70
print(f"That'a about {calorie_cookie_count:.2f} cookies!")


print(f'You are at least {user_age_days} days old.')

