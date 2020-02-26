#!/usr/bin/python3

def alnum_fn(x):
    return all([c >= 'a' and c <= 'z' or c >='A' and c <= 'Z' or c >= '0' and c <= '9' for c in x])

print ("1. ", "is '3' alphanumeric? ", alnum_fn('3'))
print (" ", "is 'x$z' alphanumeric?", alnum_fn('x$z'))
print()

def is_noun(x):
    return sum([1 for a in x[:2] if a == 'N']) == 2
    #return len(x) >= 2 and x[0] == 'N' and x[1] == 'N'

print ("2. ", "is NNP a noun?", is_noun('NNP'))
print (" ", "is VP a noun? ", is_noun('VP'))
print (" ", "is N a noun? ", is_noun('N'))
print()


def is_even(x):
    return x % 2 == 0

print ("3. ", "is 3 even? ", is_even(3))
print (" ", "is 0 even? ", is_even(0))
print (" ", "is -2 even? ", is_even(-2))
print()

def add_one(x):
    return [i + 1 for i in x]

v1 = [2, 0, -2, 4, 6]
v2 = add_one(v1)
print("4. ", "if the input is ", v1)
print(" ", "the output is ", v2)
print()


def drop_bad(x):
    return [a for a in x if all(['a' <= c <= 'z' or  'A' <= c <= 'Z' for c in a])]

v1 = ['abc', 'x$z', '3']
v2 = drop_bad(v1)
print("5. ", "if the input is ", v1)
print(" ", "the output is ", v2)
print()

def show_nouns(x):
    return [[b,a] for [b,a] in x if is_noun(a)]

v1 = [['man', 'NN'], ['man', 'VB'], ['flowers', 'NNS'], ['flowers', 'VBZ']]
v2 = show_nouns(v1)
print("6. ", "if the input is ", v1)
print(" ", "the output is ", v2)
print()

def show_nouns2(x):
    return [[b,a] for [b,a] in x if any([is_noun(c) for c in a])]

v1 = [['man', ['NN', 'VB']], ['flour', ['NN', 'VB']], ['the', ['DT']]]
v2 = show_nouns2(v1)
print("7. ", "if the input is ", v1)
print(" ", "the output is ", v2)
print()

def show_nouns3(x):
    return [a for [a,b] in x if any([is_noun(c) for c in b])]

v1 = [['man', ['NN', 'VB']], ['flour', ['NN', 'VB']], ['the', ['DT']]]
v2 = show_nouns3(v1)
print("8. ", "if the input is ", v1)
print(" ", "the output is ", v2)
print()

def select_numbers(x):
    return [a+1 for a in x if a%2==0]

v1 = [2, 0, -1, 3, 6]
v2 = select_numbers(v1)
print("9. ", "if the input is ", v1)
print(" ", "the output is ", v2)
print()


def  show_count(x):
    return sum([len(a) for a in x])


v1 = [[1, 2, 3], [5, 4]]
v2 = show_count(v1)
print("10. ", "if the input is ", v1)
print(" ", "the output is ", v2)
print()

def show_totals(x):
    return [sum(a) for a in x]

v1 = [[1, 2, 3], [5, 4]]
v2 = show_totals(v1)
print("11. ", "if the input is ", v1)
print(" ", "the output is ", v2)
print()

def show_total(x):
    return sum([sum(a) for a in x])

v1 = [[1, 2, 3], [5, 4]]
v2 = show_total(v1)
print("12. ", "if the input is ", v1)
print(" ", "the output is ", v2)
print()

def  dot_product(x):
    return sum([a * b for (a,b) in zip(x[0],x[1])])

v1 = [[1, 2, 3], [5, 4, 7]]
v2 = dot_product(v1)
print("13. ", "if the input is ", v1)
print(" ", "the output is ", v2)
print()


def remove_dot(x):
    return x[:-1]

v1 = ['The', 'big', 'black', 'horse', 'is', 'black', '.']
v2 = remove_dot(v1)
print("14. ", "if the input is ", v1)
print(" ", "the output is ", v2)
print()


def produce_lower(x):
    return [a.lower() for a in x]

v1 = ['The', 'big', 'black', 'horse', 'is', 'black', '.']
v2 = produce_lower(v1)
print("15. ", "if the input is ", v1)
print(" ", "the output is ", v2)
print()


def count_words(x):
    return len({a:1 for a in v1[:-1]})

#return sum(1 for (i,a) in enumerate(x[:-1]) if a not in x[:i])

v1 = ['The', 'big', 'black', 'horse', 'is', 'black', '.']
v2 = count_words(v1)
print("16. ", "if the input is ", v1)
print(" ", "the output is ", v2)
print()


def avg_grade(x):
    return sum([c[0] for [a,b,c] in x])/len(x)

v1 = [['Aaa', 'g', [2, 4, 5]],
 ['Bbb', 'u', [4, 5, 6]],
 ['Ccc', 'g', [7, 8, 9]],
 ['Ddd', 'u', [1, 2, 3]],
 ['Eee', 'u', [4, 5, 7]]]
v2 = avg_grade(v1)
print("17. ", "if the input is ", v1)
print(" ", "the output is ", v2)
print()


def ugrad_points(x):
    return sum(c[1] for [_,b,c] in x if b == 'u')

v2 = ugrad_points(v1)
print("18. ", "if the input is ", v1)
print(" ", "the output is ", v2)
print()
