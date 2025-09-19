nums={1,2,3,4}

print(nums)

empty_set=set()

nums.add(5)
nums.discard(2)

#membership

print(5 in nums) #if its there it returns true, if not false

#set operation now
a={1,2,3,4,5}
b={6,7,8,3,9,10}

print(a|b) #union
print(a&b) #intersection
print(a-b)
print(a^b)#symmetric difference

#relations
print({1,2}<=a) #subset
print(a>={2,3}) #superset

evens={n for n in range(20) if n%2==0}
print(evens)