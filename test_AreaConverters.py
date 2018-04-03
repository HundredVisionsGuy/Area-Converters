# test_TempConverters.py
# Tests Temp Converter functions

import unittest
import AreaConverters

class KnownValues(unittest.TestCase):
    # Formula for unittest method is:
    # test_functionName_testDescription
    def test_kmToAcres_for212F(self):
        # Capture the results of the function
        result = AreaConverters.kmToAcres(0,0)
        # Check for expected output
        self.assertEqual(100.0, result)

    def test_yardsToAcres_for0C(self):
        # Capture the results of the function
        result = AreaConverters.yardsToAcres(0,0)
        # Check for expected output
        self.assertEqual(32.0, result)

