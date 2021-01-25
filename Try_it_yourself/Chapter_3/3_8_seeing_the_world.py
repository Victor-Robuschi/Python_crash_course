""" 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.

• Store the locations in a list. Make sure the list is not in alphabetical order. (t)

• Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list. (t)

• Use sorted() to print your list in alphabetical order without modifying the actual list. (t)

• Show that your list is still in its original order by printing it. (t)

• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list. (t)

• Show that your list is still in its original order by printing it again. (t)

• Use reverse() to change the order of your list. Print the list to show that its order has changed. (t)

• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order. (t)

• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed. (t)

• Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed. (t)

"""


destinations = ['new york', 'dublin', 'istanbul', 'budapest', 'montevideo']
print(destinations)
print(sorted(destinations))
print(destinations)
print(sorted(destinations, reverse=True))
print(destinations)
destinations.reverse()
print(destinations)
destinations.reverse()
print(destinations)
destinations.sort()
print(destinations)
destinations.sort(reverse=True)
print(destinations)
