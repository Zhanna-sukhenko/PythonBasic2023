a = [1, 2, 3, 4]
k = 1

for i in range(k, len(a)-1):
    a[i] = a[i+1]
a.pop()
print(a)



















    # a = []
# a = list()
# b = [1, True, "Hello"]
# print(id(b))
# b.append(2)
# print(id(b))
# c = "Hello world"
# print(id(c))
# c += "one"
# print(id(c))

# list_num = [1, 2, 3]
#
# while True:
#     num = int(input("input int:"))
#     if num == 0:
#         break
#     list_num.append(num)
#
# print(list_num)

# list_char = list("Hello world")
# print("list char", list_char)
#
# print("list range", list(range(1,10)))

# list_num = [1, 2, 3, 4, 3, 6, 7, 8, 9]
# list_num.pop()
# print("pop list_num", list_num)
# list_num.pop(2)
# print("pop(2) list_num", list_num)
