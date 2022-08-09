
# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b + c)/2
# S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#
# print(S)
'''
Drugaya zadacha
'''
# x = int(input())
# if -15 < x <= 12 or 14 < x < 17 or x >= 19:
#     print(True)
# else:
#     print(False)
'''
Drugaya zadacha
'''
# x = float(input())
# y = float(input())
# z = str(input())
# if z == '+':
#     print(x + y)
# elif z == '-':
#     print(x - y)
# elif z == '/' and y > 0:
#     print(x / y)
# elif z == '/' and y == 0:
#     print('Деление на 0!')
# elif z == '*':
#     print(x * y)
# elif z == 'mod' and y > 0:
#     print(x % y)
# elif z == 'mod' and y == 0:
#     print('Деление на 0!')
# elif z == 'pow':
#     print(x ** y)
# elif z == 'div' and y > 0:
#     print(x // y)
# elif z == 'div' and y == 0:
#     print('Деление на 0!')
# else:
#     print('Ya ne umeyu')
'''
Drugaya zadacha
'''
# x = str(input())
# if x == 'треугольник':
#     a, b ,c = int(input()), int(input()), int(input())
#     p = (a + b + c) / 2
#     print(float(p * (p - a) * (p - b) * (p - c)) ** 0.5)
# elif x == 'прямоугольник':
#     a, b = int(input()), int(input())
#     print(float(a * b))
# elif x == 'круг':
#     a = int(input())
#     print(float(3.14 * a**2))
# else:
#     print('ya ne umeyu')
'''
Drugaya zadacha
'''

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a <= b:
#     a, b = b, a
# if b <= c:
#     b, c = c, b
# if a <= b:
#     a, b = b, a
#
# print(a, c, b, sep='\n')
'''
Drugaya zadacha
'''
'''
moe reshenie
'''
# x = str(input())
# if x.endswith('11') or x.endswith('12') or x.endswith('13') or x.endswith('14'):
#     print(x,'программистов')
# elif x.endswith('1'):
#     print(x,'программист')
# elif x.endswith('2') or x.endswith('3') or x.endswith('4'):
#     print(x,'программиста')
# elif x.endswith('0') or x.endswith('5') or x.endswith('6') or x.endswith('7') or x.endswith('8') or x.endswith('9'):
#     print(x, 'программистов')
# elif x.endswith('1'):
#     print(x, 'программист')
# else:
#     print('Ne hochu')
'''
chuzhoe
'''
# i=int(input())
# d=i%10
# h=i%100
# if d==1 and h!=11:
#     s=""
# elif 1<d<5 and not 11<h<15:
#     s="а"
# else:
#     s="ов"
# print(i," программист"+s)
'''
Drugaya zadacha
'''
# x = str(input())
# if int(x[0]) + int(x[1]) + int(x[2]) == int(x[4]) + int(x[5]) + int(x[3]):
#     print('Счастливый')
# else:
#     print('Обычный')
