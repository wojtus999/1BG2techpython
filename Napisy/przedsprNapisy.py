# zad 1
# s = input()

# L = list(s)
# a = len(s)-1

# print(s[0], s[a])

# zad 2
# b = input()
# for i in range(1, len(b)-1):
#   print(b[i], end=" ")
# print()

# print(b[1:len(b)-1])

# print(b[1:-1])

# L = list(b)
# L.pop(0)
# L.pop(-1)
# b = "".join(L)
# print(b)

# zad 3
# c = input()
# L = list(c)
# L.reverse()
# c = "".join(L)
# print(c[:4])

#zad 4 (średnia z liter)
# d= input()
# s = 0
# for x in d:
#   s += ord(x)
# znak = s // len(d)
# print(chr(znak))

# zad 5
# e = input()
# ilosc = 0
# for x in e:
#   if x == "A":
#     ilosc += 1
# print(ilosc)

# SAMO = ["A", "E", "I", "O", "U", "Y"]

# ilosc_samo = 0
# for x in e:
#   if x in SAMO:
#       ilosc_samo += 1
# print(ilosc_samo)

# zad 6 (dominująca, czyli ta której jest najwięcej + jej ilość)
# f = input()
# maksiu = 0
# for x in f:
#   if f.count(x) > maksiu:
#      maksiu = f.count(x)
#      literka = x
# print(literka, maksiu)

# zad 8
h = input()
ilosc = 0
for i in range(len(h)):
  if h[i:i+2] == "LA":
      ilosc += 1
if ilosc == 3:
  print("TAK")
else:
  print("NIE")