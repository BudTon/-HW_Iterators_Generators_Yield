class FlatIterator:
    def __init__(self, list_of_list):
        self.stack = []
        self.current_list = list_of_list
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.current_list):
            if self.stack:
                self.current_list, self.counter = self.stack.pop()
                return next(self)
            else:
                raise StopIteration

        item = self.current_list[self.counter]
        self.counter += 1

        if type(item) is not list:
            return item
        else:
            self.stack.append((self.current_list, self.counter))
            self.current_list = item
            self.counter = 0
            return next(self)


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    test_list = list(FlatIterator(list_of_lists_2))
    return test_list

if __name__ == '__main__':
    test_3()
    print(test_3())