a = int(input("enter first number: "))
b = int(input("enter second number: "))

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
print(f"{a}//{b}={a//b}")
print(f"{a}%{b}={a%b}")
print(f"{a}**{b}={a**b}") #exponent

#comparing and printing which one is larger or equal
if a>b:
    print(f"{a} is grater than{b}")
elif a<b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} and {b} are eqaul")

#asking uer for age and telling them if they are minor, adult or senior

age = int(input("enter age :"))
if age<=18:
    print("you are  minor.")
elif age<60:
    print("you are adult.")
else:
    print("you are a senior.")