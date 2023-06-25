words = open("../../names.txt", 'r').read().splitlines()

# Visualizing the bigrams in the first 3 words of the dataset
for w in words[:3]:
    # We can hallucinate a start and end character to extract all the value a word has to offer us.
    characters = ['<S>'] + list(w) + ['<E>']
    for ch1, ch2 in zip(characters, characters[1:]):
        print(ch1, ch2)
