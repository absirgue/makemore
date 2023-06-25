# We are going to improve the efficiency of our implementation of Bigram by vectorizing the normalization of the rows.
import torch
words = open("../../names.txt", 'r').read().splitlines()

N = torch.zeros((27, 27), dtype=torch.int32)
chars = sorted(list(set(''.join(words))))

string_to_int = {s: i+1 for i, s in enumerate(chars)}
string_to_int['.'] = 0

b = {}
for w in words:
    characters = ['.'] + list(w) + ['.']
    for ch1, ch2 in zip(characters, characters[1:]):
        idx1 = string_to_int[ch1]
        idx2 = string_to_int[ch2]
        N[idx1, idx2] += 1
g = torch.Generator().manual_seed(2147483647)

int_to_string = {i: s for s, i in string_to_int.items()}

# Vectorizing the normalization of the rows
P = N.float()
# We want to, simultaneously and in parallel, divide all the rows by their respective sums
P /= P.sum(1, keepdim=True)

for i in range(10):
    index = 0
    out = []
    while True:
        index = torch.multinomial(
            P[index], num_samples=1, replacement=True, generator=g).item()
        if index == 0:
            break
        out.append(int_to_string[index])
    print(''.join(out))
