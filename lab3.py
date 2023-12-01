import unittest

def sin(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Не число")
    result = 0
    term = x
    n = 1
    while abs(term) > 1e-6:
        result += term
        term = -term * x * x / ((2 * n) * (2 * n + 1))
        n += 1
    return result

def cos(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Не число")
    result = 1
    term = 1
    n = 1
    while abs(term) > 1e-6:
        term = -term * x * x / ((2 * n - 1) * (2 * n))
        result += term
        n += 1
    return result

def ln(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Аргумент должен быть числом")
    if x <= 0:
        raise ValueError("Аргумент логарифма должен быть больше нуля")
    if x >= 1:
        y = (x - 1) / x
        result = 0
        term = y
        i = 1
        while abs(term) > 1e-10:
            result += term / i
            i += 1
            term *= y
        return result
    else:        
        result = 0
        term = x - 1  
        k = 1
        while abs(term) > 1e-6:
            result += term / k
            term *= -(x - 1)
            k += 1
            
        return result

def sqrt(x):
    if not isinstance(x, int) and not isinstance(x, float):
        raise Exception("Не число")
    if x < 0:
        raise Exception("Аргумент корня должен быть неотрицательным")
    guess = x
    while True:
        next_guess = 0.5 * (guess + x / guess)
        if abs(next_guess - guess) < 1e-9:
            return next_guess
        guess = next_guess
        
def abs(x):
    if not isinstance(x, int) and not isinstance(x, float):
        raise Exception("Не число")
    elif x >= 0:
        return x
    else:
        return -x
        
def f(x):
    if not isinstance(x, int) and not isinstance(x, float):
        raise Exception("Не число")
    elif x >= 0:
        sin_x = sin(x)
        cos_x = cos(x)
        return abs(sin_x ** 2 - cos_x)
    else:
        sin_x = sin(x)
        cos_x = cos(x)
        return ln(sin_x) + sqrt(cos_x)
    
    

class func_tests(unittest.TestCase):
    def test_sin_correct(self):
        input = 0.6
        output = 0.5646424457142857
        
        result = sin(input)
        self.assertEqual(result, output)
        
    def test_sin_incorrect(self):
        input = 'fdgdgdsfg'
        
        with self.assertRaises(Exception):
            sin(input)
            
    def test_cos_correct(self):
        input = 0.6
        output = 0.8253356165714286
        
        result = cos(input)
        self.assertEqual(result, output)
        
    def test_cos_incorrect(self):
        input = 'fdgdgdsfg'
        
        with self.assertRaises(Exception):
            cos(input)
            
    def test_ln_correct(self):
        input = 0.6
        output = -0.5108255806633686
        
        result = ln(input)
        self.assertEqual(result, output)
        
    def test_ln_incorrect(self):
        input = 'fdgdgdsfg'
        
        with self.assertRaises(Exception):
            ln(input)
            
    def test_sqrt_correct(self):
        input = 4
        output = 2
        
        result = sqrt(input)
        self.assertEqual(result, output)
        
    def test_sqrt_incorrect(self):
        input = 'fdgdgdsfg'
        
        with self.assertRaises(Exception):
            sqrt(input)
            
    def test_sqrt_negetive(self):
        input = -4
        
        with self.assertRaises(Exception):
            sqrt(input)
            
    def test_abs_correct(self):
        input = 4
        output = 4
        
        result = abs(input)
        self.assertEqual(result, output)
        
    def test_abs_correct_negetive(self):
        input = -4
        output = 4
        
        result = abs(input)
        self.assertEqual(result, output)
        
    def test_abs_incorrect(self):
        input = 'fdgdgdsfg'
        
        with self.assertRaises(Exception):
            abs(input)



class IntegrationTests(unittest.TestCase):
    def test_positive_x(self):
        self.assertAlmostEqual(f(1), 0.16777115637394735)
        self.assertAlmostEqual(f(5), 0.6358727267127433)
        self.assertAlmostEqual(f(3.14), 1.0000012693244826)

    def test_non_numeric_x(self):
        with self.assertRaises(Exception):
            f("x")
        
    def test_sin(self):
        self.assertAlmostEqual(sin(1),  0.8414710097001764)
        
    def test_cos(self):
        self.assertAlmostEqual(cos(1), 0.540302303791887)
        
    def test_ln(self):
        self.assertAlmostEqual(ln(1), 0)
        self.assertAlmostEqual(ln(2), 0.6931471805566138)
        
    def test_sqrt(self):
        self.assertAlmostEqual(sqrt(0.5403023058681398), 0.7350525871447156)
          
if __name__ == '__main__':
    unittest.main()