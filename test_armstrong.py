import unittest

from armstrong import is_armstrong, generate_armstrong


class TestArmstrong(unittest.TestCase):
    def test_known_armstrongs_base10(self):
        self.assertTrue(is_armstrong(0))
        self.assertTrue(is_armstrong(1))
        self.assertTrue(is_armstrong(153))
        self.assertTrue(is_armstrong(370))
        self.assertTrue(is_armstrong(371))
        self.assertTrue(is_armstrong(407))

    def test_non_armstrong_base10(self):
        for n in (2, 10, 100, 154, 372, 408):
            self.assertFalse(is_armstrong(n))

    def test_generate_up_to_1000(self):
        nums = generate_armstrong(1000)
        expected = [0, 1, 153, 370, 371, 407]
        self.assertEqual(nums, expected)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            generate_armstrong(-1)
        with self.assertRaises(ValueError):
            is_armstrong(10, base=1)


if __name__ == "__main__":
    unittest.main()
