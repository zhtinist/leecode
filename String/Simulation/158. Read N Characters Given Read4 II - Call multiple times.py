"""
LeetCode #158 - Read N Characters Given Read4 II - Call multiple times
https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

Given a file and n, return the number of characters read.

The read4 API is defined as:

    def read4(buf4):
        # Read 4 characters from file into buf4.
        # The length of the actual characters read is returned.

You may call read4 multiple times. You may assume the file is valid and has at
least n characters.

Example 1:
    Input: file = "abc", n = 4
    Output: 3

Example 2:
    Input: file = "abcde", n = 5
    Output: 5

Constraints:
    1 <= n <= 10^4
"""


class Solution:
    def __init__(self):
        self.buffer = []
        self.buffer_ptr = 0

    def read(self, buf, n: int) -> int:
        copied = 0

        while copied < n:
            if self.buffer_ptr == len(self.buffer):
                self.buffer = [" "] * 4
                self.buffer_ptr = 0
                read_len = read4(self.buffer)
                if read_len == 0:
                    break
                self.buffer = self.buffer[:read_len]

            buf[copied] = self.buffer[self.buffer_ptr]
            self.buffer_ptr += 1
            copied += 1

        return copied
