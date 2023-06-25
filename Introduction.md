## General Structure

Makemore is built to "make more" of an input data set. For example, if you give it an input set of names, make more will generate some more name-like strings.

Under the hood, it is a **character-level language model**. It is treating every input line as an example and it is treating every example as a sequence of individual characters.

Through our exploration, we will implement a large number of character-level language models. We will start with the very simple _Bigram_ and then gradually improve our approach by implementing the following language models neural networks:

- Bag of Words
- MultiLayer Perceptrons
- Recurrent Neural Networks
- GRU
- Transformers

In fact, the transformer that we will build will the equivalent transformer to GPT-2.

## On Character-Level Language Models

A character-level language model is predicting the next character in a sequence given already some concrete sequence of characters before it.

Every single training "word" has actually quite a few charcters "packed in" this word. For example, word "isabella" is telling us:

- character 'i' is a very likely character to come first in a sequence of a name
- character 's' is likely to come after 'i'
- character 'a' is likely to come after 'is'
- ....
- character 'a' is likley to come after 'isabell'
- after there is 'isabella' the word is very likely to end

Hence, a lot is already packed in a single word in terms of the **_statistical structure_** of what's to follow in these character sequences.
