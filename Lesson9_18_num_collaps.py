# The sum() method is used to compute the sum of digits of a number in python in a list.
# Convert the number to a string using str(), then strip the string and convert it
# to a list of numbers with the strip() and map() methods, respectively.
# Then, compute the total using the sum() method.

num = int(input("Enter your num: "))

def number_collaps(num): #getSum()
    if num <= 0:
        raise Exception("number less or equal 0")
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum
def collapse_number(num):
    num = number_collaps(num)
    num = number_collaps(num)
    num = number_collaps(num)
    num = number_collaps(num)
    num = number_collaps(num)
    return num

print(collapse_number(num))

