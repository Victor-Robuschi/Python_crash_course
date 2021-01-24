#this is a list, its a variable that contains a multitude of values. so insted of makeing hundred different variables
#we make a single variable that can contain many values. 
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# in order to pull out a specific value out of a list, we use the varavle name and brackets with the numerical position of the value.
# the order always starts at 0
# dependet of what type of value it is, it can be manipuleted. so with a string we can use .tile() 
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])

#if we want to access the rear of the list we use negative numbers eg. -1
print(bicycles[-1])

#Here we are simply constructing a sentens with one of our list values
message = 'My first bicycle was a ' + bicycles[0].title() + '.'
print(message)
