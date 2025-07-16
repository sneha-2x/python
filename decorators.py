import argparse

def postive_only(func):
    def checker(n):
        if not isinstance(n, int) or n < 0:
            raise argparse.ArgumentTypeError('number must be positive')
        return func(n)
    return checker

@postive_only
def fact(num):
    if num == 1 or 0:
        return 1
    return num * fact(num - 1)

print(fact(5))
print(fact(2.5))
print(fact(-1))
