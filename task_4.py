import types

def flat_generator(list_of_lists_2):
    for item in list_of_lists_2:
        if type(item) != list:
            yield item
        else:
            yield from flat_generator(item)

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)

    test_list = list(flat_generator(list_of_lists_2))

    return test_list


if __name__ == '__main__':
    test_4()
    print(test_4())
