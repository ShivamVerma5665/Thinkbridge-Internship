#Topic : Thinkbridge Internship --> First Program
#Author : Shivam Verma
#Problem Statement : Write a program that takes a number like 12345.67 and 
#                    prints "Rs. Twelve Thousand Three Hundred Forty Five 67/100"
#Programming language : Python
import timeit

def int_to_words(num):
    dict1 = { 0 : 'Zero', 1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five', \
          6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'nine', 10 : 'Ten', \
          11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen', \
          15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen', 18 : 'Eighteen', \
          19 : 'Ninteen', 20 : 'Twenty', \
          30 : 'Thirty', 40 : 'Fourth', 50 : 'Fifty', 60 : 'Sixty', \
          70 : 'Seventy', 80 : 'Eighty', 90 : 'Ninety' }                  
                                                                                    #Dictionary to store single and double digit numbers and suffixes
    size_hun = 1000                                                                 #initializing maxsize for 3 digit input
    size_thousand = size_hun * 1000                                                 #initializing maxsize for 4 digit input

    if (num < 20):                                                                  #condition check for numbers defined in above dictionary i.e. less than 20
        return dict1[num]                                                           #returning output dictionary to the main() function

    if (num < 100):                                                                 #condition check for numbers less than 100 
        if num % 10 == 0:                                                           #condition check in order to find whether the number is divisible by 10, 
            return dict1[num]                                                       #so it's value can be directly returned from the dictionary
        else:
            return dict1[num // 10 * 10] + ' ' + dict1[num % 10]                    #splitting the 2 digit number to return tens and units place from dictionary

    if (num < size_hun):                                                            #condition check to find if number include digit at hundreds place
        if num % 100 == 0:                                                          #condition check in order to find whether the number is divisible by 100,
            return dict1[num // 100] + ' hundred'                                   #so it's value can be directly returned from the dictionary by appending "hundred" to it at the end
        else:
            return dict1[num // 100] + ' hundred ' + int_to_words(num % 100)        #splitting the tree digit number so that "hundred" gets added after first digit's value and the remaining 2 digit's value ar tens and units place can be extracted from dictionary by calling the same function int_to_words()
    if (num < size_thousand):                                                       #condition check to find if number include digit at thousand place
        if num % size_hun == 0:                                                     #condition check in order to find whether the number is divisible by 1000,
            return int_to_words(num // size_hun) + ' thousand'                      #so it's value can be directly returned from the dictionary by appending "thousand" to it at the end
        else:
            return int_to_words(num // size_hun) + ' thousand, ' + int_to_words(num % size_hun) #splitting the tree digit number so that "thousand" gets added after first digit's value, "hundred" after second digits value 
                                                                                                #and the remaining  digit's value ar tens and units place can be extracted from dictionary by calling the same function int_to_words()
def main():
    print("\n\tCompiling time is :", (timeit.default_timer() - starttime), "usec")
    print("\n\t", "*"*25,"Currency Converter - Program 1","*"*25)
    ch = " "
    while True:                                                                                 #loop to provide usability after each run
        ch = input("\n\tDo you want to continue(y/n): ")
        if (ch.lower() == "y"):                                                         
            inp_num = input('\n\tPlease enter an integer between 1 and 9999(eg. 231.21): ')                       #taking currency as an input from user 
            num, frac = map(int, inp_num.split('.'))                                                  #splitting the integer and decimal part from given input
            print("\n\tGiven amount is Rs.",f"{int_to_words(num)} {frac}/100")                       #printing the desired output
        elif (ch.lower() == "n"):
            print("\n\tExiting Program...")
            print("\n\t", "*"*30,"Bye","*"*30,"\n")
            exit()                                                                                    #exit program(break while loop)
        else:
            print("\n\tInvalid Input\n\tPlease try again!")

if __name__ == "__main__":
    starttime = timeit.default_timer()
    # print("The start time is :",starttime)
    main()
    
'''
Output
         ************************* Currency Converter - Program 1 *************************

        Compiling is : 7.740000000922009e-07 usec

        Do you want to continue(y/n): y

        Please enter an integer between 1 and 9999: 12345.67

        Given amount is Rs.  Twelve thousand, Three hundred Fourth Five 67/100

        Do you want to continue(y/n): y

        Please enter an integer between 1 and 9999: 454.65

        Given amount is Rs.  Four hundred Fifty Four 65/100

        Please enter an integer between 1 and 9999: 54.3

        Given amount is Rs.  Fifty Four 3/100

        Do you want to continue(y/n): y   

        Please enter an integer between 1 and 9999: 4.54

        Given amount is Rs.  Four 54/100

        Exiting Program...

        ****************************** Bye ****************************** 

Output of Execution Time:

        ************************* Currency Converter - Program 1 *************************

        Given amount is Rs. One thousand, Two hundred Thirty Four 56/100

        The execution time is : 0.00014102800014370587 usec

        ****************************** Bye ****************************** 

'''
