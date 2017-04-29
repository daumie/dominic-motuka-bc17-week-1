"""Docstring"""
def words(string):
    """
        Counts the occurrences or characters in a word
    """
    string_dictionary = {}

    separated = string.split()

    if len(separated) == 1:
        string_dictionary[separated[0]] = 1
        return string_dictionary
    else:
        for item in separated:
            if item.isdigit():
                item = int(item)
            string_dictionary[item] = separated.count(str(item))
        return string_dictionary
#print(words("Is cat with tag 546 is come is eat is food") )
