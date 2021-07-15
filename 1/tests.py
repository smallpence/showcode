from main import Solution
import unittest


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        self.assertEqual(solution.devvie("RF"), 3)

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.devvie("FxLxLxFx"), 0)


if __name__ == '__main__':
    unittest.main()