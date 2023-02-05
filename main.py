# reverse any number
# i.e. -› 1234 -› 4321

num = int(input("Enter the number: "))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))