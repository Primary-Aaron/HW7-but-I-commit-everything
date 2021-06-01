import unittest
import leapYear

class test_(unittest.TestCase):
  def test_4(self):
    year = leapYear.isLeapYear(8)
    message = "this ain't it, chief"
    self.assertEqual(year, True, message)