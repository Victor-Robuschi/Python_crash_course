# Sorting a List Permanently with the sort() Method
print('------------------')

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# If you wanna sort the list in reverse alphabetical order then use reverse=True

cars.sort(reverse=True)
print(cars)
print('------------------')

# Sorting a List Temporarily with the sorted() Function

cars = ['bmw', 'audi', 'toyota', 'subaru']

print('Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)
print('------------------')

# Printing a List in Reverse Order
# this is a permanent change, however it is easy to get back the original order by reversing it again.

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
