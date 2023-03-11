# Напишить функцію, яка буде переводити число у розгорнутий вигляд
# Вам буде надано число, і вам потрібно буде повернути його як рядок у розгорнутій формі.
# Наприклад:
# expanded_form(12) # повинно повернути '10 + 2'
# expanded_form(42) # повинно повернути '40 + 2'
# expanded_form(70304) # повинно повернути '70000 + 300 + 4'
# Уважно: всі числа які будуть передаватись повинні бути більше 0, інакше треба показати помилку.

num = int(input("Enter a num more than 10: "))
def expanded_form(num):
    result = []

    for index, digit in enumerate(str(num)[::-1]):
        if int(digit) != 0:
            result.append(digit + ('0' * index))
        elif num == 0:
            raise Exception("number is not > 0")
    return ' + '.join(result[::-1])

print(expanded_form(num))

