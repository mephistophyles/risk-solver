import unittest

from risk_monte_carlo import simulate_round, run_simulations, roll_dice


class DiceRollTests(unittest.TestCase):

    def test_rolls_amount(self):
        self.assertEqual(len(roll_dice(2)), 2)
        self.assertEqual(len(roll_dice(1)), 1)
        self.assertEqual(len(roll_dice(3)), 3)
        self.assertEqual(len(roll_dice(10)), 10)

    def test_rolls_sorted(self):
        result = roll_dice(3)
        self.assertGreaterEqual(result[0], result[1])
        self.assertGreaterEqual(result[0], result[2])
        self.assertGreaterEqual(result[1], result[2])
        result2 = roll_dice(10)
        self.assertGreaterEqual(result2[0], result2[-1])


class SimulateRoundTests(unittest.TestCase):

    def test_returns_same_if_one_attacker(self):
        self.assertEqual(simulate_round(1, 1), (1, 1))


if __name__ == '__main__':
    unittest.main()
