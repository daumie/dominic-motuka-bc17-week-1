def data_type(data):
  if type(data) == type(None):
    return 'no value'
  elif type(data) == str:
    return(len(data))
  elif type(data) == bool:
    return data
  elif type(data) == int:
    if data < 100:
      return 'less than 100'
    elif data == 100:
      return 'equal to 100'
    else:
      return 'more than 100'
  elif type(data) == list:
    try:
      return data[2]
    except:
      return None

