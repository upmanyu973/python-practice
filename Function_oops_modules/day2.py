# List/dict/set comprehensions; lambda, map, filter

# 1. List comprehensions
# The general pattern is:
# [expression for item in iterable if condition]

# squares of 0-9
squares = [x**2 for x in range(10)]
print(squares)


# with Dict 
nums = [1, 2, 3, 4, 5]
squares_dict = {n: n ** 2 for n in nums}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# only even squares
even_squares = [ x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)

# uppercase every word in a list
words = ["hi", "there", "friend"]
upper = [word.upper() for word in words]
print(upper)

# Given nums = [3, 8, 15, 22, 7, 41, 9], write a list comprehension that produces a list of only the numbers greater than 10.

Given_nums = [3, 8, 15, 22, 7, 41, 9]
Only10s= [num for num in Given_nums if num > 10]
print(Only10s)

2. #Lambda functions

# A lambda is an anonymous (unnamed) function, written as:
# lambda arguments: expression

add = lambda a,b : a+b
print(add(3,4))

# is equivalent to:
def add(a, b):
    return a + b

# 3. Filter 

only_10s = list(filter(lambda num: num > 10, Given_nums))

# Exercise 2: Using filter and lambda (not a comprehension this time), write a line that pulls only the even numbers out of Given_nums. Give it a try.

only_evens =  list(filter(lambda num : num % 2 == 0,Given_nums))
print(only_evens)

# 4. Map 
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda num : num * 2,nums ))
print(doubled)

output = list(map(lambda num: num * 10 , filter(lambda num : num % 2 == 0, nums)))
print(output)


# Challenge: You have a list of names:

# names = ["alice", "bob", "eve", "sam", "mia"]

# Write one line (comprehension, or map/filter/lambda — your choice, or both if you want to compare) that produces a dictionary mapping each name to the length of that name, but only for names with more than 3 letters. So the expected output would be:
# {"alice": 5, "sam": 3}  # wait — check that condition yourself, don't just trust me

# Actually — don't trust that expected output blindly. Work it out yourself: which names have more than 3 letters, and what should the final dict look like? Write the code and tell me both your code and what you predict it'll print, before running it.

names = ["alice", "bob", "eve", "sam", "mia"]
obj = {name: len(name) for name in names if len(name) > 3}
print(obj)

obj2 = dict(map(lambda name: (name,len(name)),filter(lambda name : len(name) > 3, names)))
print(obj2)
