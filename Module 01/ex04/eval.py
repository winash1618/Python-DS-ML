"""
The goal of the exercise is to discover 2 useful methods for lists, tuples, dictionnaries
(iterable class objects more generally) named zip and enumerate.

@winash1618 ➜ /workspaces/Python-ML/Module 01/ex04 (main) $ python3
Python 3.10.4 (main, Mar 31 2022, 08:41:55) [GCC 7.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from eval import Evaluator
>>> words = ["Le", "Lorem", "Ipsum", "est", "simple"]
>>> coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
>>> Evaluator().zip_evaluate(coefs, words) // wrong in the subject
32.0
>>> words = ["Le", "Lorem", "Ipsum", "n", "est", "pas", "simple"]
>>> coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
>>> Evaluator().enumerate_evaluate(coefs, words)
-1
"""

class Evaluator:
    """
    Code a class Evaluator, that has two static functions named zip_evaluate and enumerate_evaluate.
    """
    def zip_evaluate(self, coefs, words) -> any:
        """
        compute the sum of the lengths of every words of
        a given list weighted by a list of coefficinents coefs
        """
        if not len(coefs) == len(words):
            return -1
        total = 0
        for coef, word in zip(coefs, words):
            total += coef * len(word)
        return total
    def enumerate_evaluate(self, coefs, words) -> any:
        """
        compute the sum of the lengths of every words of
        a given list weighted by a list of coefficinents coefs
        """
        if not len(coefs) == len(words):
            return -1
        total = 0
        for i, coef in enumerate(coefs):
            for j, word in enumerate(words):
                if i == j:
                    total += coef * len(word)
        return total
