def sort_by_len(words):
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse = True)

    res = []
    for length, word in t:
        res.append(word)

    return res

st = []
file = open('wd.txt')
st = sort_by_len(file)

for word in st:
    print word

