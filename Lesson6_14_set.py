list_num1 = [1, 2, 3, 4, 5, 100, 55]
list_num2 = [9, 8, 1, 2, 3, 4, 5]
unique_num = list(set(list_num1) & set(list_num2))

print("the number of unique_num:  ", len(unique_num))