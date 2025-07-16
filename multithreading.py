import time
import threading

square = []
def sqr_of_num(n):
    global square
    for i in n:
        sqr = i * i
        time.sleep(0.2)
        print(sqr)
        square.append(sqr)


def cub_of_num(n):
    for i in n:
        sqr = i * i * i
        time.sleep(0.2)
        print(sqr)


numbers = [2, 3, 4, 5]

t = time.time()

t1 = threading.Thread(target=sqr_of_num, args=(numbers,))
t2 = threading.Thread(target=cub_of_num, args=(numbers,))

t1.start()
t2.start()

t1.join()
t2.join()

print('Total time is ', time.time() - t)
print(square)
print('Done!')
