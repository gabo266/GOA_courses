def filter_long_words(words):
    result = []
    for word in words:
        if len(word) > 3:
            result.append(word)
    return result

print(filter_long_words(["cat", "banana", "sun", "book"]))
