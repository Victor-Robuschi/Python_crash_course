#How to manipulate a strings letter, makeing them all upper or lowercase. And to capitalize the first letter of the first and last name. 
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#A showcase of how "+" manipulates two strings, concatenation.
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = 'Hello ' + full_name.title() + '!'
print(message)
