So far, we have trained a bigram character-level language model and did so by having the counts of all bigrams and normalizing the rows to get probability distributions. We were then able to both use the model to sample new words and to measure the quality of this model through negative log-likelihood.

We will now introduce a new approach to solving this problem using Neural Networks. In this part 2, we will arrive at a very similar position as in part 1 because we will simply cast the bigram approach to the Neural Network framework.

## Creating the Training Values

We want to create two tensors, one giving the inputs and the other the expected outputs from each input. Our inputs will be the first charcter of a bigram and the output the second

## One-hot encoding

We therefore have two list of integers (the index of each of the two characters composing a bigram). It would not make sense to pass just one integer to a Neural Network and to expect it to give an answer from that (because they re multiple layers taht need to be fed in the input layer). We therefore will implement **one-hot encoding**. In one-hot encoding, we turn an integer into a vector of 0s and a 1. For example, integer value 13 will be encoded by a vector with all 0s except at position 13 where there will be a 1.
