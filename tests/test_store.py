
from unittest import TestCase


class TestStore(TestCase):

    def test_default(self):

        self.assertEqual('foo'.upper(), 'FOO')
