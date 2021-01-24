# Changing, adding and removing items in a list

# Modifying item
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Addding item to the end of a list
motorcycles.append('ducati')
print(motorcycles)

# You could also build up a list from scratch with append()
motorcycles = []

motorcycles.append('harley davidsson')
motorcycles.append('BMW')
motorcycles.append('ducati')

print(motorcycles)
# If you want to put in a item in a specific position, use intert()
motorcycles.insert(0, 'honda')

print(motorcycles)
# To delete a item from the list, use "del". you have to pick a specific item
del motorcycles[0]

print(motorcycles)

# with "del" you remove a item completely and you wont be able to use it afterwards
# if you still want to work with a removed item then we use pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# popping any item in a list. 
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.') 

# Removing item by value with remove(value)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# if we want to work with the removed item we save it in a varabile

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
