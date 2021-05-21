class dictionary_iter:
    def __init__(self, dict):
        self.dict = dict
        self.index = 0
        self. keys = list(self.dict)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.dict):
            raise StopIteration
        index = self.index
        self.index += 1
        key = self.keys[index]
        return key, self.dict[key]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


def generator(seq):
    keys = list(seq)
    index = 0
    while index < len(keys):
        key = keys[index]
        yield key, seq[key]
        index += 1


result = generator({1: "1", 2: "2"})
for x in result:
    print(x)
