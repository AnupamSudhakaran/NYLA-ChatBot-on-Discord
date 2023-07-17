
import nltk
import numpy as np

from nltk.stem.porter import PorterStemmer;
stemmer=PorterStemmer();

def tokenize(sent):
    return nltk.word_tokenize(sent);



def stem(word):
    return stemmer.stem(word.lower());




def bag_of_words(tokenized_sentence,all_words):
    """
    we take all the stemmed words of a sentnce and all the word
    an array is made which has 0s of the lenght all_words

    now if the sentence has some word  which is presnt in all_words then 0->1
    else do nothing 
    

    """
    tokenized_sentence=[stem(w) for w in tokenized_sentence]
    bag=np.zeros(len(all_words),dtype=np.float32);
    for idx,w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx]=1.0
    

    return bag;




