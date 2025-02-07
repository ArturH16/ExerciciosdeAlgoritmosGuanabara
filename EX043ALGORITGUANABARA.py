from time import sleep
c = 30
while c >= 1:
    if c % 4 == 0:
        print(f'[{c}]')
    else:
        print(f' {c}')
    sleep(1)
    c -= 1
print('Acabou!')