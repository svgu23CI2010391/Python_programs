Write a program to convert the elements of two lists into key-value pairs of a dictionary.

list1 = ['name', 'age', 'city']
list2 = ['John', 30, 'New York']

dict1 = dict(zip(list1, list2))
print("dict1 => ", dict1)
print("dict1.get('name')", dict1.get("name"))
print("dict1.get('age')", dict1.get("age"))
print("dict1.get('city')", dict1.get("city"))
print("dict1.keys()", dict1.keys())
print("dict1.values()", dict1.values())