#fibonacci

print('Fibonacci series...')
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for i in fib():
    if i> 50:
        break
    print(i)

print('End')

print("Squares list...")
def sqr():
    num = 1
    while True:
        yield num * num
        num += 1

for i in sqr():
    if i > 999:
        break
    else:
        print(i)

