num = int(input("número: "))
tot = 0
for i in range(1, num+1):
    if num % i == 0:
        tot += 1
if tot == 2:
    print("O número {} é primo".format(num))
else:
    print("O número {} não é primo".format(num))
