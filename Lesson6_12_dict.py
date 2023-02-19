str = "Why do you cry Willy ? Why do you cry ? Why Willy ? Why Willy ? Why ? Willy why ?"

list_words = str.split()
print("list_words", list_words)

set_word = set(list_words)
print("set_word", set_word)

dict_word = {}
for word in set_word:
    # print("current word", word)
    print("count of word ", word, "is", str.count(word))
    dict_word[word] = str.count(word)

    # if str.count(word) > 1:
    #     print("duplicate word =", word)