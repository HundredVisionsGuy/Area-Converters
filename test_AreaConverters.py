# test_TempConverters.py
# Tests Temp Converter functions

import unittest
import AreaConverters

class KnownValues(unittest.TestCase):
    # Formula for unittest method is:
    # test_functionName_testDescription
    def test_kmToAcres_for10_10(self):
        # Capture the results of the function
        result = AreaConverters.kmToAcres(10,10)
        # Check for expected output
        self.assertEqual(24710.538, result)
    def test_kmToAcres_for10_100(self):
        # Capture the results of the function
        result = AreaConverters.kmToAcres(10,10)
        # Check for expected output
        self.assertEqual(247105.38, result)

    def test_kmToAcres_for25_25(self):
        # Capture the results of the function
        result = AreaConverters.kmToAcres(10,10)
        # Check for expected output
        self.assertEqual(247105.38, result)

    def test_kmToAcres_for50_2(self):
        # Capture the results of the function
        result = AreaConverters.kmToAcres(10,10)
        # Check for expected output
        self.assertEqual(24710.538, result)


    def test_yardsToAcres_for15_15(self):
        # Capture the results of the function
        result = AreaConverters.yardsToAcres(15,15)
        # Check for expected output
        self.assertEqual(55599.75, result)

    def test_yardsToAcres_for15_150(self):
        # Capture the results of the function
        result = AreaConverters.yardsToAcres(15,150)
        # Check for expected output
        self._baseAssertEqual(555997.5, result)

    def test_yardsToAcres_for100_200(self):
        # Capture the results of the function
        result = AreaConverters.yardsToAcres(100,200)
        # Check for expected output
        self._baseAssertEqual(4942200.0, result)

    def test_yardsToAcres_for40_20(self):
        # Capture the results of the function
        result = AreaConverters.yardsToAcres(100,200)
        # Check for expected output
        self._baseAssertEqual(197688.0, result)

# Run the tests
if __name__ == '__main__':
    unittest.main()
