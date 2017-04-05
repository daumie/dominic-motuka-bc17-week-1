def find_max_min(n):
    holdinglist = []
    if not isinstance(n, list):
        raise TypeError
    elif max(n) == min(n):
        holdinglist.append(len(n))
        return holdinglist
    else:
        holdinglist.append(min(n))
        holdinglist.append(max(n))
    return holdinglist
#print(find_max_min([-100, 1, 10, 1000]))
#print(find_max_min(["cat,apple,dog,trump"]))
