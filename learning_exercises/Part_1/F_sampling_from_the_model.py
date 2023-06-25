import torch
words = open("../../names.txt", 'r').read().splitlines()

N = torch.zeros((27, 27), dtype=torch.int32)
chars = sorted(list(set(''.join(words))))

string_to_int = {s: i+1 for i, s in enumerate(chars)}
string_to_int['.'] = 0

for w in words:
    characters = ['.'] + list(w) + ['.']
    for ch1, ch2 in zip(characters, characters[1:]):
        idx1 = string_to_int[ch1]
        idx2 = string_to_int[ch2]
        N[idx1, idx2] += 1

# Shows us the occurence of each character as the first character in a string
# print(N[0])

# To sample, we need to calculate the probability of each character appearing as the next character in our string.
# As an example, let's claculate the probability of each character being the first character.
p = N[0].float()
p = p/p.sum()
print(p)

# Using a generator object allows us to make the behavior deterministic.
g = torch.Generator().manual_seed(2147483647)
# torch.multinomial() allows us to generate samples from a given distribution.
idx = torch.multinomial(p, num_samples=1, replacement=True, generator=g).item()

int_to_string = {i: s for s, i in string_to_int.items()}
# The first character we sampled
print(int_to_string[idx])


# To predict the next character, we will use the same technique applied to m's row.
