# functions in depth. Some of this transfers straight from JS, one part (scope) genuinely doesn't and will trip you up if you don't slow down for it.
# Write a function calculate_total(*prices, discount=0) that accepts any number of item prices as positional args and an optional keyword-only discount (a percentage, e.g. 10 for 10% off), returning the total after discount is applied. Call it a few different ways — with just prices, and with prices plus a discount — and print the results.
# Write the global-counter example yourself: a global visits = 0, a function log_visit() that increments it using global, called 3 times in a row with the counter printed after each call.

def personal_details(name, address="default"):
    return f"name: {name}, add: {address}!"
print(personal_details("John"))
print(personal_details("Rita","H345, los Angeles"))

def add_all(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    return total

output = add_all(1,2,3,4)
print(output)

def print_info(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    return kwargs

info = print_info(name="Ajax", role="BE", age=25)
print(info)

# count = 0
 # def increment():
 # count = count +1
 # return count

# increment()

count = 0
def increment():
    global count
    count = count +1
    return count
print(increment())

def calculate_total(*args,discount=0):
    total = 0
    for price in args:
        total += price
        return total - discount
print(calculate_total(10,40,35,60,discount = 30))

visits = 0
def log_visit():
    global visits
    visits +=1
    print(visits)
log_visit()
log_visit()
log_visit()

visits = 0
def log_visit():
    global visits
    visits +=1
print(visits)
log_visit()
log_visit()
log_visit()