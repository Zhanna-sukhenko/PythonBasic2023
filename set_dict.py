#set (множини)невпорядкований, приймає унікальні значення
#{}
#{"a", 5, True}
#set (множини)
set_var = set({1,2,3,4,5}) #множина НЕ упорядкована не можна вживати квадратн дужки
print(set_var) #множина складається із знезмінних
#fozenset(іterable) - створює незмінний сет(перетворює множину в незмінний сет)

frozen_set_var = frozenset(set_var)
print(frozen_set_var)

print({frozen_set_var, 2})
print({frozenset([1,2,3]), set([2,3])})

file_list = ["", "", ""]
print(frozenset(file_list))

set_01 = {1,2,3,4,5}
set_02 = {3,4,5,6,7}
#оператори щоб прибрати дублікати:
print(set_01 - set_02)
print(set_01 | set_02)
print(set_01 & set_02)
print(set_01 ^ set_02) #спільне не виводить
# [in], [not in]
print(4 in set_01)
print(4 not in set_01)

set_01 = {}
set_02 = {}

for item_set in set_02:
    if item_set in set_01,
        print(item_set)

#method add(value)
set_01.add(199)

print(set_01)

set_01.add(199)
list_duplicate = [1,2,2,3,3,4,4]
set_uniq = set()

for item_setin list_duplicate:
    set_uniq.add(item_set)
print(item_set)

pop() - видалити останнє

#метод перетину множин - intersection або  &

#метод об єднань - union або | (аналог нашого оператора | який виводить )




#dict (словники НЕвпорядковані) у словника є ключ, доступ до елементів(об єктів) за ключем(а не за індексом),
#{}  #словник можна помістити в словник
new_dict = {} #створюється пустий словник
print(type(new_dict))
#нижче відображення більш старіший метод словника
new_dict = {
    14: "nick01",
    197: "nick02"
}

#в одному словникку мають бути унікальні ключі/і два однакових не може бути теж бо вони будуть перезатиратись
#ключі можуть бути 1.

#новіший метод словника
new_dict = dict(
    # key = value
    winter=1,
    spring=2,
    summer=3,
    autumn=4
)
print(new_dict)

new_dict = dict(
    # key : value
    "winter"=1,
    "spring"=2,
    "summer"=3,
    "autumn"=4,
    4 = "seasons"
)
print(new_dict[4])

# mapping = (перетворення списку в словник за допомогою zip-з двох наборів повертає сформовані пари)
days = [1,2,3]
days_names = ["mon", "tue", "wed"]

new_dict = dict(zip(days, days_names))
print(new_dict)

# [] - доступ до елементу за ключем
print(new_dict[14])
#метод get дозволяє отримати значення по ключу (якщо такого ключа немає то повернеться значення None)
print(new_dict.get['summer'])
print(new_dict.get(16, "not found"))

# del - можемо видаляти конкретний ключ
del new_dict[14]
print(new_dict)

# in
print(14 in new_dict)
# clear повністю очищує словник
new_dict.clear()  # або  new_dict = {}

# copy - повертає повну копію словника
copy_new_dict = new_dict.copy()
print(new_copy_dict)
# dict.fromkeys - створення словників із ключів
keys_tuple = ("1","2","3")
value = 0
new_dict = dict.fromkeys(keys_tuple, value)

#метод  items - дозволяє пройтись по всім пари ключ-значення
#метод key - повертає ключі       print(...____.keys.())
#метод value- повертає значення   .values()
# pop - метод який видаляє значення за КЛЮЧЕМ .pop(key, [default])   .pop(199, None)-видалення неіснуючого ключа з відповіддю None

string_value = "Why do you cry Willy why do you cry why Willy why Willy? why Willy? Why?"

