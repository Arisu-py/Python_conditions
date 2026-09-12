point_x = float(input('Введите абсциссу точки: '))
point_y = float(input('Введите ординату точки: '))

if (point_x ** 2 + point_y ** 2 <= 9) and ((point_y >= -point_x + 3) or (point_y <= point_x - 3)):
    in_shaded_area = True
else:
    in_shaded_area = False

print(in_shaded_area)