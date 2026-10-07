def matching_words(words):
    char = 0
    list = []
    for word in words:
        if len(words) > 1 and word[0] == word [-1]:
            char += 1
            list.append(word)
    print ("List is:", list)
    return char

count = matching_words(["1221", "abd", "dog", "ellie"])
print ("Count is:", count)
