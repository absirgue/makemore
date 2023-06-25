We will start our exploration with building a Bigram language model. In a Bigram language model, we are always working with just two characters at at a time. We are working with one character that we are given and attempting to predict the next character in a sequence.

## Bigrams and their Informations

With the word "emma" we can create the following bigrams:

- e m
- m m
- m a

Having those 3 pairs of chararacters actually gives us more information than just 3 pairs of characters going well together to form a name. It also tells us that 'e' is likely to come first and 'a' to come last.

To extract all of the value from a given input word (here "emma"), we can therefore halluciante two special characters to mark the Start and the End of the word. This gives us the following bigram:

- S e
- e m
- m m
- m a
- a E

## Introducting Bigram's Statistical Model

In order to learn the statistics of which chracter is likely to follow which characters, the simplest way in the language Bigram model is to simply do it by counting. We are therefore going to simply count how often each combination of 2 characters occurs in the training set.

With the first 3 words from our input set, we have the following counts:
{('S', 'e'): 1,
('e', 'm'): 1,
('m', 'm'): 1,
('m', 'a'): 1,
('a', 'E'): 3,
('S', 'o'): 1,
('o', 'l'): 1,
('l', 'i'): 1,
('i', 'v'): 1,
('v', 'i'): 1,
('i', 'a'): 1,
('S', 'a'): 1,
('a', 'v'): 1,
('v', 'a'): 1}

We see that most bigram occured only once, except ('a', 'E') that occured in each of the three words.

By repeating our counting procedure on the entire training set, we can for example know that the 3 most common bigrams are:
[(('n', 'E'), 6763), (('a', 'E'), 6640), (('a', 'n'), 5438)]
...and the three least common ones are:
[(('q', 'r'), 1), (('d', 'z'), 1), (('p', 'j'), 1)]

## Improving the Data Structure

Instead of storing the counts in a Python dictionary, we will use a 2-dimensional array where each row is a first character in a bigram and the columns are going to be the second character in a bigram. Each entry in this 2-dimensional array will tell us how often this second character follows the first character in the dataset.

To do so, we will use Pytorch's Tensors. Tensors allow us to manipulate all the individual entries in a 2D array and to do so very efficiently.

We obtain the following structure for our counts:
![Alt text](../illustrations/Part%201/counts_visualization.png "Count Structure")
