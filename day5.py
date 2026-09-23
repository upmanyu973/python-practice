# Lists & tuples: indexing, slicing, append/sort/common methods

skills = ["Javascript","React","CSS","Redux","python"]

print (skills.pop())
print(skills)
skills.insert(-1,"python")
print(skills)
skills.remove("python")
print(skills)
skills.append("python")
print(skills)
skills.sort()
print(skills)
print(skills[:4])
print(skills)

lo,hi = (10, 35)
print(lo)

lo=12
print(lo)

coordinates = (17.2344, 34.532)
#coordinates[0]=12


def min_max(nums):
    return min(nums), max(nums)

print(min_max([4,6,3,2,1]))
