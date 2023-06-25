words = open("../names.txt", 'r').read().splitlines()

# We have a list of string, each element being a name. Here are the first 10:
print(words[:10])
# The size of our dataset
print(len(words))
# The size of the shortest word
print(min(len(w) for w in words))
# The size of the longest word
print(max(len(w) for w in words))
