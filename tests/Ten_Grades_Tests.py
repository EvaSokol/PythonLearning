import unittest

from scripts.Ten_Grades_Scoring import TenGrades


class UnitTestsForTenGrades(unittest.TestCase):

    def test_allDifferent(self):
        self.assertEqual(TenGrades.score_dice([1, 2, 3, 4, 5]), 150)
        self.assertEqual(TenGrades.score_dice([4, 2, 1, 5, 3]), 150)

    def test_oneDice(self):
        self.assertEqual(TenGrades.score_dice([4]), 0)
        self.assertEqual(TenGrades.score_dice([1]), 100)
        self.assertEqual(TenGrades.score_dice([5]), 50)

    def test_twoDices(self):
        self.assertEqual(TenGrades.score_dice([1, 5]), 150)
        self.assertEqual(TenGrades.score_dice([2, 5]), 50)
        self.assertEqual(TenGrades.score_dice([5, 5]), 100)

    def test_threeDices(self):
        self.assertEqual(TenGrades.score_dice([1, 1, 1]), 1000)
        self.assertEqual(TenGrades.score_dice([2, 2, 2]), 200)
        self.assertEqual(TenGrades.score_dice([1, 2, 3]), 100)
        self.assertEqual(TenGrades.score_dice([5, 2, 3]), 50)
        self.assertEqual(TenGrades.score_dice([4, 1, 5]), 150)

    def test_fourDices(self):
        self.assertEqual(TenGrades.score_dice([5, 5, 5, 5]), 550)
        self.assertEqual(TenGrades.score_dice([4, 4, 4, 4]), 400)

    def test_fiveDices(self):
        self.assertEqual(TenGrades.score_dice([1, 2, 3, 4, 5]), 150)
        self.assertEqual(TenGrades.score_dice([1, 1, 1, 1, 1]), 1200)
        self.assertEqual(TenGrades.score_dice([3, 3, 3, 3, 3]), 300)

    def test_excessDices(self):
        self.assertEqual(TenGrades.score_dice([1, 2, 3, 4, 5, 6]), 0)

    def test_incorrectNumbers(self):
        self.assertEqual(TenGrades.score_dice([8, 7, 9, 8]), 0)

