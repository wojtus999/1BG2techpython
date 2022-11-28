# Sprawdź czy dana liczba jest pierwsza

# n = int(input())
# for i in range(2, int(n**0.5)+1):
#   if n % i == 0:
#     print("NIE JEST PIERWSZA")
#     exit(0)
# print("TAK, LICZBA JEST PIERWSZA")

# Generowanie liczb pierwszych (w przedziale [p, q])

# p, q = int(input()), int(input())

# for j in range(p, q+1):
#   flaga = True
#   for i in range(2, j):
#     if j % i == 0:
#       flaga = False
#       break
#   if flaga == True:
#      print(j, end=" ")

# Generowanie liczb pierwszych (pierwsze n liczb pierwszych)

n = int(input("Podaj ile chcesz liczb pierwszych: "))

k = 2
ilosc = 0
while 1:
  flaga = True
  for i in range(2, k+1):
    if k % i == 0:
        flaga = False
        break
  if flaga == True:
     print(k, end=" ")
     ilosc = ilosc + 1
  if ilosc == n:
    