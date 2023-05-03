"""
Program: whoisTest.py
Author: Mahdi
Date: 16/04/2023
usage: python whois_test.py
"""

import unittest
import subprocess

class TestMyProgram(unittest.TestCase):
    """
    Test class for whois.py
    """
    def test_even_number(self):
        """
            Test whether the program correctly identifies an even number.
        """
        output = subprocess.check_output(['python', 'whois.py', '10'])
        self.assertEqual(output.decode('utf-8').strip(), "I'm Even.")
    def test_odd_number(self):
        """
            Test whether the program correctly identifies an odd number.
        """
        output = subprocess.check_output(['python', 'whois.py', '7'])
        self.assertEqual(output.decode('utf-8').strip(), "I'm Odd.")
    def test_non_numeric_argument(self):
        """
            Test whether the program correctly identifies a non-numeric argument.
        """
        with self.assertRaises(subprocess.CalledProcessError) as _cm:
            subprocess.check_output(['python', 'whois.py', 'abc'], stderr=subprocess.PIPE)
        self.assertIn("AssertionError: Argument is not a number",
                      _cm.exception.stderr.decode('utf-8').strip())
    def test_no_argument_given(self):
        """
            Test whether the program correctly identifies no argument given.
        """
        with self.assertRaises(subprocess.CalledProcessError) as _cm:
            subprocess.check_output(['python', 'whois.py'], stderr=subprocess.PIPE)
        self.assertIn("AssertionError: No argument given",
                      _cm.exception.stderr.decode('utf-8').strip())
    def test_multiple_arguments_given(self):
        """
            Test whether the program correctly identifies multiple arguments given.
        """
        with self.assertRaises(subprocess.CalledProcessError) as _cm:
            subprocess.check_output(['python', 'whois.py', '10', '20'], stderr=subprocess.PIPE)
        self.assertIn("AssertionError: Too many arguments given",
                      _cm.exception.stderr.decode('utf-8').strip())
if __name__ == '__main__':
    unittest.main()
