import functools


def cache(func):
    log = {}
    func.log = log

    @functools.wraps(func)
    def wrapper(num):
        if num not in log:
            log[num] = func(num)
        return log[num]
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)

