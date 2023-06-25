# Sampling Words

## The Technique

Our approach to sampling a word is quite simple. We initialize a string with the start character. Then, we loop over the following procedure until the end character is reached:

1. We take the row in our 27\*27 matrice of characters that refers to the last character of the string we have built so far
2. We calculate the probability of each of the 27 characters appearing as the next character in our string (by dividing each entry in the row by the sum of all the entries in the row)
3. We sample a character based on the probability distribution established (in practice, using PyTorch's multinomial() funtion)
4. When add the character to the string and repeat at step 1 until the end character is drawn at which point we can return the string.

## The Result

We see that Bigram has very bad results. For example, we generated the 10 following names:
cexze
momasurailezitynn
konimittain
llayn
ka
da
staiyaubrtthrigotai
moliellavo
ke
teda

We can recognize some patterns that could be observed in well-known names but the fact that the model only knows about the single previous character clearly limits its ability to combine those patterns into something name-like.

Nevertheless, it can be noted that the performance (every character is equally likely to occur next) is way worse. Hence, bigram has bad performance (which we will later attempt to measure) but it presents a singificant improvement compared to the fully untrained approach.

## Improving Efficiency

We will now work on improving the efficiency of our approach by vectorizing the normalization of our 27\*27 array of counts.

**_Note: pay attention to PyTorch broadcasting, read docs and watch tutorials. It is very important and can get tricky._**

## Measuring our Model's Performance: Loss and Likelihood

We want to be able to evaluate our model's performance with a single number, its loss. There are multiple ways to calculate such number but we decided to choose the **likelihood**.

The likelihood is calculated by taking the product of the probabilities of all of the possible actions from a given state. The higher the likelihood, the better the model.

Since all the probabilities will be (probably low) numbers between 0 and 1, the likelihood will be a very small number. We therefore prefer to work with the **Log Lieklihood**. The log likelihood is simply caclulated by taking the log of the likelihood.

We recall that log(a\*b) = log(a)+log(b). Hence, the log likelihood can also be calculated by summing the logs of each probability.

Nevertheless, Log Likelihood is not a perfect loss function because we want the log function to get lower as the quality of our model gets higher. This is because we want to be **minimizing the loss**. We therefore introduce the **_Negative Log Likelihood_** which is simply -(loss likelihood).

Our goal is therefore to:

- maximize the likelihood
- which is equivalent to maximizing the log-lieklihood
- which is equivalent to minimzing the negative log-likelihood
- which is equivalent to minimzing the average negative log-likelihood

Another issue now is that when we calculate the probability of seeing a string occur that does not at all occur in our training set, we get a negative log-likelihood of infinity because the probabilty of seeing one or more of the bigrams in that string is 0 and log(0)=-infinity. To adjust for that, we will initiate our 27\*27 matrice of counts with all 1s instead of all 0s.
