# simple looping of a list
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)

# doing more work in a loop

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    print("I can't wait to see your next trick, " + magician.title() + '.\n')

print('Thank you, everyone. That was a great magic show')

# indentation errors showcase
# 
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# print(magician)
# 
# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
# print("I can't wait to see your next trick, " + magician.title() + ".\n")