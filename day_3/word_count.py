def words(string):
    """
        Counts the occurrences or characters in a word
    """
    stringDict = {} 
    
    separated = string.split()
    
    if len(separated) == 1:
        stringDict[separated[0]] = 1
        return stringDict
    else:
        for item in separated:
            if item.isdigit():
                item = int(item)
            stringDict[item] = separated.count(str(item))
        return stringDict
#print(words("Is cat with tag 546 is come is eat is food") )