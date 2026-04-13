import math

r, a = map(float, input().split())
circumference = round(2 * math.pi * r, 2)
circle_area = math.pi * r ** 2
square_area = a ** 2
ratio = round(circle_area / square_area * 100, 2)

print(f"Длина окружности равно {circumference}.\nПлощадь круга составляет {ratio}% от площади квадрата.")
