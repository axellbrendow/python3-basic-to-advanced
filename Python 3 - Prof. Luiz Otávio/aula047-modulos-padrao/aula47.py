"""
Módulos são arquivos .py
"""

import sys

print(sys.platform)

from sys import platform

print(platform)

from sys import platform as so

print(so)

##########################

import random

for i in range(5):
    print(random.randint(0, 10), end=' ')

print()

from random import randint, random

for i in range(5):
    print(randint(0, 10), random(), end=' ')

print()
