# Ось умови роботи функції:
#
# Він повинен починатися з хештегу (#).
# Усі слова мають мати першу літеру з великої літери.
# Якщо кінцевий результат довший за 140 символів, він має повернути false.
# Якщо вхід або результат є порожнім рядком, він повинен повернути помилку.
# Приклад:
# hash_tag_creator(" Hello there thanks for trying my Kata")
#                 повинно повернути  "#HelloThereThanksForTryingMyKata"
# hash_tag_creator(""  Hello   World  ")
#                 повинно повернути  "#HelloWorld"
# hash_tag_creator(""")
#                 повинно повернути exception
s = input(str("Enter the trend: "))

def hash_tag_creator(s):
    output = "#"
    s = s.replace('"', '')
    for word in s.split():
        output += word.title()
    if len(s) > 140:
        return False
    if len(s) == 0:
        raise Exception(s, "wrong")
    return output

print(hash_tag_creator(s))

