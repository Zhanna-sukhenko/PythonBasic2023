from random import randint

M = int(input("Enter num1: "))
N = int(input("Enter num2: "))

matrix = []

for i in range(M):
    if M <= 5:
        raise Exception("number less or equal 5")
    line = []
    for j in range(N):
        line.append(randint(0, 50))
    matrix.append(line)
    print("list", line)

for i in range(len(matrix)):
    print('\t'.join([str(x) for x in matrix[i]]))
sum_columns = []
for j in range(N):
    sum_column = 0
    for i in range(len(matrix)):
        sum_column += matrix[i][j]
    sum_columns.append(sum_column)
    print(sum_column, end="\t")

def bubble_sort(list_to_sort):
for _ in range(0, len(list_to_sort) - 1):
    for x in range(0, len(list_to_sort) - 1):
        if list_to_sort[x] < list_to_sort[x + 1]:
            list_to_sort[x], list_to_sort[x + 1] = list_to_sort[x + 1], list_to_sort[x]
return list_to_sort
        # for x in range(0, len(list_to_sort) - 1):
        #     if list_to_sort[x] > list_to_sort[x + 1]:
        #         list_to_sort[x], list_to_sort[x + 1] = list_to_sort[x + 1], list_to_sort[x]
            # if list_to_sort[x] < list_to_sort[x + 1]:
            #     list_to_sort[x], list_to_sort[x + 1] = list_to_sort[x + 1], list_to_sort[x]

matrix_sorted = [bubble_sort(matrix(i) if i % 2 == 0 else matrix[i] for i in range(len(matrix)))]

def print_matrix(custom_matrix):
    matrix = custom_matrix
    for j in range(j):
        for i in matrix:
            print(f"{i[j]:<5}", end = " ")
    for i in matrix:
        for j in i:
            print(f"{j:<5}", end=" ")
        print()
print(print_matrix(custom_matrix))


print("\t")