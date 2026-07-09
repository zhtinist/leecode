"""
LeetCode #150 - Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/

You are given an array of strings tokens that represents an arithmetic
expression in Reverse Polish Notation. Evaluate the expression and return an
integer that represents the value of the expression.

Example 1:
    Input: tokens = ["2","1","+","3","*"]
    Output: 9

Example 2:
    Input: tokens = ["4","13","5","/","+"]
    Output: 6

Example 3:
    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22

Constraints:
    1 <= tokens.length <= 10^4
    tokens[i] is "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]
