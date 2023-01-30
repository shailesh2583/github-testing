import unittest
import assgn1_soln
import numpy as np

class Testassgn1_soln(unittest.TestCase):

    def test_square(self):
        self.assertEqual(assgn1_soln.square(4), 16)

    def test_word_is_palindrome(self):
        self.assertEqual(assgn1_soln.word_is_palindrome('madam'), True)
        self.assertEqual(assgn1_soln.word_is_palindrome('abcd'), False)
        self.assertEqual(assgn1_soln.word_is_palindrome('12321'), True)
        self.assertEqual(assgn1_soln.word_is_palindrome('abc cba'), True)

    def test_sqrt_of_numbers(self):
        self.assertEqual(assgn1_soln.sqrt_of_numbers(4), 2)
        self.assertEqual(assgn1_soln.sqrt_of_numbers(6), 2.45)
        self.assertEqual(assgn1_soln.sqrt_of_numbers(9.0), 3.0)
        self.assertEqual(assgn1_soln.sqrt_of_numbers(68), 8.25)
        # self.assertRaises(ValueError, assgn1_soln.sqrt_of_numbers, -1)

    def test_Maximum(self):
        self.assertEqual(assgn1_soln.Maximum([1,2,3,4,5]), (5,4))
    
    def test_even_sort(self):
        self.assertEqual(assgn1_soln.even_sort([1,2,3,4,5]), [2,4,1,3,5])

    def test_eqn_solver(self):
        self.assertEqual(assgn1_soln.eqn_solver([1,2], [3,4], [5,6]), (-1.0, 2.0))

    def test_swap_case(self):
        self.assertEqual(assgn1_soln.swap_case('Hello'), 'hELLO')
        self.assertEqual(assgn1_soln.swap_case('Hello World'), 'hELLO wORLD')

    def test_is_prime(self):
        self.assertEqual(assgn1_soln.is_prime(5), True)
        self.assertEqual(assgn1_soln.is_prime(4), False)

    def test_is_leap_year(self):
        self.assertEqual(assgn1_soln.is_leap_year(2000), True)
        self.assertEqual(assgn1_soln.is_leap_year(2001), False)
        self.assertEqual(assgn1_soln.is_leap_year(2004), True)
        self.assertEqual(assgn1_soln.is_leap_year(1700), False)

    def test_is_perfect_square(self):
        self.assertEqual(assgn1_soln.is_perfect_square(4), True)
        self.assertEqual(assgn1_soln.is_perfect_square(5), False)

    def test_is_perfect_number(self):
        self.assertEqual(assgn1_soln.is_perfect_number(6), True)
        self.assertEqual(assgn1_soln.is_perfect_number(5), False)

    def test_resize_array(self):
        self.assertEqual(assgn1_soln.resize_array([1,2,3,4,5,6]).tolist(), np.array([[1,2,3],[4,5,6]]).tolist())

    def test_reverse_step_array(self):
        self.assertEqual(assgn1_soln.reverse_step_array([1, 2, 3, 4, 5, 6, 7, 8, 9]), [9, 6, 3])

    def test_reverse_words(self):
        self.assertEqual(assgn1_soln.reverse_words('Hello World'), 'World Hello')
        self.assertEqual(assgn1_soln.reverse_words('hehe gotcha'), 'gotcha hehe')

    def test_count_characters(self):
        self.assertEqual(assgn1_soln.count_characters('Hello World'), {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'W': 1, 'r': 1, 'd': 1})
        self.assertEqual(assgn1_soln.count_characters("hehe gotcha"), {'h': 3, 'e': 2, 'g': 1, 'o': 1, 't': 1, 'c': 1, 'a': 1})
        self.assertEqual(assgn1_soln.count_characters("aaa111   bbb"), {'a': 3, '1': 3, 'b': 3})
        self.assertEqual(assgn1_soln.count_characters("      "), {})

    def test_remove_special_characters(self):
        self.assertEqual(assgn1_soln.remove_special_characters("Hello, World! 123$ th15 1s 4 t35t str1ng"), "Hello World 123 th15 1s 4 t35t str1ng")
        self.assertEqual(assgn1_soln.remove_special_characters("he##llo123%  *-  abc 12  ab23"), "hello123    abc 12  ab23")
        self.assertEqual(assgn1_soln.remove_special_characters("###"), "")
        self.assertEqual(assgn1_soln.remove_special_characters("### "), " ")

    # def test_tuple_of_tuples(self):
    #     self.assertEqual(assgn1_soln.sort_tuple_of_tuples((('a', 55), ('z', 1), ('f', 37), ('w', 19))), (('z', 1), ('w', 19), ('f', 37), ('a', 55)))

    # def test_alpha_numeric_words(self):
    #     self.assertEqual(assgn1_soln.alpha_numeric_words("Hey there33 how11 are you1"), "there33 how11 you1")
    #     self.assertEqual(assgn1_soln.alpha_numeric_words("hey"), "")
    #     self.assertEqual(assgn1_soln.alpha_numeric_words(""), "")

    # def test_count_them_all(self):
    #     self.assertEqual(assgn1_soln.count_them_all("IdDk3837#$fsd%%"), {'Characters': 7, 'Numbers': 4, 'Symbols': 4})

    # def test_hash_supremacy(self):
        # self.assertEqual(assgn1_soln.hash_supremacy("&He was a^%$ great @guy"), "#He was a### great #guy")
        


if __name__ == '__main__':
    unittest.main()