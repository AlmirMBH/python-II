# tuple is a collection that is unordered and un-indexed; no duplicate values
utensils = {'fork', 'spoon', 'knife'}
dishes = {'bowl', 'plate', 'cup', 'knife'}

utensils.add('napkin')
print("add: ", utensils)

utensils.remove('fork')
print("remove: ", utensils)

utensils.update(dishes)
print("update: ", utensils)

utensils.union(dishes)
print("union: ", utensils)

utensils.difference(dishes)
print("difference: ", utensils)

utensils.intersection(dishes)
print("difference: ", utensils)

for item in utensils:
    print(item)

utensils.clear()
print(utensils)
