word_list = ["fish", "fort", "flow"]
input_word = "fosh"

input_word_length = len(input_word)
# cell = [[0 for i in range(4)] for j in range(4)]

for word in word_list:
    similarity = 0
    for i in range(input_word_length):
        j = i
        if word[i] == input_word[j]:
            similarity += 1
        else:
            continue
    print(similarity)
