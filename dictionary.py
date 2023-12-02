# Dictionary - A changeable, unordered collection of unique key:value pairs. They are fast because they use hashing
capitals = {
    'usa': 'washington',
    'india': 'new delhi',
    'china': 'beijing',
    'russia': 'moscow'
}

capitals.update({'bosnia': 'tuzla'})
capitals.update({'bosnia': 'sarajevo'})
capitals.pop('india')

print(capitals)
print(capitals['bosnia'])  # throws an error if no key
print(capitals.get('bosnia'))  # returns none if no key
print(capitals.keys())
print(capitals.values())
print(capitals.items())  # keys and values

for key, value in capitals.items():
    if key == 'usa':
        value = 'tel aviv'
        print(key, value)
    else:
        print(key, value)

print(capitals.clear())
 