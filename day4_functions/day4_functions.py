def greet(name="sammy"):
    print(f"hello, {name}")
greet("rajesh")
greet()

def add(a,b):
    return a+b
new=add(3,4)
print(new)

def power(base,exp=2):
    return base**exp
result=power(3)
result1=power(3,6)
print(result)
print(result1)


def say_hello(name):
    print(f"hello,{name}")
name="raj"
say_hello(name)

#checking if a number is prime

def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
num=int(input("enter a number:"))
print(f"{is_prime(num)}")
