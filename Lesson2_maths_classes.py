
a = int(input("students_num1: "))
b = int(input("students_num2: "))
c = int(input("students_num3: "))
d = 2
print("all students", a+b+c)
print("per 1 desk", d)

print("desks", (a+b+c)//d)
print("left free places", (a+b+c)%d)
