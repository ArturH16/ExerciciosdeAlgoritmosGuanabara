c = 500
s = 0
while c >= 0:
    print(f'{c} ',end='')
    if c == 0:
        print('= ',end='')
    else:
        print('+ ',end='')
    s += c
    c -= 50
print(f'{s}')