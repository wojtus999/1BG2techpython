# zad 1
s = input()

L = list(s)
a = len(s)-1

print(s[0], s[a])

# zad 2
b = input()
for i in range(1, len(b)-1):
  print(b[i], end=" ")
print()

print(b[1:len(b)-1])

print(b[1:-1])

L = list(b)
L.pop(0)
L.pop(-1)
b = "".join(L)
print(b)

# zad 3
c = input()
L = list(c)
L.reverse()
c = "".join(L)
print(c[:4])