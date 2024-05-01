'''
This will containt he examples from

list
list functions
tuples
functions
return statements
if statements
if statements and comparisons

'''

# friends = ["Hanuman", "Ram", "Shiva", "Ganesh", "Gayatri"]

# print(friends)
# print(friends[0])
# print(friends[-1])
# print(friends[1:])
# print(friends[:-2]) #
# print(friends[2:5]) 
# print(friends[-4:-2]) #


#LIST FUNCTIONS

luck_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Hanuman", "Ram", "Shiva", "Ganesh", "Gayatri"]

# extend
new_friends = friends.copy()
new_friends.extend(luck_numbers)
print(new_friends)

# append
new_friends = friends.copy()
new_friends.append("Vishnu")
print(new_friends)

# insert
new_friends = friends.copy()
new_friends.insert(3," >> Vishnu << ")
print(new_friends)


# remove
new_friends = friends.copy()
new_friends.remove("Ram")
print(new_friends)


# clear
new_friends = friends.copy()
new_friends.clear()
print(new_friends)


# pop
new_friends = friends.copy()
new_friends.pop()
print(new_friends)


# index of a element
new_friends = friends.copy()
find_friend = "Ganesh"
print(f'The friend {find_friend} is at {new_friends.index(find_friend)} (according to array indexing)')
# The friend Ganesh is at 3
print(f'The friend {find_friend} is at {new_friends.index(find_friend)+1}  (according to array indexing) ')


# count
new_friends = friends.copy()
find_friend_2 = "Ram"
print(f'There are {new_friends.count("Ram")} "{find_friend_2}"s in the given list')

# sort
new_friends = friends.copy()
print(f"the sorted list for the given list \n {new_friends} is \n{new_friends.sort()}")

sorted_frnds = new_friends.sort()
print(f'The sorted friends list  using "sort method" is {sorted_frnds}')

# sorted returns a value which can be stored in a variable
sorted_frnds = sorted(new_friends)
print(f'The sorted friends list  using "sort method" is {sorted_frnds}')

# in line sort and the new sorted list is present in the same variables it doesn;t retuen anything
new_friends.sort()
print(f'The sorted friends list  using "sort method" is {new_friends}')


# in line sort and the new sorted list is present in the same variables it doesn;t retuen anything
new_friends.reverse()
print(f'The REVERSED sorted friends list  using "sort method" is {new_friends}')
