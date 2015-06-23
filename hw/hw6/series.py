def fibonacci(n):
    # return nth value in Fibonacci Series with seed value 0, 1
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    # return nth value in Lucas Numbers with seed value 2, 1
    if (n == 0):
        return 2
    elif (n == 1):
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(x, y=0, z=1):
    #  use seed values to decide which function to use
    if (y == 0) and (z == 1):
        return fibonacci(x)
    elif (y == 2) and (z == 1):
        return lucas(x)
    else:
        print('other series')

if (__name__ == '__main__'):
    # validate against 10th value
    assert fibonacci(10) == 55
    assert lucas(10) == 123
    assert sum_series(10) == 55
    assert sum_series(10,2,1) == 123
