def fat(num, show=False):
    f = 1
    for i in range (num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f

print(fat(5,show=True))