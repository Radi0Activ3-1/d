import unittest
from nato_phonetic import frequency_counter, spell_word # type: ignore

class TestNatoPhonetic(unittest.TestCase):

    def test_frequency_counter(self):
        self.assertEqual(frequency_counter([1, 2, 2, 3, 3, 3]), {1: 1, 2: 2, 3: 3})
        self.assertEqual(frequency_counter(['a', 'b', 'a']), {'a': 2, 'b': 1})
        self.assertEqual(frequency_counter([]), {})

    def test_spell_word(self):
        self.assertEqual(spell_word('dog'), ['Delta', 'Oscar', 'Golf'])
        self.assertEqual(spell_word('cat'), ['Charlie', 'Alpha', 'Tango'])
        self.assertEqual(spell_word('Zebra'), ['Zulu', 'Echo', 'Bravo', 'Romeo', 'Alpha'])

if __name__ == '__main__':
    unittest.main()

