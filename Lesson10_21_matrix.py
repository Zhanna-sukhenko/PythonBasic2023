from pprint import pprint
from random import randint

if __name__ == "__main__":
    M = int(input("Num_of_rows: "))
    N = int(input("Num_of_colums: "))
    matrix = [[randint(1, 20) for i in range(M)] for j in range(N)]

    pprint(matrix)

    sum_column = [0 for i in range(M)]
    for row in matrix:
        sum_row = 0
        for i in range(len(row)):
            print(f"{row[i]:>4}", end="")
            sum_row += row[i]
            sum_column [i] += row[i]
        print(f"\t{sum_row}")

    print()
    for i in sum_column:
        print(f"{i:>4}", end="")



