import unittest

import math

def is_prime(num):
    '''Check if num is prime or not.'''
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

class TestPrime(unittest.TestCase):
    def test_two(self):
        self.assertFalse(is_prime(2))
    
    def test_five(self):
     self.assertTrue(is_prime(5))
    
    def test_nine(self):
     self.assertFalse(is_prime(9))
    
    def test_eleven(self):
     self.assertTrue(is_prime(11))

if __name__=='__main__':
    unittest.main()