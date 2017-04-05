def binary_search(given_list, item):
    first_item = 0
    last_item = len(given_list) - 1
    found = False

    while first_item <= last_item and not found:
        midpoint = (first_item + last_item) // 2
        if given_list[midpoint] == item:
            found = True
        else:
            if item < given_list[midpoint]:
                last_item = midpoint - 1
            else:
                first_item = midpoint - 1
                return found
test_list = [21,27,32,33,42,47,58,69,70,77,79]
print(binary_search(test_list,3))
print(binary_search(test_list,30))

