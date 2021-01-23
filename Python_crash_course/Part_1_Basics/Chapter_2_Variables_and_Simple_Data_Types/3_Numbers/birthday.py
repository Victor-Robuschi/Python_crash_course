#error showcase: "TypeError: Can't convert 'int' object to str implicitly"
# age = 23
# message = 'happy ' + age + 'rd Birthday'
# print(message)

age = 23
message = 'happy ' + str(age) + 'rd Birthday'
print(message)
