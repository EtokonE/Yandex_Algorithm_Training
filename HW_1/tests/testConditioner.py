import unittest
import sys
sys.path.append('/home/max/Data/algorithms/yandex')
from HW_1.tasks.A_Conditioner import conditioner

class testConditioner(unittest.TestCase):
    def test_freeze_low(self):
        room, cond, mode = 20, 10, 'freeze'
        result = conditioner(room, cond, mode)
        self.assertEqual(result, 10)

    def test_freeze_eq1(self):
        room, cond, mode = 20, 435345340, 'freeze'
        result = conditioner(room, cond, mode)
        self.assertEqual(result, 20)

    def test_fan(self):
        room, cond, mode = 5, 50, 'fan'
        result = conditioner(room, cond, mode)
        self.assertEqual(result, 5)

    def test_heat(self):
        room, cond, mode = 5, 50, 'heat'
        result = conditioner(room, cond, mode)
        self.assertEqual(result, 50)

    def test_heat_eq(self):
        room, cond, mode = 30, 20, 'heat'
        result = conditioner(room, cond, mode)
        self.assertEqual(result, 30)

    def test_heat_eq2(self):
        room, cond, mode = 30, 30, 'heat'
        result = conditioner(room, cond, mode)
        self.assertEqual(result, 30)

    def test_heat_nn(self):
        room, cond, mode = -30, 50, 'heat'
        result = conditioner(room, cond, mode)
        self.assertEqual(result, 50)

    def test_heat_nn2(self):
        room, cond, mode = 30, -50, 'heat'
        result = conditioner(room, cond, mode)
        self.assertEqual(result, 30)

    def test_freeze_nn(self):
        room, cond, mode = 30, -50, 'freeze'
        result = conditioner(room, cond, mode)
        self.assertEqual(result, -50)


if __name__ == '__main__':
    unittest.main()