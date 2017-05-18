"""Binary seaerch module docstring here"""


def binary_search(given_list, item):
    """implements binary search by factorial strategy"""
    sorted_given_list = sorted(given_list)
    len_sorted = len(sorted_given_list)
    if len_sorted == 0:
        return False
    else:
        midpoint = len_sorted // 2

    if sorted_given_list[midpoint] == item:
        return True
    else:
        if item < sorted_given_list[midpoint]:
            return binary_search(sorted_given_list[:midpoint], item)
        else:
            return binary_search(sorted_given_list[midpoint + 1:], item)


# TEST_LIST = [21, 27, 32, 33, 42, 47, 58, 69, 70, 77, 79]
# print(binary_search(TEST_LIST, 3))
# print(binary_search(TEST_LIST, 69))
