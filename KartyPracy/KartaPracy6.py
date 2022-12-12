# Zad 1
# a, b, c = int(input()), int(input()), int(input())


# Zad 2
# suma = 0
# for i in range(100, 1000):
#   if i % 8 == 0 and i % 16 != 0:
#     suma = suma + i
# print(suma)

# Zad 3
for i in range(99, 9, -1):
  if i % 7 == 0:
    podzielnik = i
    break

ilosc = 0
for i in range(100, 10000):
  if i % podzielnik == 0:
    ilosc += 1
print(ilosc)

# Zad 4
ilosc = 0
for i in range(10, 100):
  cd = i // 10
  cj = i % 10
  if cd >= 2*cj:
    ilosc = ilosc + 1
print(ilosc)