import torch

# Creating a 3*5 arrays filled with 0
a = torch.zeros(3, 5)

# By default, the type of each entrt is a float32.
# print(a.dtype)

# Because we are going to store counts, let's use ints.
a = torch.zeros((3, 5), dtype=torch.int32)

# We can manipulate tensors very easily:
a[1, 3] = 1
a[0, 0] = 5
# print(a)
