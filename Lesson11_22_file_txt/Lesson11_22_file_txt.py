# Створити текстовий файл,
# записати в нього, рядково, дані, які вводить користувач.
# Закінченням введення служить порожній рядок.
# Кожен введений рядок у файлі повинен починатися з нового рядка.

# Option 1
file = open("Lesson11_countries.txt", "w+")
file.write(str(input("Your country: " + "\n")))
file.close()

# Option 2
# text = file.readlines()
# lineCounter = 1
with open("Lesson11_countries.txt", "w") as file:
    file.write(str(input("Your country: " + "\n")))


# while len(text) == 0:
#     break
# else:
#     lineCounter = lineCounter + 1

