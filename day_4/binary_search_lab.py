class BinarySearch(list):
    def __init__(self, a, b):
        self.length = a
        self.step = b
        super(BinarySearch, self).__init__()
        for elem in range(1, self.length+1):
            self.append(elem * self.step)
        self.length = len(self)

# Implementation of Binary Search algorithm
    def search(self, value):
        start, stop, index, found, count = 0, len(self)-1, 0, False, 0

        if value == self[start]:
            index = start
            found = True
        elif value == self[stop]:
            index = stop
            found = True

        if value not in self:
            found = True
            index = -1
        while start <= stop and not found:
            index = (start + stop) // 2
            if self[index] == value:
                found = True
            else:
                count += 1
                if value < self[index]:
                    stop = index - 1
                else:
                    start = index + 1
        return {'count': count, 'index': index}

# test_list = BinarySearch()
# test_list = [1,2,3,4,5,6,7,8,9,9,0]