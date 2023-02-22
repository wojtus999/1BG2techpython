W = "MMMMMAAARRRRECCZZZEKK"
W = W + "."

# 5M3A4RE2C3ZE2K

ilosc = 1
H = ""
for i in range(len(W) - 1):
  if W[i] == W[i + 1]:
    ilosc += 1
  else:
    if ilosc > 1:
      H += str(ilosc)
    H += W[i]
    ilosc = 1
print(H)

# UŁAMKI

from math import gcd

licz1 = int(input())
mia1 = int(input())
licz2 = int(input())
mia2 = int(input())

wspolny = int(mia1 * mia2 / gcd(mia1, mia2))
licznik = int((wspolny / mia1) * licz1 + (wspolny / mia2) * licz2)
print(str(licznik) + "/" + str(wspolny))
