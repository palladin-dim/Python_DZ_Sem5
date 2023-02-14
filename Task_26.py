'''
Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''
def power(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / power(a, - b)
    if b % 2 == 0:
        return power(a, b // 2) * power(a, b // 2)
    else:
        return a * power(a, b - 1)

a = int(input("Введите число: "))
b = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(a, b))