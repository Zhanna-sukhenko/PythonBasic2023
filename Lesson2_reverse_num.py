# reverse any number
# i.e. -› 123 -› 321

num = int(input("Enter the number: "))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))