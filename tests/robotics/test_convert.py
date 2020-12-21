import unittest
import os
import sys
import math
parent = os.path.dirname(__file__)
sys.path.insert(0, parent)
import src.robotics.convert as convert

class TestConvert(unittest.TestCase):
    def test_quaternion2euler(self):
        q = [0, 0, 0.7072, 0.7072]
        r, p, y = convert.euler_from_quaternion(*q)
        self.assertEqual(r, 0, "bad roll")
        self.assertEqual(p, 0, "bad pitch")
        self.assertEqual(round(y,2), round(math.pi/2, 2), "bad yaw")
