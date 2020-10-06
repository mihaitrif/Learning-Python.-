# Roman Numeral Equivalent
# For this exercise, start by creating a variable and assigning it a randomly generated integer between and inclusive of both 1 and 10.

# Then, using your knowledge of if, elif, and else statements, create a program which prints the roman numeral equivalent of the randomly generated number.

# For example, if the randomly generated integer was 9, then the program would say that the roman numeral equivalent of 9 is IX in the output.



#solutia lui

#from random import randint

#one_to_ten = randint(1, 10)

#if one_to_ten == 1:
   # print("The roman numeral equivalent of " + str(one_to_ten) + " is I.")
#lif one_to_ten == 2:
    #print("The roman numeral equivalent of " + str(one_to_ten) + " is II.")
#elif one_to_ten == 3:
    #print("The roman numeral equivalent of " + str(one_to_ten) + " is III.")
#elif one_to_ten == 4:
    #print("The roman numeral equivalent of " + str(one_to_ten) + " is IV.")
#elif one_to_ten == 5:
   # print("The roman numeral equivalent of " + str(one_to_ten) + " is V.")
#elif one_to_ten == 6:
   # print("The roman numeral equivalent of " + str(one_to_ten) + " is VI.")
#elif one_to_ten == 7:
    #print("The roman numeral equivalent of " + str(one_to_ten) + " is VII.")
#elif one_to_ten == 8:
   #print("The roman numeral equivalent of " + str(one_to_ten) + " is VIII.")
#elif one_to_ten == 9:
   # print("The roman numeral equivalent of " + str(one_to_ten) + " is IX.")
#else:
   #print("The roman numeral equivalent of " + str(one_to_ten) + " is X.")

import random

number = int(random.randint(1, 10))

if number == 10:
    print("Then roman numeral number equivalent of 10 is X.")
elif number == 9:
    print("Then roman numeral number equivalent of 9 is IX.")
elif number == 8:
    print("Then roman numeral number equivalent of 8 is VIII.")
elif number == 7:
    print("Then roman numeral number equivalent of 7 is VII.")
elif number == 6:
    print("Then roman numeral number equivalent of 6 is VI.")
elif number == 5:
    print("Then roman numeral number equivalent of 5 is V.")
elif number == 4:
    print("Then roman numeral number equivalent of 4 is IV.")
elif number == 3:
    print("Then roman numeral number equivalent of 3 is III.")
elif number == 2:
    print("Then roman numeral number equivalent of 2 is II.")
else:
    print("Then roman numeral number equivalent of 1 is I.")