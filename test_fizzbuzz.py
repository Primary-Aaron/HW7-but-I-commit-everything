import unittest
import fizzbuzz

class test_(unittest.TestCase):
  def test_type(self):
    fizzy = fizzbuzz.fizzBuzz()
    message = "this ain't it, chief. gotta check that type"
    self.assertIsInstance(fizzy, list, message)