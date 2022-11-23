procent = 6
L = float(input("Długość trwania inwestycji: "))
W0 = int(input("Liczba kasy podanej na inwestycje: "))
W = W0
for i in range(int(L * 12)):
  W = W *(1+(procent/12)/100)
  print(W)