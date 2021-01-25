""" 3-10. Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once. """

mountains = ['mount everest', 'k2', 'kangchenjunga', 'lhotse', 'cho oyu', 'dhaulagiri', 'nanga parbat',]
print(mountains)
print(mountains[0])
print(mountains[0].title())
fun_fact = mountains[0].title() + ' is 8848.86 meters or 29 031.7 feet tall.'
print(fun_fact)

print(mountains)
mountains[6] = 'manaslu'
print(mountains)

mountains.append('nanga parbat')
print(mountains)
mountains.insert(3, 'makalu')
print(mountains)

mountains = ['mount everest', 'k2', 'kangchenjunga', 'makalu', 'lhotse', 'cho oyu', 'dhaulagiri', 'manaslu', 'nanga parbat', '     annapurna', 'k5']
print(mountains)
del mountains[-1]
print(mountains)

popped_mountain = mountains.pop()
print(mountains)
print(popped_mountain.title().strip())

print(mountains)
popped_nanga = mountains.pop(-1)
print(mountains)

mountains = ['mount everest', 'k2', 'kangchenjunga', 'makalu', 'lhotse', 'cho oyu', 'dhaulagiri', 'manaslu', 'nanga parbat', 'annapurna', 'k5']
print(mountains)
mountains.remove('makalu')
print(mountains)

short_mountain = 'k5'
mountains.remove(short_mountain)
print(mountains)

mountains = ['mount everest', 'k2', 'kangchenjunga', 'makalu', 'lhotse', 'cho oyu', 'dhaulagiri', 'manaslu', 'nanga parbat', 'annapurna', 'k5']
print(mountains)

