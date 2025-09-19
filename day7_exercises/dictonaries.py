#createing a dictonary
student ={"name":"Rajesh","age":"25","grade":91.5}

#reading a dictionary
print(student["name"])
print(student.get("gpa",0.0)) #0.0 default if missing

student["age"]=27
student["city"]="hyderabad"
student["gender"]="male"


student.pop("city")

for key in student:
    print(key,student[key])
for k,v in student.items():
    print(k,"-->",v)

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

a={"x":2,"y":3}
b={"y":4,"z":5}

c=a|b
b|=a

squares={n:n*n for n in range(7)}


print(student.get("gpa"))        # None (no default)
print("gpa" in student)          # False (key missing)
print(sorted(student.items()))   # Items sorted by key (for stable comparison)
