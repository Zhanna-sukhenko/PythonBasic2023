s = str(input("Введіть рядок: "))
ch = str(input("Введіть символ: "))

for i in range(len(s)):
    if s[i] == ch:
        print(i, end="\t")

