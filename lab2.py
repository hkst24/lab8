import unittest
from lab1 import*

class test_BubbleSort(unittest.TestCase):
    def test_BubbleSort_correct(self):
        input_arr = [5, 2, 0, -1, 10]
        output_arr = [-1, 0, 2, 5, 10]
        
        result = BubbleSort(input_arr)
        self.assertEqual(result, output_arr)
        
    def test_BubbleSort_with_str(self):
        input_arr = ['dfhdfg']
        
        with self.assertRaises(Exception):
            BubbleSort(input_arr)
            
    def test_BubbleSort_with_empty_list(self):
        input_arr = []
        
        with self.assertRaises(Exception):
            BubbleSort(input_arr)
    
    def test_BubbleSort_with_not_list(self):
        input_arr = 10
        
        with self.assertRaises(Exception):
            BubbleSort(input_arr)
        
class test_palindrome(unittest.TestCase):
    def test_palindrome_correct_true(self):
        input = 'gvg'
        
        result = palindrome(input)
        self.assertTrue(result)
        
    def test_palindrome_correct_false(self):
        input = 'gvgv'
        
        result = palindrome(input)
        self.assertFalse(result)
        
    def test_palindrome_with_not_str(self):
        input = 5
        
        with self.assertRaises(Exception):
            palindrome(input)
        
class test_factorial(unittest.TestCase):
    def test_factorial_with_correct(self):
        input = 5
        output = 120
        
        result = factorial(input)
        self.assertEqual(result, output)
        
    def test_factorial_with_negative(self):
        input = -5
        
        with self.assertRaises(Exception):
            factorial(input)
        
    def test_factorial_with_float(self):
        input = 1.5
        
        with self.assertRaises(Exception):
            factorial(input)
            
class test_fibonacci(unittest.TestCase):
    def test_fibonacci_with_correct_positive(self):
        input = 10
        output = 55
        
        result = fibonacci(input)
        self.assertEqual(result, output)
        
    def test_fibonacci_with_correct_even_negative(self):
        input = -10
        output = -55
        
        result = fibonacci(input)
        self.assertEqual(result, output)
        
    def test_fibonacci_with_correct_odd_negative(self):
        input = -5
        output = 5
        
        result = fibonacci(input)
        self.assertEqual(result, output) 
        
    def test_fibonacci_with_not_int(self):
        input = 'dfgdsdf'
        
        with self.assertRaises(Exception):
            fibonacci(input)
            
class test_exponent(unittest.TestCase):
    def test_exponent_with_correct(self):
        input_num = 2.5
        input_exp = 2
        output = 6.25
        
        result = exponent(input_num, input_exp)
        self.assertEqual(result, output)
        
    def test_exponent_with_not_float_num(self):
        input_num = 'dsgfgdsf'
        input_exp = 2
        
        with self.assertRaises(Exception):
            exponent(input_num, input_exp)
        
    def test_exponent_with_not_float_exp(self):
        input_num = 5
        input_exp = 'dsgfgdsf'
        
        with self.assertRaises(Exception):
            exponent(input_num, input_exp) 
            
class test_simple(unittest.TestCase):
    def test_simple_with_correct_simple(self):
        input = 5
        output = True
        
        result = simple(input)
        self.assertTrue(result, output)
        
    def test_simple_with_correct_not_simple(self):
        input = 4
        output = False
        
        result = simple(input)
        self.assertFalse(result, output)
        
    def test_simple_with_correct_zero(self):
        input = 0
        output = False
        
        result = simple(input)
        self.assertFalse(result, output)
        
    def test_simple_with_not_int(self):
        input = 1.8
        
        with self.assertRaises(Exception):
            simple(input)
            
if __name__ == '__main__':
    unittest.main()