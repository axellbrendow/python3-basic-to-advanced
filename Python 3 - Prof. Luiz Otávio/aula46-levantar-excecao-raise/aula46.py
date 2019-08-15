"""
Lançar exceções - raise
"""

def divide(v1, v2):
    if v2 == 0:
        raise ValueError("O divisor não pode ser zero.")

    return v1 / v2

try:
    print(divide(2, 0))

except ValueError as error:
    print(error)
