sum = 0
counter = 0
odd = 0
even = 0
min_num = float("+inf")
max_num = float("-inf")
while True:
    num = int(input("Enter a num: "))
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    if num == 0:
        break
    sum += num
    counter += 1

print("print_sum", "-", sum)
print("print_counter", "-", counter)
print("print_min_num", "-", min_num)
print("print_max_num", "-", max_num)
print("print_avg", "-", sum/counter)
print("print_odd", "-", odd)
print("print_even", "-", even)