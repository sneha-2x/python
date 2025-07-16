import multiprocessing

square = []

def calc_sqr(numbers):
    global square
    for i in numbers:
        print(i*i)
        square.append(i*i)
    print('Square_list:', square)

def calc_cube(numbers):
    for i in numbers:
        print(i*i*i)

numbers = [2, 3, 4, 5]
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=calc_sqr, args=(numbers,))
    p2 = multiprocessing.Process(target=calc_cube, args=(numbers,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Result:', square)
    print('Done!')




