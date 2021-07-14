def logged(func):
    def wrapper(*args, **kwargs):
        result = func(*args)
        return f'you called {func.__name__}{args}\nit returned {result}'
    return wrapper


@logged
def bobi(*args):
    return 3 + len(args)


print(bobi(4, 4, 4))
