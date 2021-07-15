from solution import PairValidator
import unittest


class PairValidatorTests(unittest.TestCase):

    def test1(self):
        solution = PairValidator()
        self.assertEqual(solution.validate("CAT", "SAD"), True)

    def test2(self):
        solution = PairValidator()
        self.assertEqual(solution.validate("BBB", "ABC"), True)


if __name__ == '__main__':
    unittest.main()
    # solution = PairValidator()
    # solution.validate("CAT", "SAD")
