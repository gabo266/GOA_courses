def word_lengths(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

print(word_lengths(["apple", "banana", "kiwi"]))
