#!/usr/bin/python3

import re
from collections import defaultdict
import json
import sys

# Function Name: main(file_name)
# Function Purpose: The purpose of this function is to read the input file and count the number of distinct unigrams, disticnt bigrams, words, number of items in 
#                   dictionary and the 10 frequnetly used words in that file

def main(file_name):

    # In the next three lines we are creating a default dictionary and assigning one each to unigram, bigram and word count.
    unigram = defaultdict(int) 
    bigram = defaultdict(int)
    word_counts = defaultdict(int)
    try:
        f = open(file_name, mode="r") # using open function to read the input file
    except:
        print("Error while reading file") # Print error if there is an error reading the file
        return

    for line in f:
        # In the followign line I am trying to remove the AP tag usign the function split(), Also we are replacing characters that are not ASCII by space and also we 
        # are converting the text to lower case. I am using list comprehnesion technoque to do this. 
        words = [word for text1 in re.split("AP\d*-\d*\t", line) for word in
                 re.sub("[^a-zA-Z ]", ' ', text1).lower().split()] 
        for word in words:
            word_counts[word] = word_counts[word] + 1  # Adding the word_count with 1 and assigning it to word_count
            word1 = "<" + word + ">"    # Including the " < " and " > " and adding it with word and assigning it to word1
            for ch in word1:
                unigram[ch] = unigram[ch] + 1 # Counting every distinct character and adding it  by 1 and assiging it to unigram
            for ch1, ch2 in zip(word1[:-1], word1[1:]): 
                bigram[ch1+ch2] = bigram[ch1+ch2] + 1 # Counting the set of characters and adding it by 1 and assiging it to bigram. I have used Zip to combine the 
                                                      # characters 
    print(unigram)  # Printing Unigram
    print(bigram)   # Printing bigra
    print(word_counts)  # Printing word count
    print("the number of distinct unigrams", len(unigram))  # Printing the number of distinct unigrams present in the file
    print("the number of distinct bigrams", len(bigram))    # Printing the number of distinct bigrams present in the file
    print("the number of words", sum(word_counts.values())) # Printing the total number of words present in the file
    print("the number of items in dictionary", len(word_counts))    # Printing the number of items in the dictionary
    word_counts_sorted = sorted(word_counts, key=lambda x: word_counts[x], reverse=True)    # Sorting the words
    print("10 frequent words", word_counts_sorted[:10]) # Printing the 10 freqeuntly used words in the file
    return {'unigrams': unigram, 'bigrams': bigram, 'words': word_counts}

from time import perf_counter 
t1_start = perf_counter()
t1_stop = perf_counter()
print("Elapsed time:", t1_stop, t1_start)  
print("Elapsed time during the whole program in seconds:", 
                                        t1_stop-t1_start) 

if __name__ == "__main__":
    if len(sys.argv) >  1:           # If there is more than one parameter given take the input file name provided in the command line by user
        file_name = sys.argv[1]
    else:
        file_name = "ap88.txt"      # Else by default use ap88.txt as mentioned
    dictionary = main(file_name)    # We are then creating a dictionary cotaining these  words
    print(dictionary)               # Priting the dictionary
    with open('json-data.json', 'w') as fp:
        json.dump(dictionary, fp,sort_keys=True) # We are using json to serialize the dictionary which is human readable
