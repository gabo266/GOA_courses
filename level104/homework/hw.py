#1
def split_sentence(sentence):
    return sentence.split()

print(split_sentence("ეს არის წინადადება"))

#2
def join_words_with_dash(words):
    return "-".join(words)

print(join_words_with_dash(["მე", "მიყვარს", "Python"]))

#3
fruits = ["ვაშლი", "ატამი", "ბანანი"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

#4
sentence = input("შეიყვანე წინადადება: ")
words = sentence.split()

for word in words:
    print(word)

#5
products = ["პური", "რძე", "კვერცხი", "კარაქი"]
joined = ", ".join(products)

print(f"სიის შედეგი: {joined}")
