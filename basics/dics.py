print("Docs: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict")
ages = { 'Name1' : 11, 'Name2' : 22, 'Name3' : 33 }
print(ages)
ages['Name1'] = 12
print(ages)
print("Let's add one more item!")
ages['Name4'] = 44
print(ages)
del ages['Name1']
print("Name1 is out: ", ages)
ages['name4'] = 45
print("Obviously dictionary is case-sensitive: ", ages)
print("Pop name4 value: ", ages.pop('name4'))
print("Safely retrieve value: ", ages.get('abc'))
print("Dict keys: ", ages.keys(), ", and it's values: ", ages.values())
print("Dict keys as list: ", list(ages.keys()), ", and values as a list: ", list(ages.values()))
print("Remove dictionary at all!")
del ages

print("Create a dict, alternative 1")
ages2 = dict(Name1=11, Name2=22)
print(ages2)
print("Create a dict, alternative 2")
ages3 = dict([('Name1', 11), ('Name2', 22)])
print(ages3)