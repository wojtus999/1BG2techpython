# Zad 1
# n = int(input())
# suma = 0
# while n > 0:
#   cyfra = n % 10
#   suma = suma + cyfra
#   n = n // 10
# print(suma)

# Zad 2
# wersja 1
# n = int(input())
# flaga = True
# for i in range(2,n):
#   if n % i == 0:
#     flaga = False
# if flaga == True:
#   print("TAK")
# else:
#   print("NIE")
  
# wersja 2
# n = int(input())
# for i in range(2, n):
#   if n % i == 0:
#     print("NIE")
#     exit(0)
# print("TAK")

# wersja 3
# n = int(input())
# suma = 0
# for i in range(2,n):
#   suma = suma + i
# if suma == 0:
#   print("TAK")
# else:
#   print("NIE")

# Zad 3
# n = int(input())
# suma = 0
# for i in range(1,n):
#   if n % i == 0:
#     suma = suma + i
#   if suma == n:
#     print("TAK, jest doskonała")
#   else:
#     print("NIe,nie jest doskonała")

# Zad 4
# x = int(input())
# y = int(input())
# while x != y:
#   if x > y : x = x - y
#   if y > x : y = y - x
# if x == 1:
#   print("TAK")
# else:
#   print("NIE")

# Zad 5
# m = int(input())

# for i in range(10, 20):
#   x, y = i, m
#   while y > 0:
#     x, y = y, x%y
#   if x == 1:
#     print(f"TAK, {i} i {m} są względnie pierwsze")
#   else:
#     print(f"NIE, {i} i {m} nie są względnie pierwsze")