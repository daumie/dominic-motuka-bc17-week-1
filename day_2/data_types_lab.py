"""Docstring"""
def data_type(data):
    """returns type of data"""
    if isinstance(data, None):
        return 'no value'
    elif isinstance(data, str):
        return len(data)
    elif isinstance(data, bool):
        return data
    elif isinstance(data, int):
        if data < 100:
            return 'less than 100'
        elif data == 100:
            return 'equal to 100'
        else:
            return 'more than 100'
    elif isinstance(data, list):
        try:
            return data[2]
        except:
            return None
print(data_type("dominic"))
