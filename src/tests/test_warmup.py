import unittest
from warmup.transfiorm_dictionary import transform_dictionary

class TestTransformDictionary(unittest.TestCase):
    def test_transform_integers(self):
        input_dict = {'a': 1, 'b': 2, 'c': 3}
        expected_dict = {'a': 2, 'b': 3, 'c': 4}
        transform_dictionary(input_dict)
        self.assertEqual(input_dict, expected_dict)

    def test_transform_floats(self):
        input_dict = {'a': 1.5, 'b': 2.5, 'c': 3.5}
        expected_dict = {'a': 2.5, 'b': 3.5, 'c': 4.5}
        transform_dictionary(input_dict)
        self.assertEqual(input_dict, expected_dict)

    def test_transform_strings(self):
        input_dict = {'a': 'hello', 'b': 'world', 'c': 'foo'}
        expected_dict = {'a': 'hello AE', 'b': 'world AE', 'c': 'foo AE'}
        transform_dictionary(input_dict)
        self.assertEqual(input_dict, expected_dict)

    def test_transform_mixed_types(self):
        input_dict = {'a': 1, 'b': 2.5, 'c': 'hello'}
        expected_dict = {'a': 2, 'b': 3.5, 'c': 'hello AE'}
        transform_dictionary(input_dict)
        self.assertEqual(input_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()