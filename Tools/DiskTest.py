import os
import random
import shutil
import time


def disk_test() -> None:
    i = 0
    t = time.time()
    s = [f for f in os.listdir('null') if f.startswith('null.') and f.endswith('.dat')].__len__() if os.path.exists('null') else 0

    if not os.path.exists('null'):
        os.mkdir('null')

    while True:
        try:
            with open(f'null/null.{random.randint(10**15, 10**16-1)}.dat', 'wb') as f:
                f.seek(10**9-1)
                f.write(b'\x00')
                i += 1
                print(f'\rTotal: {s+i} GB    Speed: {i/(time.time()-t):0>10.6f} GB/s', end='', flush=True)
        except:
            break


def clean() -> None:
    if os.path.exists('null'):
        shutil.rmtree('null')


if __name__ == '__main__':
    disk_test()
    clean()
