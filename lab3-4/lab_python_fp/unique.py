from gen_random import gen_random


class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(sorted(items))
        self.db = set()

    def __next__(self):
        while True:
            cur = next(self.items)
            cur = cur.lower() if self.ignore_case and isinstance(cur, str) else cur
            if cur not in self.db:
                self.db.add(cur)
                return cur

    def __iter__(self):
        return self


def main():
    data1 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    data2 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data3 = gen_random(10, 1, 3)

    print(list(Unique(data1, ignore_case=False)))
    print(list(Unique(data1, ignore_case=True)))
    print(list(Unique(data2, ignore_case=False)))
    print(list(Unique(data3, ignore_case=False)))


if __name__ == '__main__':
    main()