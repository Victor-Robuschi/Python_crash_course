""" 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner. """

guest_list = ['simone de beauvoir', 'albert einstein', 'ragnar lothbrock']

print('Dear ' + guest_list[0].title() + ' i hereby would like to extend a dinner invitation to you.')
print('Dear ' + guest_list[1].title() + ' i hereby would like to extend a dinner invitation to you.')
print('Dear ' + guest_list[2].title() + ' i hereby would like to extend a dinner invitation to you.')

""" 3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.

• Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can’t make it.

• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.

• Print a second set of invitation messages, one for each person who is still
in your list. """

print('-----------------------------------------------------------------')

print('Unfortunately, ' + guest_list[2].title() + ' could not make it for dinner.')

guest_list[2] = 'harald hardrada'

print('\nDear ' + guest_list[0].title() + ' i hereby would like to extend a dinner invitation to you.')
print('Dear ' + guest_list[1].title() + ' i hereby would like to extend a dinner invitation to you.')
print('Dear ' + guest_list[2].title() + ' i hereby would like to extend a dinner invitation to you.')

print('-----------------------------------------------------------------')

""" 3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.

• Start with your program from Exercise 3-4 or Exercise 3-5. 
Add a print statement to the end of your program informing people that you found a bigger dinner table.

• Use insert() to add one new guest to the beginning of your list.

• Use insert() to add one new guest to the middle of your list.

• Use append() to add one new guest to the end of your list.

• Print a new set of invitation messages, one for each person in your list """

print('\nEsteemed guests, we have found an even bigger dinner table and will be inviting 3 more guests.')
# guest_list = ['simone de beauvoir', 'albert einstein', 'harald hardrada']

guest_list.insert(1, 'pope pius XII')
guest_list.insert(3, 'arthur patschke')
guest_list.append('harold godwinson')

print('\nDear ' + guest_list[1].title() + ' i hereby would like to extend a dinner invitation to you.')
print('Dear ' + guest_list[3].title() + ' i hereby would like to extend a dinner invitation to you.')
print('Dear ' + guest_list[5].title() + ' i hereby would like to extend a dinner invitation to you.')

print('\n-----------------------------------------------------------------')

""" 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, 
and you have space for only TWO guests.

• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.

• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.

• Print a message to each of the two people still on your list, letting them
know they’re still invited.

• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program. """
# ['simone de beauvoir', 'pope pius XII', 'albert einstein', 'arthur patschke', 'harald hardrada', 'harold godwinson']

print('\nDear guests I regret to inform you that new dinner table wont arrive in time for the dinner and we can only arrange seeting for two guests.')

removed_guest = guest_list.pop(0)
print("\n" + removed_guest.title() + "I'm sorry to inform you that you have been uninvited to the dinner, sucks to suck...")

removed_guest = guest_list.pop(0)
print(removed_guest.title() + "I'm sorry to inform you that you have been uninvited to the dinner, sucks to suck...")

removed_guest = guest_list.pop(0)
print(removed_guest.title() + "I'm sorry to inform you that you have been uninvited to the dinner, sucks to suck...")

removed_guest = guest_list.pop(0)
print(removed_guest.title() + "I'm sorry to inform you that you have been uninvited to the dinner, sucks to suck...")

print('\n' + guest_list[0].title() + 'you are still invited to the dinner, hope to see you there.')
print(guest_list[1].title() + 'you are still invited to the dinner, hope to see you there.')

del guest_list[0]
del guest_list[0]

print(guest_list)

""" 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (page 46), use len() to print a message indicating the number
of people you are inviting to dinner. """

print(len(guest_list))