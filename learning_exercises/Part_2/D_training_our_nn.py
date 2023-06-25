import torch
import torch.nn.functional as F
words = open("../../names.txt", 'r').read().splitlines()

chars = sorted(list(set(''.join(words))))

string_to_int = {s: i+1 for i, s in enumerate(chars)}
string_to_int['.'] = 0

xs, ys = [], []
for w in words:
    chs = ['.']+list(w)+['.']
    for ch1, ch2 in zip(chs, chs[1:]):
        index1 = string_to_int[ch1]
        index2 = string_to_int[ch2]
        xs.append(index1)
        ys.append(index2)

xs = torch.tensor(xs)
ys = torch.tensor(ys)
num = xs.nelement()

W = torch.randn((27, 27), requires_grad=True)

'''
Gradient Descent
'''
for k in range(1000):
    # Forward Pass
    x_encoded = F.one_hot(xs, num_classes=27).float()
    logits = x_encoded @ W
    counts = logits.exp()
    probs = counts/counts.sum(1, keepdims=True)
    # We take the probabilities that the NN assigns to each "correct" next character
    # (based on the 5 bigrams from the first word)
    # average negative log-likelihood
    loss = -probs[torch.arange(num), ys].log().mean()

    # Backward pass
    W.grad = None
    loss.backward()

    # Update
    W.data += -50*W.grad
    print(loss)

# Note: we expect our loss to be like the one we had before, when manually counting
# under normal bigram (around 2.45). Which is what we manage to achieve.
