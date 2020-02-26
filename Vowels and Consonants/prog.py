#!/usr/bin/python3
import sys
import unicodedata

# Creating a "LIST" called VOWELS_LIST that contains all the vowels


VOWELS_LIST = ['a', 'e', 'i', 'o', 'u', 'y']   


# Creating a "MAP" called VOWELS_MAP that convert from a letter with a diacritic to its equivalent without diacritics


VOWELS_MAP = {'\u00e9': "e", '\u00e2': "a", '\u00ea': "e", '\u00ee': "i", '\u00f4': "o", 
              '\u00fb': "u", '\u00e0': "a", '\u00e8': "e", '\u00f9': "u", '\u00eb': "e", 
              '\u00ef': "i", '\u00ff': "y", '\u00fc': "u", '\u00e6': "ae", '\u0153': "oe"}


# Function Name: vowels_count(line)
# Function Purpose: The purpose of this function is to check if the lines conatain letters and if the letter is alpha then increment the number of letters


def vowels_count(line):
    dt = {}
    number_of_letters = 0 # Intializing the value of letter to zero
    number_of_consonants = 0 # Intializing the value of consonants to zero
    for letter in line:
        if letter.isaplpha(): # Checking if the letter is alphabet or not using isalpha()
            number_of_letters += 1 # Incrementing the letter by one if the letter is alpha
        if (letter.lower() in VOWELS_LIST): 
            dt.setdefault(letter, 0)
            dt[letter] += 1  # We are ensuring that the letter if it is capital we are converting it to lower case and incrementing the letter count by one
    return dt, number_of_letters


# Function Name: compute_expected(actual)
# Function Purpose: We are creating a 2D Array to store the values of number of letters, lines, characters, consonants and vowels


def compute_expected(actuals):
    row_sum = [sum(actual) for actual in actuals]
    # print(row_sum)
    columns = len(actuals[0])
    col_sum = [0] * columns
    for actual in actuals:
        for col in range(columns):
            col_sum[col] = col_sum[col] + actual[col]
    # print(col_sum)
    total = sum(row_sum)
    expected = [[row_sum[row] * col_sum[col] / total for col in range(columns)] for row in range(len(actuals))]
    return expected


# Function Name: read_file(file_name)
# Function Purpose: We are using this function to read the files which are encoded in utf8 format using with open() as fhand technique
#		    Also in this function we are going to increment the vowel count and return the count values of number of lines, characters, letters, and consonants 


def read_file(file_name):
    with open(file_name, 'r', encoding="utf8") as fhand:
        number_lines = 0 # Intializing the count of line to zero
        number_characters = 0 # Intializing the count of characters to zero
        number_letters = 0 # Intializing the count of letters to zero
        number_vowels = 0 # Intializing the count of vowels to zero
        vowel_count = {c: 0 for c in VOWELS_LIST}


# In the following steps we are increasing the count of lines, characters, letters and vowels as and when we start reading a new line from the input file 


        for line in fhand:
            number_lines = number_lines + 1
            number_characters = number_characters + len(line) 
            number_letters = number_letters + len([ch for ch in line if unicodedata.category(ch).startswith("L")])
            line = line.lower()  # Converting the text to lowercase
            for ch in line:
                if ch in VOWELS_LIST:
                    number_vowels += 1 # if character is in the VOWELS_LIST increment vowel by one
                    vowel_count[ch] += 1 
                elif ch in VOWELS_MAP:
                    number_vowels += 1	# else if character is in the VOWELS_MAP increment vowel by one
                    for v in VOWELS_MAP[ch]:
                        vowel_count[v] += 1 

        return number_lines, number_characters, number_letters, vowel_count, number_vowels, number_letters - number_vowels


# Function Name: main(file_name_1, file_name_2)
# Function Purpose: To read the two input files and print the output in the required format


def main(file_name_1, file_name_2):
    file_names = [file_name_1, file_name_2]
    counts = [read_file(file_name) for file_name in file_names]


# We are prinitng out the lines, characters and letters present in the both the text files in the following steps


    print("\nTotal Count:\n")
    print("{:20} {:>16} {:>20} {:>19}".format("Book", "Line Count", "Character Count", "Letter Count"))
    for i, count in enumerate(counts):
        print("{:20} {:>16} {:>20} {:>19}".format(file_names[i], count[0], count[1], count[2]))
    print()

    actuals = [count[-2:] for count in counts]
    expected = compute_expected(actuals)
    chi_square, df = compute_chi_square(actuals, expected)


# We are printing out the actual count of vowels, consonants, Chi-square and Degree of Freedom in the following steps


    print("Actual:")
    print("{:20} {:>16} {:>14}".format("Book", "Consonants", "Vowels"))
    for i in range(2):
        print("{:20} {:>16} {:>14}".format(file_names[i], actuals[i][1], actuals[i][0]))
    print()


# We are printing out the expected count of vowels, consonants in the following steps


    print("Expected:")
    print("{:20} {:>16} {:>14}".format("Book", "Consonants", "Vowels"))
    for i in range(2):
        print("{:20} {:16.2f} {:14.2f}".format(file_names[i], expected[i][1], expected[i][0]))
    print()


# We are printing out the Chi-square and Degree of Freedom


    print("Degress of Freedom = ", df)
    print("chi-square = {:.2f}".format(chi_square))
    print()

    vowel_counts = [[count[3][c] for c in VOWELS_LIST] for count in counts]
    expected_vowel_counts = compute_expected(vowel_counts)
    chi_square, df = compute_chi_square(vowel_counts, expected_vowel_counts)


# Here we are printing out the actual count of indiviadual list of vowels present in the following steps 


    print("\nVowel Counts:")
    print("\nActual:")
    print("{:20}".format("Book", ), " ".join("{:>12}".format(ch) for ch in VOWELS_LIST))
    for i, vowel_count in enumerate(vowel_counts):
        print("{:20}".format(file_names[i], ), " ".join("{:>12}".format(n) for n in vowel_count))
    print()


# Here we are printing out the expected count of indiviadual list of vowels present in the following steps


    print("\nExpected:")
    print("{:20}".format("Book", ), " ".join("{:>12}".format(ch) for ch in VOWELS_LIST))
    for i, vowel_count in enumerate(expected_vowel_counts):
        print("{:20}".format(file_names[i], ), " ".join("{:12.2f}".format(n) for n in vowel_count))

    print()
    print("Degree of Freedom = ", df)
    print("chi-square = {:.2f}".format(chi_square))
    print()


#Function Name: compute_chi_square(actuals, expected)
#Function Purpose: To compute the chi-square value.

def compute_chi_square(actuals, expected):
    return sum([sum([((a - e) ** 2) / e for (e, a) in zip(e_row, a_row) if e != 0]) for (e_row, a_row) in
                zip(expected, actuals)]), (len(actuals) - 1) * (len(actuals[0]) - 1)


if __name__ == "__main__":


# In the following couple of steps we are making sure that we are passing exactly parameters in the command line to exeucte the program using an if-elif construct
# We are opening the two input files using the argument sys.argv


    if len(sys.argv) < 3:
        print("Error. Please provide two parameters")
        sys.exit(-1)
    elif len(sys.argv) > 3:
        print("Error. Please provide two parameters")
        sys.exit(-1)
    file_name_1 = sys.argv[1]
    file_name_2 = sys.argv[2]
    main(file_name_1, file_name_2)
