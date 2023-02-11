num = int(input("Enter a num: "))
sum = 0
counter = 0
min_value = num
max_value = num
while num != 0:
    sum += num
    num = int(input("Enter a num: "))
print("print_sum", sum)
while True:
    if num < min_value:
        min_value = num
    if num == 0:
        break
print("Min value:", min_value)
while True:
    if num > max_value:
        max_value >= num
    if num == 0:
        break
print("Max value:", max_value)
if num % 2 == 0:
    counter = 0
else:
    counter += 1
print("print_counter", counter)
if num == "num" and num == "1":
     print(num, "== num")
else:
    print(num, "!= num")



