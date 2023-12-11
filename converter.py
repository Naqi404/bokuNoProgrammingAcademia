import unittest

class TestIntegerToRoman(unittest.TestCase):
    def test_convert_1(self):
        self.assertEqual(IntegerToRomanConverter.convert(1), "I")
    
    def test_convert_2(self):
        self.assertEqual(IntegerToRomanConverter.convert(5), "V")
    
    def test_convert_3(self):
        self.assertEqual(IntegerToRomanConverter.convert(1000), "M")
    
    def test_convert_4(self):
        self.assertTrue(IntegerToRomanConverter.convert(-1), "The roman numeral system doesnt have numbers 0 or below")


class IntegerToRomanConverter:
    def convert(number):
        numeral_dictionary = {
            1: "I", 4: "IV", 5: "V", 9: "IX",
            10: "X", 40: "XL", 50: "L", 90: "XC",
            100: "C", 400: "CD", 500: "D", 900: "CM",
            1000: "M"
        }
        if number <= 0:
            return("The roman numeral system doesnt have numbers 0 or below")
        
        while number > 0:
            result = ''
            for value, numeral in sorted(numeral_dictionary.items(), reverse=True):
                while number >= value:
                    result += numeral
                    number -= value
            return result
        
if __name__ == '__main__':
    unittest.main()