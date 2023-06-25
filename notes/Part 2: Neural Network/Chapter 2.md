We now are going to build our Neural Network.

## Our Neural Network

We are going to build a very simple Neural Network with a single layer followed by softmax.

## Softmax

The network is fed with the one-hot encoding of a character and our goal is for it to return the probability distribution for the next character.

We know that probabilities have a series of properties:

- they are positive integers
- they sum to one

The problem is that such constrained numbers can not be outputed by our Neural Network, nor can the count of each possibility for the next character. We therefore want our Neural Netwok to return the _log count_. We are then going to exponientate the log count to get the count of each posbbility for the next character. After exponentiation, we know (from the properties of e) that the negative log-count values will become positive numbers smaller than 1 and that the positive log-count values will become bigger positive numbers. We can call the log-counts **_logits_**.

Important remark: all of the operations we applied so far is differentiable. Hence, we can backpropagate through the network to adjust the weights.

The succession of exponentiating logits and caclulating a probability distribution from the obtained numbers is called **_Softmax_**.

## Training

We feed the network with the first character of the bigram (**_data_**) and expect it to return probability distributions leading to the second character in this bigra (**_the label_**).

To train our network, we can check the probability that it assigned to the label and calculate its **_negative log-likelihood_**.

Repeating this process over our training data, we can calculate the **_average negative log-likelihood_**. This value can be considered as our Network's **_loss_**. We then can backpropagate and nudge the weight's value to minimize average negative log-likelihood.

We can repeat this process a few hundreds (or 1000) times to arrive at a loss of aporoximately 2.45, which is what we had when coutning manually under "normal" Bigram. This is roughly the best result we can achieve with this Neural Network because we are not taking any additional information than Bigram.

## Moving Forward

This is a very simple Neural Network: only taking the previosu character as input and having only one layer of 27 neurons. We will therefore work on building more complex networks. Nevertheless, the approach to encoding the input data, measuring loss, and backpropagating to mimize the value of the loss will stay the same even for more complex networks. What we will be changing in the next iterations of makemore simply is the way we do the Forward Pass, to take more information into account.
