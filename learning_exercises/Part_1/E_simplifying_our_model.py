import torch
words = open("../../names.txt", 'r').read().splitlines()

# We now will use only 1 special characters and therefore reduce the size of the array to 27*27
N = torch.zeros((27, 27), dtype=torch.int32)
chars = sorted(list(set(''.join(words))))

# Our mapping now includes the single special characters and places it an index 0
string_to_int = {s: i+1 for i, s in enumerate(chars)}
string_to_int['.'] = 0

for w in words:
    characters = ['.'] + list(w) + ['.']
    for ch1, ch2 in zip(characters, characters[1:]):
        idx1 = string_to_int[ch1]
        idx2 = string_to_int[ch2]
        N[idx1, idx2] += 1
