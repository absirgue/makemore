words = open("../../names.txt", 'r').read().splitlines()

b = {}
for w in words:
    characters = ['<S>'] + list(w) + ['<E>']
    for ch1, ch2 in zip(characters, characters[1:]):
        bigram = (ch1, ch2)
        b[bigram] = b.get(bigram, 0) + 1

# 3 least common bigram
print(sorted(b.items(), key=lambda kv: kv[1])[:3])
# 3 most common bigram
print(sorted(b.items(), key=lambda kv: -kv[1])[:3])
