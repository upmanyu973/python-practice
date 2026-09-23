# for/while loops, range(), break/continue, the loop-else clause

fruits = ["heera", "mandi", "movie"]
for fruit in fruits:
    print(fruit)

for i,fruit in enumerate(fruits):
    print(i, fruit)

for i in range(5):
    print(i)          # 0, 1, 2, 3, 4 — stops before 5, same "exclusive end" habit as JS's i<5

for i in range(2, 10, 2):
    print(i)           # start, stop, step -> 2, 4, 6, 8


count = 0
while count <= 5:
    print(count)
    count += 1

num= 14
for i in range(2,num):
    num % i == 0
    print(num, "is not prime")
    break
else: 
    print(num, "is prime")