#!/usr/bin/python3

import sys

if len(sys.argv) == 1: #This if construct is to check the input arguments and if there are no argumnets by default need to take the value as 1000
    n = 1000;

elif len(sys.argv) > 2: #If there are more than two arguments, the input is invalid
    print("Invalid Input; Hey user!!please check again and input the correct value")
    exit()

elif len(sys.argv) == 2: 
    if(int(sys.argv[1]) < 0): # This if loop is to make sure that user doesn't provide a negative number, if he does, it will throw an error.
        print("Inavlid input; Hey user you have a given a negative value which is not acceptable for this assignment")
        exit()
    else:
        n = int(sys.argv[1]) # I have type-casted the input value to int as we cannot have a string or any other format of input value for this program. If the user still persists and gives a string as an input while compiling this line will throw an error and it will state it is an invalid literal.

original_n = n # I am declaring another variable called original_n where the current n value is being stored because we will need this later

print("\n")
print("  decrement      current      count")
print("{:>24} ".format(n)) # > is used to right justify

decrement = 1 # I have declared a variable by the name decrement so we can start decrementing the number. Since we begin by decrementing using number 1 I have assigned value 1 to the variable.
count = 0     # I have declared a variable called count to keep track of the amount of numbers we are using to decrement till it reaches next zero in the unit's place.  
count_all = 0 # I have declared a variable called count_all to keep track of the overall amount of count that we use till we reach the next zero as we need it finally to check the avergae numbers spoken per increment and average cycles per increment.

while n - decrement >= 0: # I am using while loop for the execution of this code. We are trying to make sure that the user input minus the decrementing value is equal to or greater than zero.
    
    n -= decrement # This step we are reducing the number by decrement.
    
    count += 1     # We are incrementing the count
    
    last_digit = n % 10 #  We are checking if the remainder is zero or not by using the modulo opearator because if the unit place number is zero then the following if loop will get executed.
    
    if last_digit == 0 or n - decrement < 0: # If last digit is equal to zero or number minus the decrement value is less than 0 then the follwoing statments will be executed.

        width = 10 
        str_number = str(ord('a'))
        print("{:11} {:>12} {:>10}    {:<18} ".format(decrement,n,count,"*" * count)) # > is used to right justify and < is used to left justify
        count_all += count
        count = 0
        decrement += 1  

print("\n")
print(" There were", count_all, "number spoken with", decrement-1, "differnet increments.") 
print(" Average cycles/incr: %.2f "% (float(count_all) / float(decrement-1))) 
print("\n")
print(" There were", original_n - n, "numbers passed by with", decrement-1, "different increments.")
print(" Average numbers/incr: %.2f "% (float(original_n - n) / float(decrement-1)))
print("\n")
