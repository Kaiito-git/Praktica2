print("номер 1")
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

print("номер 2")
kat1 = int(input())
kat2 = int(input())
print(1/2 * kat1 * kat2)

print("номер 3")
n = int(input())
maxn = n // 1440
if n >= 1440:
    n = n - 1440 * maxn 
chasn = n // 60
ostatn = n % 60
print(chasn, ostatn)

print("номер 4")
a = int(input())
b = int(input())
L = int(input())
N = int(input())
print(2 * L + (2 * N - 1) * a + 2 * (N - 1) * b)

print("номер 5")
z = int(input())
x = int(input())
y = int(input())
if z < x and z < y:
    print(z)
if x < z and x < y:
    print(x)
if y < x and y < z:
    print(y)

print("номер 6")
print("Введите четыре числа от 1 до 8 включительно")
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if ((x1 + y1) % 2 == (x2 + y2) % 2):
    print("Да")
else:
    print("Нет")

print("номер 7")
year = int(input())
if (year % 4 == 0) and (not(year % 100 == 0)) and (year % 400 == 0):
    print("Да")
else:
    print("Нет")

print("номер 8")
u = int(input())
i = int(input())
o = int(input())
if (not(u == i == o)):
    print("0")
if (u + i + o) / 3 == u:
    print("3")
if (u == i and (not(o == i)) and (not(o == i)) or (u == o and (not(o == i)) and (not(u == i)) or (o == i and (not(u == i)) and (not(o == u)):
    print("2")

print("номер 9")
g = int(input())
h = int(input())
j = int(input())
if (g*h) % k == 0:
    print("можно отломить")
else:
    print("нельзя отломить")
