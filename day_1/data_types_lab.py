def data_type(data):
  if type(data) == None:
    return 'no value'
  elif type(data) == str:
    return(len(data))
  elif type(data) == bool:
    return 'the boolean'
  elif type(data) == int:
    if data < 100:
      return 'less than 100'
    elif data == 100:
      return 'equal to 100'
    else:
      return 'more than 100'
  elif type == list:
    for i in data:
      return data[2]
    else:
      return 'None'

