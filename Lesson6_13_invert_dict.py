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


