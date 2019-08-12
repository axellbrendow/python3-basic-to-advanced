"""
for / while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""

i = 0
j = 10

while i < 9:
    print(i, j)
    i += 1
    j -= 1

print('#####################')
# Outra forma interessante de se fazer

for index, value in enumerate(range(10, 1, -1)):

    print(index, value)
