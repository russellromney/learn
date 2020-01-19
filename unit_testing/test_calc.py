import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertRaises(ValueError, calc.add, 10, '1')
    
        with self.assertRaises(ValueError):
            calc.add(10,'a')



if __name__ == "__main__":
    unittest.main()