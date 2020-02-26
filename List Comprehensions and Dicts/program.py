#!/usr/bin/python3

# 1.) Write a function alnum_fn(x) that takes a string and returns True if the string is alphanumeric, otherwise False.


#Function Name: alnum_fn(x)
#Function Arguments: str(x) i.e. string
#Purpose: The alnum() checks if the string is alphanumeric or not. We return the value true or false respectively.


def alnum_fn(x):
    # return all([c >= 'a' and c <= 'z' or c >='A' and c <= 'Z' or c >= '0' and c <= '9' for c in x]) # Works good but takes more time.
    return str(x).isalnum()
	

# 2.) Write a function is_noun(x) that takes a part of speech such as 'NNP' and returns True if the POS represents a noun phrase,     #     otherwise False. A POS represents a noun if its first two letters are 'NN'.


#Function Name: is_noun(x)
#Function Arguments: string
#Purpose: To check if the given part of speech is noun or not based on the position that represents the noun. We determine it is a    #         noun if the  first two letters are 'NN' or not. We return the value true or false respectively.


def is_noun(x):
    #return sum([1 for a in x[:2] if a == 'N']) == 2
    return len(x) >= 2 and x[0] == 'N' and x[1] == 'N'#If length is greater than or equal to two and if the first and second character is N then it is non, else it is not  


# 3.) Write a function is_even(x) that returns True if x is an even number, otherwise False. You can assume that the function will 
#      only be called with integer arguments.


#Function Name:is_even(x) 
#Function Arguments: Integer
#Purpose: To check if the given number is even or not. We return the values true or false respectively.


def is_even(x):
    return x % 2 == 0 #We know that all even number when divided by '2' yields '0' as remainder. 


# 4.) Given a list such as v1 = [1, 3, 5, 7, 9], write a function add_one(x) that returns a list where each element is one greater than the original list, 
# e.g., [2, 4, 6, 8, 10] for this example. You can assume that all of the elements in the original list are numeric.


#Function Name: add_one(x)
#Function Arguments: List of integers.
#Purpose: To return the integers from list and add 1 to each element in the list  which yields the desired result.


def add_one(x):
    return [i + 1 for i in x] #So I am taking all the elements from list and adding 1 to the integers to yield the result.


# 5.) Given a list such as v2 = ['N', 'V', "JJ", "NS", "N$"], write a function drop_bad(x) that returns a list that contains only the alphabetic elements in x. In this example the result would be ['N', 'V', "JJ", "NS"].

#Function Name:drop_bad(x)
#Function Arguments: List of strings.
#Purpose: We are returning the list of strings that contain only the alphabets and we are dropping any other character if present. With the help of predefined
#         function is_alpha() we are checking if the string contains only alphabets or not.


def drop_bad(x):
    #return [a for a in x if all(['a' <= c <= 'z' or  'A' <= c <= 'Z' for c in a])] # Works good but takes more time.
    return [items for items in x if items.isalpha()]


# 6.) Given a list such as
# v2 = [['boy', 'N'], ['is', 'V'], ['of', 'PP'], ['xyz', 'NS'],
#       ['abc', 'N$']]
# write a function show_nouns(x) that returns a list of the same format that contains only the nouns in the input list.


#Function Name: show_nouns(x)
#Function Arguments: Nested list of strings.
#Purpose: To check if the nested list contains only noun and return the part of the nested list which contains nouns.


def show_nouns(x):
    return [[b,a] for [b,a] in x if is_noun(a)]


# 7.) Given a list of words and parts of speech such as
# v2 = [['book', ['NN', 'VB']], ['is', ['VBZ']], ['of', ['PP']]]
# write a function show_nouns2(x) that returns a list of the same format containing only the nouns in the original list.


#Function Name: show_nouns2(x)
#Function Arguments: Nested list of strings.
#Purpose: To check if the nested list contains atleast one noun and return the part of the nested list which contains atleast one noun.


def show_nouns2(x):
    return [[b,a] for [b,a] in x if any([is_noun(c) for c in a])]


# 8.) Given a list of the format above, write a function show_nouns3(x) that returns a simple list containing only the nouns, e.g. ['book', 'x'].


#Function Name: show_nouns3(x)
#Function Arguments: Nested-List of strings.
#Purpose: To check if the nested list contains noun and return that part of speech that contains the noun.


def show_nouns3(x):
    return [a for [a,b] in x if any([is_noun(c) for c in b])]


# 9.) Given a list of the format a_list = [3, 3, 4, 4, 5, 5, 6, 6, 9, 9] write a function select_numbers(x) that returns a list containing one greater than 
# each even number in the list, e.g., # [5, 5, 7, 7].


#Function Name: select_numbers(x)
#Function Arguments: List of integers.
#Purpose: We are checking the list, then if the list contains an even integer, we add '1' to that integer and return that value.


def select_numbers(x):
    return [a+1 for a in x if a%2==0]


# 10.) Given a list of lists of numbers where the sublists do not necessarily have the same lengths e.g., v1 = [[1, 2, 3], [5, 4]],
# write a function show_count(x) that produces the total number of entries in the sublists, e.g., 5 for the list above.


#Function Name: show_count(x)
#Function Arguments: Sub-Lists of integers.
#Purpose: We are computing the total numbers of numbers passed in the list.


def  show_count(x):
    return sum([len(a) for a in x])


# 11.) Write a function show_totals(x) that produces a list where each sublist has been summed, e.g., [6, 9] for the list above.


#Function Name: show_totals(x)
#Function Arguments: Sub-Lists of integers.
#Purpose: We are summing up the numbers in the sublist and returning the sum value of the sub list.


def show_totals(x):
    return [sum(a) for a in x]


# 12.) Write a function show_total(x) that produces the sum of the values in the sublists e.g. 15 for the list above.


#Function Name: show_total(x)
#Function Arguments: Sub-Lists of integers.
#Purpose: We are summing up the numbers in the sublist and then we are summing up the sub list numbers as well and returing the final sum value.


def show_total(x):
    return sum([sum(a) for a in x])


# 13.) Given a list containing two sublists of the same length e.g., v2 = [[1, 2, 3], [5, 4, 7]],  write code to produce the dot 
#      product of the sublists, 
#      e.g. 34 for the list above (= 1*5 + 2*4 + 3*7)


#Function Name: dot_product(x)
#Function Arguments: Nested list of integers.
#Purpose: We are taking the dot product of the sublist by mkaing use of the function zip and sum.


def  dot_product(x):
    return sum([a * b for (a,b) in zip(x[0],x[1])])


# 14.) Given a sentence represented as a list of words where the last word represents the final punctuation mark, e.g., 
#  v1 = ['The', 'big', 'black', 'horse', 'is', 'black', '.'], write a function remove_dot(x) that produces a list of words without the final punctuation mark.

#Function Name: remove_dot(x)
#Function Arguments: List of strings.
#Purpose: We are removing the dot present in the list.

def remove_dot(x):
    return x[:-1]

# 15.) Given a sentence of the form above, write a function produce_lower(x) that contains the same sentence in lower case. Hint: Use the 'lower' function of the string class.

#Function Name: produce_lower(x)
#Function Arguments: List of strings.
#Purpose: We are taking the list of strings and returning this list of string but with all the strings in lowercase.

def produce_lower(x):
    return [a.lower() for a in x]

# 16.) Given a sentence of the form above, write a function count_words(x) write that returns the number of distinct words in the sentence, 
# e.g., 5 for the sentence above.

#Function Name: count_words(x)
#Function Arguments: List of strings.
#Purpose: We are returning the length of the string but we are counting only distinct words present in the sentence.

def count_words(x):
    return len({a:1 for a in v1[:-1]})
    #return sum(1 for (i,a) in enumerate(x[:-1]) if a not in x[:i])

# 17.) Prof. Untel (that is French for “So-and-so”) represents student grades in a list, as follows:
# [['Aaa', 'g', [2, 4, 5]],['Bbb', 'u', [4, 5, 6]], etc.] means that student Aaa got 2 on HW1 (not HW0!), 4 on HW2, etc. 
# The second argument represents grad/undergrad. Write a function avg_grade(x) giving the average grade for HW1.

#Function Name: avg_grade(x)
#Function Arguments: List of integers and strings.
#Purpose: We are computing the average marks scored by student in HW01 irrespective of their level of education. I have used the function sum to calculate 
#         the marks scored by student in HW01 and dividing it with the number of students in the class using the function len(x)

def avg_grade(x):
    return sum([c[0] for [a,b,c] in x])/len(x)


# 18. Write a function ugrad_points(x)giving the total number of points earned on HW2 by undergraduates.

#Function Name: ugrad_points(x)
#Function Arguments: List of integers and strings.
#Purpose: We are summing up the marks scored by undergraduate students in HW02 and returning that sum.

def ugrad_points(x):
    return sum(c[1] for [_,b,c] in x if b == 'u')
