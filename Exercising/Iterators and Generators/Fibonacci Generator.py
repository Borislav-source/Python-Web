def fibonacci():
    n = 0
    while True:
        yield n
        n += 1
        if n == 1:
            yield n


generator = fibonacci()
for i in range(5):
    print(next(generator))
