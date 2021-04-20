from time import sleep

def linha():
    print()
    print('=' * 80)
    print()
linha()

for a in range(10, -1, -1):
    print(a)
    sleep(1)
linha()
