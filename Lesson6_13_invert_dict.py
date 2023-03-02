# my_dict = {
#     "apple": ['malum', 'popum', 'popula'],
#     "fruit": ['baca', 'bacca', 'popum'],
#     "punishment": ['malum', 'multa']
# }
# swap_dict = {}
# for k, v in my_dict.items():
#     for v1 in v:
#         if v1 in my_dict:
#             print(swap_dict[v1].append([k]))
#         else:
#             swap_dict[v1] = [k]
#
# print("swap_dict", swap_dict)


my_dict = {
    "apple": ['malum', 'pomum', 'popula'],
    "fruit": ['baca', 'bacca', 'popum'],
    "punishment": ['malum', 'multa']
}
swap_dict = {}
for k, v in my_dict.items():
    for elem in v:
        if elem in my_dict:
            swap_dict[elem].append([k])
        else:
            swap_dict[elem] = [k]
swap_dict.update({"malum": ['apple', 'punishment']})
print("swap_dict", swap_dict)

# my_dict = {
#     'apple': 'popum',
#     'fruit': 'baca',
#     'punishment': 'malum'
# }
# swap_dict = {}
# for k, v in my_dict.items():
#     swap_dict.update({v:k})
# print(swap_dict)
