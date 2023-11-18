from hw3.create_wordlist import create_wordlist
from collections import Counter

global alpha

def get5words(df1, real_words):
    count2 = {} 
    alpha = real_words
    for i2 in df1['dialog']:
        sentence = create_wordlist(i2)
        for k in sentence:
            if k not in real_words:
                if count2.get(k, -1) == -1:
                    count2[k] = 0
                else:
                    count2[k] += 1

    a2 = Counter(count2)
    high = a2.most_common(5)
    list3 = ["", "", "", "", ""]
    j = 0
    for i4 in high:
        list3[j] = i4[0]
        j += 1
    return list3


