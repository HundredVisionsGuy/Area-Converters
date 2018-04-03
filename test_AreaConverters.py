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
        result = AreaConverters.kmToAcres(10,100)
        # Check for expected output
        self.assertEqual(247105.38, result)

    def test_kmToAcres_for25_25(self):
        # Capture the results of the function
        result = AreaConverters.kmToAcres(25,25)
        # Check for expected output
        self.assertEqual(154440.8625, result)

    def test_kmToAcres_for25_3(self):
        # Capture the results of the function
        result = AreaConverters.kmToAcres(25,3)
        # Check for expected output
        self.assertEqual(18532.9035, result)


    def test_yardsToAcres_for15_15(self):
        # Capture the results of the function
        result = AreaConverters.yardsToAcres(15,15)
        # Check for expected output
        self.assertEqual(0.046575, result)

    def test_yardsToAcres_for15_150(self):
        # Capture the results of the function
        result = AreaConverters.yardsToAcres(15,150)
        # Check for expected output
        self._baseAssertEqual(0.46575, result)

    def test_yardsToAcres_for100_200(self):
        # Capture the results of the function
        result = AreaConverters.yardsToAcres(100,200)
        # Check for expected output
        self._baseAssertEqual(4.14, result)

    def test_yardsToAcres_for40_20(self):
        # Capture the results of the function
        result = AreaConverters.yardsToAcres(40,20)
        # Check for expected output
        self._baseAssertEqual(0.1656, result)

# Run the tests
if __name__ == '__main__':
    unittest.main()
