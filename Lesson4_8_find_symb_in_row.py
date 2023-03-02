# s = str(input("Введіть рядок: "))
# ch = str(input("Введіть символ: "))
#
# for i in range(len(s)):
#     if s[i] == ch:
#         print(i, end="\t")

s = str(input("Введіть рядок: "))
ch = str(input("Введіть символ: "))
d = s.find(ch)
if ch in s:
    d = [0], [0:]
print (d+1)
