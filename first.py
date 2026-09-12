from math import (
log, exp, tan,
)


a, b, x = map(float, input('Введите числа a, b, x через пробел: ').split())

if abs(a - b ** 2) > b:
    if a * x - b == 0:
        y = 'Error ln(0)'
    else:
        y = log(abs(a * x - b)) - exp(tan(x))
else:
    y = tan(4 * x) - a

print(y)
