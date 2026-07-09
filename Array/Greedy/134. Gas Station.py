"""
LeetCode #134 - Gas Station
https://leetcode.com/problems/gas-station/

There are n gas stations along a circular route, where the amount of gas at the
ith station is gas[i]. You have a car with an unlimited gas tank and it costs
cost[i] of gas to travel from the ith station to its next (i + 1)th station.
You begin the journey with an empty tank at one of the gas stations. Given two
integer arrays gas and cost, return the starting gas station's index if you can
travel around the circuit once in the clockwise direction, otherwise return -1.

Example 1:
    Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    Output: 3

Example 2:
    Input: gas = [2,3,4], cost = [3,4,3]
    Output: -1

Constraints:
    gas.length == n
    cost.length == n
    1 <= n <= 10^5
    0 <= gas[i], cost[i] <= 10^4
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = current_tank = start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            current_tank += diff

            if current_tank < 0:
                start = i + 1
                current_tank = 0

        return start if total_tank >= 0 else -1
