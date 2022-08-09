
# x = int(input('Enter the amount of time in minutes you want to sleep'))
# if x // 60 == 1:
#    print(x // 60, 'hour')
# elif x // 60 > 1:
#    print(x // 60, 'hours')
# if x % 60 == 1:
#    print(x % 60, 'minute')
# elif x % 60 > 1:
#    print(x % 60, 'minutes')


x = int(input('Enter the amount of time in minutes you want to sleep'))
h = int(input('Hour you fall asleep'))
m = int(input('Minute you fall asleep'))
x += h * 60 + m
print(x // 60, x % 60)
