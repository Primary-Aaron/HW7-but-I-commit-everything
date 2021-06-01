import unittest
import fizzBuzz

class test_(unittest.TestCase):
  def test_type(self):
    fizzy = fizzBuzz.fizzBuzz()
    message = "this ain't it, chief. gotta check that type"
    self.assertIsInstance(fizzy, list, message)