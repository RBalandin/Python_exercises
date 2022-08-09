# i = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2
#     print(i)

# i = 0
# while i <= 10:
#     print('*' * i)
#     i = i + 1

# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1

# if int(input()) == 0:

# d = 0
# i = 1
# while i != 0:
#     s = int(input())
#     if s == 0:
#         print(d)
#         exit(0)
#     elif s != 0:
#         d += s

# s = 0
# i = 1
# while i:
#     i = int(input())
#     s += i
# print(s)


# a = int(input())
# b = int(input())
# d = 1
# while d % a > 0 or d % b > 0:
#     d += 1
# print(int(d))


# a, b = int(input()), int(input())
# d = 1
# while d % a != 0 or d % b != 0:
#     d += 1
# print(d)

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1

# i = 1
# while i:
#     a = int(input())
#     if a < 10:
#         continue
#     if a > 100:
#         break
#     if 10 <= a <= 100:
#         print(a)

# n = int(input())
# for i in range(n):
#     print('*' * n)

# x = int(input())
# for _ in range(x):
#     for _ in range(x):
#         print("*", end='')
#     print('', end='\n')

# n = int(input())
# m = int(input())
# for i in range(n):
#     for j in range(m):
#         print('*', end = ' '*i)
#     print()

"""
Lesenka
"""
# for i in range(1, 11):
#     for j in range(i):
#         print(j, end="")
#     print()
import os.path

"""
obratnaya lesenka
"""
# n = 11
# for i in range(n):
#     for j in range(n - i - 1):
#         print(j, end="")
#     print()
"""
lesenka s probelami
"""

# for i in range(10):
#     for j in range(i):
#         print(' ', end=" ")
#     for j in range(10 - i):
#         print(j, end=" ")
#     print()
"""
cifri
"""
# for i in range(1, 10):
#     for j in range(1, 10):
#         if j * i < 10:
#             print(' ', end="")
#
#         print(j * i, end=" ")
#
#     print()
"""
piramida
"""

# for i in range(10):
#     for j in range(10 - i):
#         print(" ", end=" ")
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     for j in range(i-1, 0, -1):
#         print(j, end=" ")
#     print()
"""
stepik
"""
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# for g in range(c, d+1):
#     print('\t'+str(g), end='')
# print(end='\n')
# for i in range(a, b+1):
#     print(str(i)+'\t', end='')
#     for j in range(c, d+1):
#         print(str(i*j), end='\t')
#     print(end='\n')


# a = int(input())
# b = int(input())
# s = 0
# v = 0
# if a % 3 == 1:
#     a += 2
# elif a % 3 == 2:
#     a += 1
# for i in range(a, b+1, 3):
#     s += i
#     v += 1
# print(s / v)

# s = input()
# a = s.lower().count('g'.lower())
# b = s.lower().count('c'.lower())
# c = len(s)
# print((a + b) / c * 100)

# s = input()
# i = 0
# j = len(s) - 1
# is_palindrom = True
# while i < j:
#     if s[i] != s[j]:
#         is_palindrom = False
#         break
#     i += 1
#     j -= 1
# if is_palindrom:
#     print('Yes')
# else:
#     print('No')

# s = input()
# r = s[::-1]
# if s == r:
#     print('Yes')
# else:
#     print('No')

'''
genome
'''
# s = input() + '.'
# p = len(s)
# u = 0
# a = 0
# for i in range(p - 1):
#     if s[u] == s[u + 1]:
#         u += 1
#         a += 1
#     elif s[u] != s[u+1]:
#         a += 1
#         u += 1
#         print(s[u-1] + str(a), end='')
#         a = 0

# genome = input()+' '
# s = 0
# n=genome[0]
# for i in genome:
#     if n!=i:
#         print(n + str(s), end = '')
#         s=0
#         n=i
#     s+=1

'''
sled
'''

# a = [int(i) for i in input().split()]
# b = 0
# for i in a:
#     b += i
# print(b)

# s = 0
# for i in input().split():
#     s += int(i)
# print(s)
'''
sled
'''
# a = sorted([int(i) for i in input().split()])
# box = ''
# for i in range(len(a)-1):
#     if a[i] == a[i+1] and a[i] != box:
#         print(a[i],end=' ')
#         box = a[i]
'''
ILI
'''
# s = [int(i) for i in input().split()]
# s.sort()
# r = []
# for i in range(0,len(s)-1):
#     if s[i] == s[i+1] and (s[i] not in r):
#         r.append(s[i])
# print(*r)
'''
ILI
'''
# a, c = [str(i) for i in input().split()], []
# for i in a:
#     if i not in c and a.count(i) > 1:
#         c.append(i)
#         print(i, end=' ')

'''
drugaya
'''

# a = [int(i) for i in input().split()]
# c = 0
# b = 0
# for i in range(len(a)):
#     if len(a) == 1:
#         print(*a)
#         break
#     if b == len(a) - 1:
#         c = a[0] + a[i - 1]
#         print(c, end=' ')
#         c = 0
#     else:
#         c = a[i + 1] + a[i - 1]
#         print(c, end=' ')
#         c = 0
#         b += 1
'''
EEEEEZZZZZZZZ
'''

# n, m, k = [int(i) for i in input().split()]
# a = [[0 for j in range(m)]for i in range(n)]
# for i in range(k):
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = - 1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()
'''
code is lekcii, saper, no skuchiy
'''

# z = 0
# c = 0
# while True:
#     b = int(input())
#     c += b**2
#     z += b
#     if z == 0:
#         break
# print(c)
'''
sled
'''
# a = int(input())
# i = 0
# b = []
# c = []
# while i < a:
#     i += 1
#     b.append(i)
# for j in range(len(b)+1):
#     c += [j] * j
#     if len(c) > len(b):
#         del c[i:]
#         break
# print(*c)
#
#
# n = int(input())
# a = []
# i = 0
# while len(a) < n:
#     a += [i] * i
#     i += 1
# print(*a[:n])
'''
sled
'''
# a = [int(i) for i in input().split()]
# box = ''
# b = int(input())
# for i in range(len(a)):
#     if a[i] == b:
#         print(i, end=' ')
#         c = a[i]
# if box == '':
#     print('Отсутствует')
#
#
# l = [int(i) for i in input().split()]
# x = int(input())
# if not x in l:
#   print('Отсутствует')
# for i in range(len(l)):
#     if l[i]==x:
#       print(i, end = ' ')
'''
sled
'''
# p = 0
# a = [[int(i) for i in input().split()]]
# b = input()
# while b != 'end':
#     a.append([int(i) for i in b.split()])
#     b = input()
#     p += 1
#
# for i in range(len(a)):
#     for j in range(len(a)): #нужно придумать как обращаться к длине вложенного списка, мб len(a[i])
#         if j == len(a) - 1:
#             if i == p:
#                 print(a[i - 1][j] + a[i][j - 1] + a[i][0] + a[0][j], end=' ')
#             else:
#                 print(a[i][j - 1] + a[i][0] + a[i - 1][j] + a[i + 1][j], end=' ')
#         elif i == p:
#             print(a[i - 1][j] + a[i][j - 1] + a[i][j + 1] + a[0][j], end=' ')
#         else:
#             print(a[i - 1][j] + a[i][j - 1] + a[i][j + 1] + a[i + 1][j], end=' ')
#
#
#     print()

'''
sled
'''
# def min2(a,b):
#     if a <= b:
#         return a
#     else:
#         return b

# def f(n):
#     return n * 10 + 5
# print(f(f(f(10))))

# def f(x):
#     if x <= -2:
#         m = 1 - (x + 2)**2
#     elif -2 < x <= 2:
#         m = - (x / 2)
#     elif 2 < x:
#         m = (x - 2)**2 + 1
#     return m

# l = [0, 1, 2, 3, 4, 5, 6]
# def modify_list(l):
#     n = 0
#     m = l[-1]
#     for x in l[::-1]:
#         if x ==0:
#             n += 1
#             l.append(x)
#             continue
#         elif x % 2 != 0:
#             n += 1
#             continue
#         elif x % 2 == 0:
#            n += 1
#            l.append(x // 2)
#     del l[0:n]
#     l.reverse()
#     return l
# modify_list(l)
# print(l)
'''
ili
'''
# def modify_list(l):
#     l[:] = [i//2 for i in l if i % 2 == 0]
'''
файловый ввод
'''
# inf = open('file.text', 'r')
# inf.close()
#
# with open('text.txt') as inf:

# s = inf.readline().strip()
#
# os.path.join('.', 'dirname', 'filename.txt')

'''
slovari
'''

# def update_dictionary(d, key, value):
#     if key in d:
#         d.update( :value)
