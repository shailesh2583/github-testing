import math
import numpy as np

def square(x):
    '''
    This is a demo function
    Where in you just return square of the number
    args:
        x (int)
    returns:
        x*x (int)
    '''

    ## Code Here
    # return x**2

def word_is_palindrome(string):
    '''
    This function returns True if the given string is
    a Palindrome
    args:
        string (str)
    returns:
        flag (bool)
    '''

    ## Code Here
    # return string == string[::-1]

def sqrt_of_numbers(num):
    '''
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float) rounded off upto 2 decimal places.
    '''

    # if num < 0:
    #     raise ValueError('Number must be positive')
    # else:
    #     return round(math.sqrt(num), 2)

def Maximum(arr):
    '''
    This function returns first maximum and the second maximum
    number in the array
    args:
        arr (array)
    returns:
        Max1, Max2 (int, int)
    '''

    # arr = np.sort(arr)
    # arr = arr[::-1]
    # return arr[0], arr[1]

def even_sort(arr):
    '''
    This function sorts the array giving higher preference to even numbers
    args:
        arr (list)
    returns:
        sort_arr (list)
    ex:
        arr = [15, 2, 6, 88, 7]
        ## then
        sort_arr = [2, 6, 88 ,7 ,15]
        ## This is any even number is smaller than any odd number
    '''
    # even = []
    # odd = []
    # for i in arr:
    #     if i%2 == 0:
    #         even.append(i)
    #     else:
    #         odd.append(i)
    
    # even.sort()
    # odd.sort()

    # return even + odd

def eqn_solver(A, B, C):
    '''
    This function solves a two variable system
    i.e.,
        A = [ 1, 2 ]
        B = [ 3, 4 ]
        C = [ 5, 6 ]
        then it means
        1x + 3y = 5
        2x + 4y = 6
        Hence you are required to find x, y for such a linear system
    args:
        A, B, C (list, list, list) representing coefficients in the equation
    returns:
        x, y (float, float)
    '''

    # A = np.array([[A[0], B[0]], [A[1], B[1]]])
    # B = np.array([C[0], C[1]]).T

    # X = np.linalg.solve(A, B)
    
    # return X[0], X[1]

def swap_case(string):
    '''
    This function swaps the case of the string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string = 'Hello World'
        ## then
        string = 'hELLO wORLD'
    '''

    # string = list(string)

    # for i in range(len(string)):
    #         if string[i].islower():
    #             string[i] = string[i].upper()
    #         else:
    #             string[i] = string[i].lower()

    # return ''.join(string)

def is_prime(num):
    '''
    This function returns True if the number is prime
    args:
        num (int)
    returns:
        flag (bool)
    '''

    # prime_flag = 0
 
    # if(num > 1):
    #     for i in range(2, int(math.sqrt(num)) + 1):
    #         if (num % i == 0):
    #             prime_flag = 1
    #             break
    #     if (prime_flag == 0):
    #         return True
    #     else:
    #         return False
    # else:
    #     return False

def is_leap_year(year):
    '''
    This function returns True if the year is leap year
    args:
        year (int)
    returns:
        flag (bool)
    '''

    # if (year % 4) == 0:
    #     if (year % 100) == 0:
    #         if (year % 400) == 0:
    #             return True
    #         else:
    #             return False
    #     else:
    #          return True
    # else:
    #     return False

def is_perfect_square(num):
    '''
    This function returns True if the number is perfect square i.e. it is a square of some integer.
    args:
        num (int)
    returns:
        flag (bool)
    '''

    # if(num >= 0):
    #     sr = int(math.sqrt(num))
    #     return ((sr*sr) == num)
    # return False

def is_perfect_number(num):
    '''
    This function returns True if the number is perfect number.
    A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
    For example 6 is a perfect number because 1+2+3 = 6
    args:
        num (int)
    returns:
        flag (bool)
    '''

    # sum1 = 0
    # for i in range(1, num):
    #     if(num % i == 0):
    #         sum1 = sum1 + i
    # if (sum1 == num):
    #     return True
    # else:
    #     return False

def resize_array(a):
    '''
    This function resizes a 1D array to 2D array of size 2x3
    args:
        a (np.array) of size 1x6
    returns:
        b (np.array) of size 2x3
    '''

    # a = np.array(a)
    # return a.reshape(2, 3)

def reverse_step_array(a):
    '''
    This function returns the reversed array with step size of 3.
    args:
        a (np.array)
    returns:
        b (np.array)
    ex:
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ## then
        b = [9, 6, 3]
    '''

    # return a[::-3]

def reverse_words(string):
    '''
    This function reverses the words in the string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string = 'Hello Again World'
        ## then
        string = 'World Again Hello'
    '''

    # words = string.split(' ')
    # words = words[::-1]

    # return ' '.join(words)

def count_characters(string):
    '''
    This function counts the frequency of characters(ignore spaces as characters) in the input string.
    args:
        string (str)
    returns:
        dict (dict)
    ex:
        string = 'Hello World'
        ## then
        dict = {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'W': 1, 'r': 1, 'd': 1}
    '''
    # freq = dict()
    # for c in string:
    #     if c == ' ':
    #         continue
    #     elif c in freq:
    #         freq[c] += 1
    #     else:
    #         freq[c] = 1
    # return freq

def remove_special_characters(string):
    '''
    This function removes the special characters from the input string. Special characters are those which are not letters or numbers.
    args:
        string (str)
    returns:
        string (str)
    ex:
        str = 'Hello, World! 123$ th15 1s 4 t35t str1ng'
        ## then
        str = 'Hello World 123 th15 1s 4 t35t str1ng'
    '''
    # string = list(string)

    # for i in range(len(string)):
    #     if string[i] == ' ':
    #         continue
    #     elif not string[i].isalnum():
    #         string[i] = ''

    # return ''.join(string)

def sort_tuple_of_tuples(tuple):
    '''
    This function sorts the input tuple of tuples by the second item.
    args:
        tuple (tuple)
    returns:
        tuple (tuple)
    ex:
        tuple: (('a', 55), ('z', 1), ('f', 37), ('w', 19))
        ## then
        tuple: (('z', 1), ('w', 19), ('f', 37), ('a', 55))
    '''
    # t = tuple()
    # t
    # return tuple()
    return None

def alpha_numeric_words(string):
    '''
    This function finds words with both alphabets and numbers from an input string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string: "Hey there33 how11 are you1"
        ## then
        string: "there33 how11 you1"
    '''

    ## Code Here
    return None

def count_them_all(string):
    '''
    This function counts all letters, digits, and special symbols from an input string.
    args:
        string (str)
    returns:
        dict (dict)
    ex:
        string: "IdDk3837#$fsd%%"
        ## then
        dict: {'Characters': 7, 'Numbers': 4, 'Symbols': 4}
    '''

    ## Code Here
    return None

def hash_supremacy(string):
    '''
    This function replaces each special symbol with '#' in the input string.
    args:
        string (str)
    returns:
        string (str)
    ex:
        string: "&He was a^%$ great @guy"
        ## then
        string: "#He was a### great #guy"
    '''

    ## Code Here
    return None






