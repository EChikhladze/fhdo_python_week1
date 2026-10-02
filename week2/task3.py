myList = [{'make': ' Google ', 'model': '216', 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': '7', 'color': 'Blue'}]
sortedList = sorted(myList, key = lambda d : d['color'])
print(sortedList)