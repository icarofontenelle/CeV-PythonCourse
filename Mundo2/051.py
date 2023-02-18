p = int(input("primeiro termo: "))
r = int(input("razão: "))
t = p + (10 - 1) * r
for i in range(p, t+r, r):
    print(i, end=" ")

