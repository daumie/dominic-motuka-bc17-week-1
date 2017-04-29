"""Docstring"""
def find_max_min(num):
    """Finds largest or smallest number in a list"""
    holdinglist = []
    if not isinstance(num, list):
        raise TypeError
    elif max(num) == min(num):
        holdinglist.append(len(num))
        return holdinglist
    else:
        holdinglist.append(min(num))
        holdinglist.append(max(num))
    return holdinglist
print(find_max_min([-100, 1, 10, 1000]))
print(find_max_min(["cat,apple,dog,trump"]))
