"""
LeetCode #157 - Read N Characters Given Read4
https://leetcode.com/problems/read-n-characters-given-read4/

Given a file and n, return the number of characters read.

The read4 API is defined as:

    def read4(buf4):
        # Read 4 characters from file into buf4.
        # The length of the actual characters read is returned.

You may assume the file is valid and has at least n characters.

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
    def read(self, buf, n: int) -> int:
        copied = 0

        while n > 0:
            chunk = [" "] * 4
            read_len = read4(chunk)
            if read_len == 0:
                break

            for i in range(read_len):
                if n == 0:
                    break
                buf[copied] = chunk[i]
                copied += 1
                n -= 1

        return copied
