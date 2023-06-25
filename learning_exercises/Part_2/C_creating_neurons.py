import torch
import torch.nn.functional as F
words = open("../../names.txt", 'r').read().splitlines()

chars = sorted(list(set(''.join(words))))

string_to_int = {s: i+1 for i, s in enumerate(chars)}
string_to_int['.'] = 0

xs, ys = [], []
for w in words[:1]:
    chs = ['.']+list(w)+['.']
    for ch1, ch2 in zip(chs, chs[1:]):
        index1 = string_to_int[ch1]
        index2 = string_to_int[ch2]
        xs.append(index1)
        ys.append(index2)

xs = torch.tensor(xs)
ys = torch.tensor(ys)

# We want the inputs to our NN to be floats
x_encoded = F.one_hot(xs, num_classes=27).float()
print(x_encoded)
print(x_encoded.shape)
# Creates 27 random weights following a Normal Distrubution
W = torch.randn(27, 1)

# x_encoded @ W calculates the dot product of the inputs and the weights W.
# Reading x_encoded @ W[2,13] gives us the firing rate of neuron 13 on word 2.
logits = x_encoded @ W
counts = logits.exp()
# Normalizing the rows to get our probabilities
probabilities = counts/counts.sum(1, keepdims=True)
