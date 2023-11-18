import re
def create_wordlist(line):
    word_list2 = []
    word_list1 = line.split()
    for word in word_list1:
        word1 = re.sub("[^a-zA-Z]+", " ", word)
        for word2 in word1.split():
            word_list2.append(word2)

    word_list3 = [x.lower() for x in word_list2]
    return word_list3


