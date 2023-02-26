a = [1, 6, 12, 10, 25]
count = 0
for i in range(1, len(a)-1):
        if a[i-1] < a[i] > a[i + 1]:
                count += 1
print(count)




# a[1:-1]








# b = 1
# c = 2
#
# if b>c:
#     print(c)
# else:
#     if b<c:
#         print(b)

# while True:
#     num = input(b),
#     if num == 0:
#         break
#     b.append(num)
#
# print(b)
