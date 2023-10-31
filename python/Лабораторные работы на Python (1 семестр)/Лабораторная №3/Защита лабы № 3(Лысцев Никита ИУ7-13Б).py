import math as m

x1, y1 = map(float, input('Введите координаты точки х1 и у1 через пробел: ').split())
x2, y2 = map(float, input('Введите координаты точки х2 и у2 через пробел: ').split())
x3, y3 = map(float, input('Введите координаты точки х3 и у3 через пробел: ').split())
x0, y0 = map(float, input('Введите координаты точки х0 и у0 через пробел: ').split())

l12 = m.sqrt((x2 -x1)**2 + (y2 - y1)**2)
l23 = m.sqrt((x3 -x2)**2 + (y3 - y2)**2)
l31 = m.sqrt((x1 -x3)**2 + (y1 - y3)**2)

l10 = m.sqrt((x0 -x1)**2 + (y0 - y1)**2)
l20 = m.sqrt((x0 -x2)**2 + (y0 - y2)**2)
l30 = m.sqrt((x0 -x3)**2 + (y0 - y3)**2)

hper1 = (l12 + l10 + l20) / 2
hper2 = (l23 + l20 + l30) / 2
hper3 = (l31 + l30 + l10) / 2


S1 = m.sqrt(hper1*(hper1 - l12)*(hper1 - l10)*(hper1 - l20))
S2 = m.sqrt(hper2*(hper2 - l23)*(hper2 - l20)*(hper2 - l30))
S3 = m.sqrt(hper3*(hper3 - l31)*(hper3 - l30)*(hper3 - l10))

height1 = (2*S1) / l12
height2 = (2*S2) / l23
height3 = (2*S3) / l31

max_height = max(height1, height2, height3)

print('Расстояние до наиболее удаленно стороны или ее продолжения равно: {:.5}'.format(max_height))
