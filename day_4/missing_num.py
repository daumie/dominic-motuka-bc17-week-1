"""Module docstring"""


def find_missing(arr1, arr2):
    """compares 2 arrays and returns missing elements"""
    new_list = []
    for element in arr1:
        if element not in arr2:
            new_list.append(element)
    for element in arr2:
        if element not in arr1:
            new_list.append(element)
    length_new_list = len(new_list)

    if length_new_list > 0:
        if length_new_list == 1:
            return new_list[0]
        else:
            return new_list
    else:
        return 0


# print(find_missing([2, 3, 3], [2]))
# print(find_missing([2, 3], [2, 3, 4, 5]))
# print(find_missing([2], [2]))
# print(find_missing([], []))
