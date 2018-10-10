
# s = input()
# v = 0
# a = s[:(s.__len__())//3]+' '
# b = s[(s.__len__())//3:2*(s.__len__())//3]+' '
# c = s[2*(s.__len__())//3:s.__len__()]
# string = a+b+c
# s = string.split(' ')
# print(s)
# for e in s:
#     for x in e:
#         if 'a' < x < 'z':
#             v = v + 1
#     if v != 0:
#         print(e)
#         v = 0

import random
import string
s = ''
v = 0
print('input the number of symbols')
N = input()
N = int(N)
print('input the number of signs in slitted parts')
N2 = input()
N2 = int(N2)
for e in range(1, N):
    s = s + random.choice(string.ascii_letters + string.digits)
    if e % N2 == 0:
        s = s + '_'
print(s)

h = s.split('_')
for e in h:
    for x in e:
        if 'a' < x < 'z':
            v = v + 1
    if v != 0:
        print(e)
        v = 0








