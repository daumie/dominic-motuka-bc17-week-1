def binary_search(given_list, item):

    if len(given_list) == 0:
    	return False
    else:
    	midpoint = len(given_list) // 2

    if given_list[midpoint] == item:
    	return True
    else:
    	if item < given_list[midpoint]:
    		return binary_search(given_list[:midpoint], item)
    	else:
    		return binary_search(given_list[midpoint + 1:],item)
# test_list = [21,27,32,33,42,47,58,69,70,77,79]
# print(binary_search(test_list,3))
# print(binary_search(test_list,69))