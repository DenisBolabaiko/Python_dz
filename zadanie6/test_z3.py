import unittest
import sys
import time
from z3 import factorial


class TestFactorial(unittest.TestCase):
    def stertTime(self):
        self.starttime = time.time()
        print(self.starttime)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(1000)
        self.assertEqual(factorial(1), 1)


    def finishTime(self):
        self.ourTime = time.time()
        print(self.ourTime)

