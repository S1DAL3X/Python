#Python 3.7.7 by S1DAL3X
#Импорт необходимых библиотек (матрицы)
import numpy, math

#Координаты потребителя (исходя из таблицы)
X = 2531
Y = -3126
Z = -4934

#Координаты спутника (исходя из таблицы)
X1 = 10102
X2 = 9779
X3 = 10659
X4 = 7566

Y1 = -9096
Y2 = -12516
Y3 = -13643
Y4 = -4728

Z1 = -22587
Z2 = -21043
Z3 = -19885
Z4 = -23203

#Создание матрицы
R1 = math.sqrt( (X - X1)**2 + (Y - Y1)**2 + (Z - Z1)**2 )
R2 = math.sqrt( (X - X2)**2 + (Y - Y2)**2 + (Z - Z2)**2 )
R3 = math.sqrt( (X - X3)**2 + (Y - Y3)**2 + (Z - Z3)**2 )
R4 = math.sqrt( (X - X4)**2 + (Y - Y4)**2 + (Z - Z4)**2 )

print("\n")
print("Значение R1 = " + str(R1))
print("Значение R2 = " + str(R2))
print("Значение R3 = " + str(R3))
print("Значение R4 = " + str(R4))

H = numpy.array([ [ ((X-X1)/R1), ((Y-Y1)/R1), ((Z-Z1)/R1) ],
                  [ ((X-X2)/R2), ((Y-Y2)/R2), ((Z-Z2)/R2) ],
                  [ ((X-X3)/R3), ((Y-Y3)/R3), ((Z-Z3)/R3) ],
                  [ ((X-X4)/R4), ((Y-Y4)/R4), ((Z-Z4)/R4) ] ])

print("\n")
print("Матрица H: \n" + str(H))

#Перемножение матриц в NumPy осуществляется с помощью функции x.dot(y)
#Numpy.trace - след матрицы (произведение её диагональных элементов)
#PDOP - пространственный геометрический фактор
PDOP = math.sqrt( numpy.trace( (H.transpose()).dot(H) ** (-1) ) )

print("\n")
print("PDOP = " + str(PDOP))

#Определение угломестных координат спутника относительно местоположения потребителя
sin_a1 = ( X*(X1-X)+Y*(Y1-Y)+Z*(Z1-Z) ) / ( math.sqrt(X**2 + Y**2 + Z**2) * R1 )
sin_a2 = ( X*(X2-X)+Y*(Y2-Y)+Z*(Z2-Z) ) / ( math.sqrt(X**2 + Y**2 + Z**2) * R2 )
sin_a3 = ( X*(X3-X)+Y*(Y3-Y)+Z*(Z3-Z) ) / ( math.sqrt(X**2 + Y**2 + Z**2) * R3 )
sin_a4 = ( X*(X4-X)+Y*(Y4-Y)+Z*(Z4-Z) ) / ( math.sqrt(X**2 + Y**2 + Z**2) * R4 )

#Определение угла по значению его синуса
angle1 = math.degrees(math.asin(sin_a1)) #77.32
angle2 = math.degrees(math.asin(sin_a2)) #87.06
angle3 = math.degrees(math.asin(sin_a3)) #87.40
angle4 = math.degrees(math.asin(sin_a4)) #63.02

print("\n")
print("Угол по первому местоположению = " + str(angle1))
print("Угол по второму местоположению = " + str(angle2))
print("Угол по третьему местоположению = " + str(angle3))
print("Угол по четвёртому местоположению = " + str(angle4))
print("\nПо данным значениям угла и рисункам нужно определить задержки\n")

#Определение погрешности измерения псевдодальности Or (сигма(R))
Oef = 10

#Следующие значения Сигма-тр и Сигма-ион смотрелись по рисунку
Otr_1 = 17
Otr_2 = 16
Otr_3 = 16
Otr_4 = 19

Oion_1 = 16
Oion_2 = 16
Oion_3 = 16
Oion_4 = 17

Or_1 = math.sqrt( Oef**2 + Otr_1**2 + Oion_1**2 )
Or_2 = math.sqrt( Oef**2 + Otr_2**2 + Oion_2**2 )
Or_3 = math.sqrt( Oef**2 + Otr_3**2 + Oion_3**2 )
Or_4 = math.sqrt( Oef**2 + Otr_4**2 + Oion_4**2 )

Or_quatro_sum = (Or_1**2 + Or_2**2 + Or_3**2)**2

print("\n")
print("Рассчитанные значения Сигма-R-i соответствуют: ")
print("Сигма-R-1 = " + str(Or_1))
print("Сигма-R-2 = " + str(Or_2))
print("Сигма-R-3 = " + str(Or_3))
print("Сигма-R-4 = " + str(Or_4))

print("\n")
print("Суммарное значение Сигма-R в квадрате = " + str(Or_quatro_sum))

#Определение Сигма-X
Ox = PDOP * math.sqrt(Or_quatro_sum)
print("\n")
print("Рассчитанное значение Сигма-X = " + str(Ox))
