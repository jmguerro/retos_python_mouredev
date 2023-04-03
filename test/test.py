import unittest

from main import Fizzbuzz


class FizzbuzzTestCase(unittest.TestCase):
    def test_fizz_buzz(self):
         self.assertEquals("buzz",Fizzbuzz.fizz_with_param(5))










    if __name__ == '__main__':
        unittest.main()