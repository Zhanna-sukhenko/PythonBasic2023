num = int(input("Enter a number: "))
step = 1
while step**2 <= num:
    print(step**2, end=" ")
    step += 1

# num = int(input("Enter a number: "))
# print(num, end = "\t") #<виводимо число на екран з параметром end="\t">
# step = 1  # введемо змінну завдяки якій будемо перебирати числа
# while True:
#    if step**2 > num:
#        break
# print(num, end = " ") #виводимо значення step в квадраті зпараметром