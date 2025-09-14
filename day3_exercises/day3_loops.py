#we use for loop for fixed no.of times
#for i in range(5):
   # print(i)

#while loop-> we use this for repeating until becomes false
#x = 5
#while x>0:
 #   print(x)
  #  x = x-1

#break-> stop the loop immediately
#continue-> skip current iteration and move to next


print("numbers 1 to 10 using for loop")
for i in range(10):
    print(i, end=" ")
print("\n")

print("numbers 10 to 1 using while loop")
x=10
while x>0:
    print(x, end=" ")
    x=x-1
print("\n")

#list iteration
fruits = ["apple","banana","cherry","mango","grape"]
print("iterating fruits over list:")
for i in fruits:
    print(i)
print("\n")

# break&& continue
num=int(input("choose a number b/w 1 and 20:"))
print("looping 1 to 20")
for i in range(1,21):
    if i%5==0:
        continue
    if i == num:
        print(f"found it! number = {i}")
        break
    print(i)