import torch
import matplotlib.pyplot as plt
words = open("../../names.txt", 'r').read().splitlines()

# For our purposes, we have 28 characters (26 letters + 2 special characters 'end' and 'start')
N = torch.zeros((28, 28), dtype=torch.int32)

# We need to convert each of our character into an int to index it in our 2D array.
# First, let's auto-generate a list of all characters present in words. We want this list in alphabetical order.
chars = sorted(list(set(''.join(words))))

# Now let's create a mapping between a character and its index
string_to_int = {s: i for i, s in enumerate(chars)}
string_to_int['<S>'] = 26
string_to_int['<E>'] = 27
for w in words:
    characters = ['<S>'] + list(w) + ['<E>']
    for ch1, ch2 in zip(characters, characters[1:]):
        idx1 = string_to_int[ch1]
        idx2 = string_to_int[ch2]
        N[idx1, idx2] += 1

# We will now attempt to visualize N
# plt.imshow(N)
# plt.show()

# A more complete and "beautiful" visualization can be created
# First, we will inverse string_to_int
int_to_string = {i: s for s, i in string_to_int.items()}
plt.figure(figsize=(16, 16))
plt.imshow(N, cmap='Blues')
for i in range(28):
    for j in range(28):
        chstr = int_to_string[i] + int_to_string[j]
        plt.text(j, i, chstr, ha='center', va='bottom', color='gray')
        plt.text(j, i, N[i, j].item(), ha='center', va='top', color='gray')
plt.axis('off')
plt.show()
