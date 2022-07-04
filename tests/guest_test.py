import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.jim = Guest("Jim", 10)

    def test_guest_has_name(self):
        self.assertEqual("Jim", self.jim.name)

    def test_guest_has_wallet(self):
        self.assertEqual(10, self.jim.wallet)