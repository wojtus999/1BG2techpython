
# Zad 1

W = "GGGGEEETTWWWWWWHHH"
W = W + "."

# 4G3E2T6W3H

ilosc = 1
H = ""
for i in range(len(W) - 1):
  if W[i] == [i + 1]:
    ilosc += 1
  else:
    if ilosc > 1:
      H += str(ilosc)
    H += W[i]
    ilosc = 1
print(H)

# Zad 2

from math import gcd
licz1 = int(input())
mia1 = int(input())
licz2 = int(input())
mia2 = int(input())
licz3 = int(input())
mia3 = int(input())

wspolny = int(mia1 * mia2 * mia3 / gcd(mia1, mia2, mia3))
licznik = int((wspolny / mia1) * licz1 + (wspolny / mia2) * licz2 + (wspolny / mia3) * licz3)
print(str(licznik) + "/"  + str(wspolny))