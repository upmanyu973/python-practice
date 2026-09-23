# operators, conditionals, and truthy/falsy.

age = 30
is_married = False 

print ( age >= 25 and is_married == True)
print ( age >= 25 or is_married == True)
print ( not is_married == False)
print (17// 5)
print(2 ** 10)
print (2* 10)
print (int(10/2))


# Person_age = int(input("Enter your age: "))
# declare = ""

# if Person_age <= 1:
#     declare = "Infant"
# elif 1 < Person_age <= 5:
#     declare = "Toddler"
# elif 5 < Person_age <= 12:
#     declare = "Child"
# elif 13 <= Person_age <= 19:
#     declare = "Teenager"
# elif Person_age > 19:
#     declare = "Adult"
# else:
#     declare = "old"

# print(declare)

values = ["", 0, [], {}, None, False, "hi", 1, [1,2]]
for v in values:
    print(v, "->", bool(v))