# Лысцев Н.Д. ИУ7-13Б

# По заданным координатам трех точек на плоскости вычисление сторон
# образованного треугольника и длины биссектрисы проведенной из наибольшего угла.
# Далее вводятся координаты точки, определяется принадлежность точки треугольнику
# Если точка принадлежит треугольнику, то вычисляется расстояние от точки до наиболее
# удаленной стороны треугольника или ее продолжения

# Ввод
# x1, y1 - координаты x1 и y1 первой точки
# x2, y2 - координаты x2 и y2 второй точки
# x3, y3 - координаты x3 и y3 третьей точки
# x0, y0 - координаты x0 и y0 четвертой точки

# Вывод
# length_side_1_2 - Длина стороны, проведенной из точки 1 к точке 2 равна
# length_side_2_3 - Длина стороны, проведенной из точки 2 к точке 3 равна
# length_side_3_1 - Длина стороны, проведенной из точки 3 к точке 1 равна
# bisector_length - Длина биссектрисы, проведенной из наибольшего угла
# largest_height_triangle - Расстояние от точки до наиболее удаленной стороны или ее продолжения

# Импорт библиотеки Python math
import math as m

# Ввод координат трех точек
x1, y1 = map(int, input('Введите координаты  x1 и y1 первой точки через пробел: ').split())
x2, y2 = map(int, input('Введите координаты  x2 и y2 второй точки через пробел: ').split())
x3, y3 = map(int, input('Введите координаты  x3 и y3 третьей точки через пробел: ').split())

# Проверка входных данных
if x1 == x2 == x3 and y1 == y2 == y3:
    print('Неверный ввод! Координаты всех трех точек совпадают.')
elif x1 == x2 and y1 == y2:
    print('Неверный ввод! Координаты первой и второй точки совпадают.')
elif x2 == x3 and y2 == y3:
    print('Неверный ввод! Координаты второй и третьей точки совпадают.')
elif x3 == x1 and y3 == y1:
    print('Неверный ввод! Координаты второй и третьей точки совпадают.')


elif (y2 - y1) == 0 and (y3 - y1) == 0:
    print('''Неверный ввод!Координаты по оси y равны.
                 Точки лежат на одной прямой.''')
elif (x2 - x1) == 0 and (x3 - x1) == 0:
    print('''Неверный ввод!Координаты по оси x равны.
             Точки лежат на одной прямой.''')
elif (x2 - x1) != 0 and (y2 - y1) != 0 and (x3 - x1) / (x2 - x1) == (y3 - y1) / (y2 - y1):
    print('Неверный ввод! Точки лежат на одной прямой.')

elif (x3 - x1) != 0 and (y3 - y1) != 0 and (x2 - x1) / (x3 - x1) == (y2 - y1) / (y3 - y1):
    print('Неверный ввод! Точки лежат на одной прямой.')
else:
    # Вычисление длины сторон образованного треугольника
    length_side_1_2 = m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    length_side_2_3 = m.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    length_side_3_1 = m.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

    print('Длина стороны, проведенной из точки 1 к точке 2 равна: {:.5}'.format(length_side_1_2))
    print('Длина стороны, проведенной из точки 2 к точке 3 равна: {:.5}'.format(length_side_2_3))
    print('Длина стороны, проведенной из точки 3 к точке 1 равна: {:.5}'.format(length_side_3_1))

    # Вычисление квадратов сторон для проверки, является ли треугольник прямоугольным
    squared_length_side_1_2 = (x2 - x1) ** 2 + (y2 - y1) ** 2
    squared_length_side_2_3 = (x3 - x2) ** 2 + (y3 - y2) ** 2
    squared_length_side_3_1 = (x1 - x3) ** 2 + (y1 - y3) ** 2

    # Вычисление периметра треугольника
    perimeter = length_side_1_2 + length_side_2_3 + length_side_3_1

    # Определение максимальной, минимальной и средней по значению длины сторон треугольника
    if length_side_1_2 > length_side_2_3:
        if length_side_2_3 > length_side_3_1:
            largest_length_side = length_side_1_2
            smallest_length_side = length_side_3_1
            middle_length_side = length_side_2_3

        else:
            if length_side_1_2 > length_side_3_1:
                largest_length_side = length_side_1_2
                smallest_length_side = length_side_2_3
                middle_length_side = length_side_3_1

            else:
                largest_length_side = length_side_3_1
                smallest_length_side = length_side_2_3
                middle_length_side = length_side_1_2

    else:
        if length_side_2_3 > length_side_3_1:
            if length_side_1_2 > length_side_3_1:
                largest_length_side = length_side_2_3
                smallest_length_side = length_side_3_1
                middle_length_side = length_side_1_2

            else:
                largest_length_side = length_side_2_3
                smallest_length_side = length_side_1_2
                middle_length_side = length_side_3_1

        else:
            largest_length_side = length_side_3_1
            smallest_length_side = length_side_1_2
            middle_length_side = length_side_2_3

    # Вычисление полу периметра треугольника для его использования
    # при вычислении длины биссектрисы, проведенной из наибольшего угла треугольника
    half_meter = perimeter / 2

    # Вычисление биссектрисы, проведенной из наибольшего угла треугольника
    bisector_length = (
            2 * m.sqrt(smallest_length_side * middle_length_side * half_meter * (half_meter - largest_length_side))
            / (smallest_length_side + middle_length_side))
    print('Длина биссектрисы, проведенной из наибольшего угла равна: {:.5}'.format(bisector_length))

    # Определение, является ли образованный треугольник прямоугольным
    if (squared_length_side_1_2 == squared_length_side_2_3 + squared_length_side_3_1 or
            squared_length_side_2_3 == squared_length_side_1_2 + squared_length_side_3_1 or
            squared_length_side_3_1 == squared_length_side_1_2 + squared_length_side_2_3):
        print('Треугольник является прямоугольным')
    else:
        print('Треугольник не является прямоугольным')

    # Ввод дополнительной (четвертой) точки
    x0, y0 = map(float, input('Введите координаты  x0 и y0  точки через пробел: ').split())

    # Вычисление векторного произведения для определения принадлежности точки треугольнику
    # Векторное произведение вектора, проведенного из 1 точки в точку 0 и вектора, проведенного из точки 1 в точку 2
    vector_product_1 = (x0 - x1) * (y2 - y1) - (y0 - y1) * (
            x2 - x1)
    # Векторное произведение вектора, проведенного из 2 точки в точку 0 и вектора, проведенного из точки 2 в точку 3
    vector_product_2 = (x0 - x2) * (y3 - y2) - (y0 - y2) * (
            x3 - x2)
    # Векторное произведение вектора, проведенного из 3 точки в точку 0 и вектора, проведенного из точки 3 в точку 1
    vector_product_3 = (x0 - x3) * (y1 - y3) - (y0 - y3) * (
            x1 - x3)

    # Если все три векторного произведения > 0, это означает, что точка лежит внутри треугольника
    # Если все три векторного произведения < 0, это означает, что точка лежит внутри треугольника
    # Если хотя бы одно произведение равно нулю, то точка находится на стороне треугольника
    if ((vector_product_1 > 0 and vector_product_2 > 0 and vector_product_3 > 0) or
            (vector_product_1 < 0 and vector_product_2 < 0 and vector_product_3 < 0) or
            (vector_product_1 == 0 or vector_product_2 == 0 or vector_product_3 == 0)):
        print('Точка принадлежит треугольнику ')

        # Вычисление длин векторов, проведенных из вершин треугольника к точке 0
        length_side_1_0 = m.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
        length_side_2_0 = m.sqrt((x0 - x2) ** 2 + (y0 - y2) ** 2)
        length_side_3_0 = m.sqrt((x0 - x3) ** 2 + (y0 - y3) ** 2)

        # Вычисление полу периметров трех треугольников образованных векторами,
        # проведенными из вершин треугольника к точке 0 и сторонами основного треугольника
        half_meter_1_2_0 = (length_side_1_0 + length_side_2_0 + length_side_1_2) / 2
        half_meter_2_3_0 = (length_side_2_0 + length_side_3_0 + length_side_2_3) / 2
        half_meter_3_1_0 = (length_side_3_0 + length_side_1_0 + length_side_3_1) / 2

        # Вычисление площадей трех треугольников образованных векторами,
        # проведенными из вершин треугольника к точке 0 и сторонами основного треугольника
        # с помощью формулы Герона
        triangle_area_1_2_0 = m.sqrt(half_meter_1_2_0
                                     * (half_meter_1_2_0 - length_side_1_0)
                                     * (half_meter_1_2_0 - length_side_2_0)
                                     * (half_meter_1_2_0 - length_side_1_2))

        triangle_area_2_3_0 = m.sqrt(half_meter_2_3_0
                                     * (half_meter_2_3_0 - length_side_2_0)
                                     * (half_meter_2_3_0 - length_side_3_0)
                                     * (half_meter_2_3_0 - length_side_2_3))

        triangle_area_3_1_0 = m.sqrt(half_meter_3_1_0
                                     * (half_meter_3_1_0 - length_side_3_0)
                                     * (half_meter_3_1_0 - length_side_1_0)
                                     * (half_meter_3_1_0 - length_side_3_1))

        # Вычисление расстояний от точки 0 До сторон основного треугольника
        height_triangle_1_2_0 = (2 * triangle_area_1_2_0) / length_side_1_2
        height_triangle_2_3_0 = (2 * triangle_area_2_3_0) / length_side_2_3
        height_triangle_3_1_0 = (2 * triangle_area_3_1_0) / length_side_3_1

        # Выявление максимального расстояния до наиболее удаленной стороны треугольника или ее продолжения
        if height_triangle_1_2_0 > height_triangle_2_3_0:
            if height_triangle_2_3_0 > height_triangle_3_1_0:
                largest_height_triangle = height_triangle_1_2_0

            else:
                if height_triangle_1_2_0 > height_triangle_3_1_0:
                    largest_height_triangle = height_triangle_1_2_0

                else:
                    largest_height_triangle = height_triangle_3_1_0

        else:
            if height_triangle_2_3_0 > height_triangle_3_1_0:
                if height_triangle_1_2_0 > height_triangle_3_1_0:
                    largest_height_triangle = height_triangle_2_3_0

                else:
                    largest_height_triangle = height_triangle_2_3_0

            else:
                largest_height_triangle = height_triangle_3_1_0
        print('Расстояние от точки до наиболее удаленной стороны или ее продолжения равно: {:.5}'.format(
            largest_height_triangle))

    else:
        print('Точка лежит вне треугольника')
