"""
LeetCode #170 - Two Sum III - Data structure design
https://leetcode.com/problems/two-sum-iii-data-structure-design/

Design a data structure that accepts a stream of integers and checks if it has
a pair of integers that sum up to a specific value.

Implement the TwoSum class:
- TwoSum() Initializes the TwoSum object, with an empty array initially.
- void add(int number) Adds number to the data structure.
- boolean find(int value) Returns true if there exists any pair of numbers
  whose sum is equal to value, otherwise, it returns false.

Example 1:
    Input: ["TwoSum","add","add","add","find","find"]
           [[],[1],[3],[5],[4],[7]]
    Output: [null,null,null,null,true,false]
    Explanation:
    TwoSum twoSum = new TwoSum();
    twoSum.add(1); twoSum.add(3); twoSum.add(5);
    twoSum.find(4) --> true
    twoSum.find(7) --> false

Constraints:
    -10^5 <= number <= 10^5
    -2^31 <= value <= 2^31 - 1
    At most 10^4 calls will be made to add and find.
    At most one valid pair exists.
"""

from collections import defaultdict


class TwoSum:
    def __init__(self):
        self.count = defaultdict(int)

    def add(self, number: int) -> None:
        self.count[number] += 1

    def find(self, value: int) -> bool:
        for num, freq in self.count.items():
            complement = value - num
            if complement not in self.count:
                continue
            if complement != num or freq > 1:
                return True
        return False
