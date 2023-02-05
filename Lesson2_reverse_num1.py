# reverse any number
# i.e. -› 123 -› 321

num = int(input("Enter the number: "))
reversed_num = 0

a = num % 10
reversed_num = reversed_num * 10 + a
num //= 10

a = num % 10
reversed_num = reversed_num * 10 + a
num //= 10

a = num % 10
reversed_num = reversed_num * 10 + a
num //= 10

print("Reversed Number: ", reversed_num)