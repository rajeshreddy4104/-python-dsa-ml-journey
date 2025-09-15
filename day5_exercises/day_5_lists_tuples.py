fruits = ["banana", "apple", "orange", "strawberry"]
print(fruits)
fruits.append("kiwi")
print(fruits)
fruits.insert(0,"grape")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.pop(2)
print(fruits)
fruits[0]="pineapple"
print(fruits)

#slicing
num=[1,2,3,4,5]
print(num)
print(num[::2])
print(num[:3])

#tuples

co = (10,20,30)


#finding the largest number
nums=[10,20,30,40,50]


def larg_num(lst):
    largest = lst[0]
    for i in lst:
        if i>largest:
            largest=i
    return largest
print(nums)
print("largest num:",larg_num(nums))

#tuple unpacking
a,b= 4,7
b,a=a,b
print(a,b)