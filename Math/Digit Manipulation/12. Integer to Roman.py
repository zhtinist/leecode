"""
LeetCode #12 - Integer to Roman
https://leetcode.com/problems/integer-to-roman/

Seven different symbols represent Roman numerals with the following values:

    Symbol    Value
    M         1000
    D         500
    C         100
    L         50
    X         10
    V         5
    I         1

Roman numerals are formed by appending the conversions of decimal place values
from highest to lowest. Converting a decimal place value into a Roman numeral
has the following rules:

1. If the value does not start with 4 or 9, select the symbol of the maximal
   value that can be subtracted from the input, append that symbol to the
   result, subtract its value, and convert the remainder to a Roman numeral.

2. If the value starts with 4 or 9 use the subtractive form representing one
   symbol subtracted from the following symbol, for example, 4 is 1 (I) less
   than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following
   subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD)
   and 900 (CM).

3. Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times
   to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D)
   multiple times. If you need to append a symbol 4 times use the subtractive
   form.

Given an integer, convert it to a Roman numeral.

Example 1:
    Input: num = 3749
    Output: "MMMDCCXLIX"

Example 2:
    Input: num = 58
    Output: "LVIII"

Example 3:
    Input: num = 1994
    Output: "MCMXCIV"

Constraints:
    1 <= num <= 3999
"""


class Solution:
    # Each index is the Roman form for that digit (0~9) at a given place value
    THOUSANDS = ["", "M", "MM", "MMM"]
    HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    def digitToRoman(self, digit: int, place: str) -> str:
        """Convert one decimal digit (0~9) at the given place to Roman symbols."""
        if place == "thousand":
            return self.THOUSANDS[digit]
        if place == "hundred":
            return self.HUNDREDS[digit]
        if place == "ten":
            return self.TENS[digit]
        return self.ONES[digit]

    def intToRoman(self, num: int) -> str:
        return (
            self.digitToRoman(num // 1000, "thousand")
            + self.digitToRoman((num % 1000) // 100, "hundred")
            + self.digitToRoman((num % 100) // 10, "ten")
            + self.digitToRoman(num % 10, "one")
        )
