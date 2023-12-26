import types


def flat_generator(list_of_lists):
    i = 0
    while i != len(list_of_lists):
        j = 0
        while j != len(list_of_lists[i]):
            flat_iterator_item = list_of_lists[i][j]
            j += 1
            yield flat_iterator_item
        i += 1
        if i == len(list_of_lists):
            return

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        if type(flat_iterator_item) == list:
            flat_generator(flat_iterator_item)

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

    return list(flat_generator(list_of_lists_1))


if __name__ == '__main__':
    test_2()
    print(test_2())
