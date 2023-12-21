#concise and expressive ways to create lists, dictionaries, and sets in Python.

#List Comprehension:
# Using a for loop to create a list of squares
squares = []
for i in range(5):
    squares.append(i**2)
print(squares)

# Equivalent list comprehension
squares = [i**2 for i in range(5)]
print(squares)


#Dictionary Comprehension:

# Using a for loop to create a dictionary of squares
squares_dict = {}
for i in range(5):
    squares_dict[i] = i**2
print(squares_dict)

# Equivalent dictionary comprehension
squares_dict = {i: i**2 for i in range(5)}
print(squares_dict)


#ex
x = int(input("enter num : "))
squares_dict = {i: i**2 for i in range(1,x+1)}
print(squares_dict)

