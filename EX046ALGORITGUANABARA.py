c = 6
s = 0
while c <= 100:
    print(f'{c} ',end='')
    if c == 100:
        print('= ',end='')
    else:
        print('+ ',end='')
    s += c
    c += 2
print(f'{s}')