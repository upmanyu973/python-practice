# Variables/casting: Ask the user for two numbers via input() (as separate prompts), convert both to float, and print their sum, difference, and product using an f-string for each.
# Conditionals: Write a script that takes a number and prints "Fizz" if it's divisible by 3, "Buzz" if divisible by 5, "FizzBuzz" if divisible by both, and the number itself otherwise. (Classic exercise — good test of elif ordering, since you have to think about which condition to check first.)
# Loops: Given numbers = [12, 45, 3, 89, 27, 6], find and print the largest value using a for loop — without using Python's built-in max(). (Hint: you'll need a variable that tracks "the biggest one seen so far," updated as you loop.)
# Strings: Write a function-free script that checks whether a word is a palindrome (reads the same forwards and backwards), ignoring case — test it with "Level" and "Python". You already have everything you need for this from Thursday (.lower(), slicing with [::-1]).
# Dicts + loops together: Given ages = {"Ravi": 24, "Meena": 17, "Tom": 31, "Sara": 15}, loop through it and print only the names of people who are 18 or older.


user_input1 = float(input("Enter number 1 here : "))
user_input2 = float(input("Enter number 2 here : "))
sum = user_input1 + user_input2
diff = user_input1 - user_input2
prod = user_input1 * user_input2

print(f'{sum}, {diff},{prod}')

number = int(input("Enter the numer here : "))
if (number%3 ==0  and number%5 == 0 or number%number == 0):
    print("FizzBuzz")
elif (number%3 == 0):
    print ("Fizz")
elif (number%5 == 0):
    print("Buzz")

Given_numbers = [12, 45, 3, 89, 27, 6]

max = 0
for num in Given_numbers:
    if(num > max):
        max= num
print(max)

Given_ages = {"Ravi": 24, "Meena": 17, "Tom": 31, "Sara": 15}

for name,age in Given_ages.items():
    if (age>=18):
        print(name)