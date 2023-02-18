t = int(input("Primeiro termo: "))
r = int(input("Razão: "))
c = 0
while c < 10:
    print("{} > ".format(t), end="")
    t += r
    c += 1
print("\033[0;31mFIM \033[m")
