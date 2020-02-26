import sys
import re
import json

words = None
unigrams = None
bigrams = None
total_words = None

class Correction():
    def __init__(self, candidate, error_type, error_pos, correct_letter, error_letter, x, w):
        self.candidate =candidate
        self.error_type = error_type
        self.error_pos = error_pos
        self.correct_letter = correct_letter
        self.error_letter = error_letter
        self.x = x
        self.w = w

    def p_x_w(self):
        count_x = unigrams[self.x] if len(self.x) == 1 else bigrams[self.x]
        count_w = unigrams[self.w] if len(self.w) == 1 else bigrams[self.w]
        return count_x / count_w

    def p_word(self):
        return words[self.candidate]/total_words

    def p_corr(self):
        return 1e9 * self.p_x_w()* self.p_word()

    def __str__(self):
        return "{:20}\t{:10}\t{:10}\t{:15}\t{:15}\t{}|{}\t{}\t{}\t{}".format(self.candidate, self.error_type, self.error_pos, self.correct_letter, self.error_letter,self.x,self.w,self.p_x_w(), self.p_word(), self.p_corr())


def generate_corrections(word):
    global words
    word1 = "<" + word + ">"
    # Add any letter at any position
    addition = [Correction("".join([word[:i], word[i+1:]]),"ins",i,'-',word[i],word1[i:i+2],word1[i]) for i in range(len(word))]
    # b) Delete the letter at any position.
    deletion = [Correction("".join([word[:i], ch, word[i:]]),'del',i,ch,word[i], word[i], word[i] + ch) for i in range(len(word)) for ch in "abcdefghijklmnopqrstuvwxyz"]
    # c) Substitute the letter at any position with any other letter.
    substitution = [Correction("".join([word[:i],ch, word[i + 1:]]),"subst",i,word[i],ch,ch,word[i]) for i in range(len(word)) for ch in "abcdefghijklmnopqrstuvwxyz" if ch != word[i] ]
    # d) Transpose any two consecutive letters.
    transposition = [Correction("".join([word[:i], word[i+1],word[i], word[i + 2:]]),"trans",i,word[i:i+2],word[i+1:i-1:-1],word[i+1:i-1:-1],word[i]) for i in range(len(word)-1)]

    print("Possible corrections for addition:",len(addition))
    print("Possible corrections for deletion:", len(deletion))
    print("Possible corrections for substitution:", len(substitution))
    print("Possible corrections for transposition:", len(transposition))

    addition = list(filter(lambda x: x.candidate in words, addition))
    deletion = list(filter(lambda x: x.candidate in words, deletion))
    substitution = list(filter(lambda x: x.candidate in words, substitution))
    transposition = list(filter(lambda x: x.candidate in words, transposition))

    print("After pruning, possible corrections for addition:",len(addition))
    print("After pruning, possible corrections for deletions:", len(deletion))
    print("After pruning, possible corrections for substitution:", len(substitution))
    print("After pruning, possible corrections for transposition:", len(transposition))

    print("Candidate Correction\tError Type\tError Pos\tCorrect Letter\tError Letter\tx|w\t\tP(x|word)\tP(word)\t10^9 * P(x|w)P(w)")
    for c in addition + deletion + substitution + transposition:
        print(c)





def read_dictionary():
    global words, unigrams, bigrams, total_words
    with open('json-data.json', 'r') as fp:
        dictionary = json.load(fp)
        words = dictionary['words']
        unigrams = dictionary['unigrams']
        bigrams = dictionary['bigrams']
        total_words = sum(words.values())
    print(words)
    print(unigrams)
    print(bigrams)

def main(misspelt_words):
    if not misspelt_words:
        print("Please provide words in command line arguments")
        return

    read_dictionary()
    for word in misspelt_words:
        if re.match("[^a-zA-Z]",word):
            print(word, " contains non-alphabetic character")
        else:
            generate_corrections(word)



if __name__ == "__main__":
    #main(sys.argv[1:])
    main(["whent", "woud", "wehn", "wren"])

