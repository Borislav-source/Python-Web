# Todo You have to comment one of the two variants

# With Iterator
class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == -1:
            raise StopIteration
        number = self.count
        self.count -= 1
        return number


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")


# With Generator
def generator(n):

    while n >= 0:
        yield n
        n -= 1


for i in generator(10):
    print(i)
