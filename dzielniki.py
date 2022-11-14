n = int(input())
licznik = 0
for i in range(1, n+1):
  if n % i == 0:
    licznik += 1

if licznik == 0:
  print("Liczba jest pierwsza")
else:
  print("Liczba nie jest pierwsza")
    