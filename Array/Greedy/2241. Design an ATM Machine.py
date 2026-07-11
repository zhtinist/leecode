"""
LeetCode #2241 - Design an ATM Machine
设计一个 ATM 机器
https://leetcode.cn/problems/design-an-atm-machine/

一个 ATM 机器，存有 `5` 种面值的钞票：`20` ，`50` ，`100` ，`200` 和 `500` 美元。初始时，ATM 机是空的。用户可以用它存或者取任意数目的钱。
取款时，机器会优先取 较大 数额的钱。
比方说，你想取 `$300` ，并且机器里有 `2` 张 `$50` 的钞票，`1` 张 `$100` 的钞票和`1` 张 `$200` 的钞票，那么机器会取出 `$100` 和 `$200` 的钞票。
但是，如果你想取 `$600` ，机器里有 `3` 张 `$200` 的钞票和`1` 张 `$500` 的钞票，那么取款请求会被拒绝，因为机器会先取出 `$500` 的钞票，然后无法取出剩余的 `$100` 。注意，因为有 `$500` 钞票的存在，机器 不能 取 `$200` 的钞票。
请你实现 ATM 类：
`ATM()` 初始化 ATM 对象。
`void deposit(int[] banknotesCount)` 分别存入 `$20` ，`$50`，`$100`，`$200` 和 `$500` 钞票的数目。
`int[] withdraw(int amount)` 返回一个长度为 `5` 的数组，分别表示 `$20` ，`$50`，`$100` ，`$200` 和 `$500` 钞票的数目，并且更新 ATM 机里取款后钞票的剩余数量。如果无法取出指定数额的钱，请返回 `[-1]` （这种情况下 不 取出任何钞票）。

示例 1：
输入： ["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"] [[], [[0,0,1,2,1]], [600], [[0,1,0,1,1]], [600], [550]] 输出： [null, null, [0,0,1,0,1], null, [-1], [0,1,0,0,1]]  解释： ATM atm = new ATM(); atm.deposit([0,0,1,2,1]); // 存入 1 张 $100 ，2 张 $200 和 1 张 $500 的钞票。 atm.withdraw(600);        // 返回 [0,0,1,0,1] 。机器返回 1 张 $100 和 1 张 $500 的钞票。机器里剩余钞票的数量为 [0,0,0,2,0] 。 atm.deposit([0,1,0,1,1]); // 存入 1 张 $50 ，1 张 $200 和 1 张 $500 的钞票。                           // 机器中剩余钞票数量为 [0,1,0,3,1] 。 atm.withdraw(600);        // 返回 [-1] 。机器会尝试取出 $500 的钞票，然后无法得到剩余的 $100 ，所以取款请求会被拒绝。                           // 由于请求被拒绝，机器中钞票的数量不会发生改变。 atm.withdraw(550);        // 返回 [0,1,0,0,1] ，机器会返回 1 张 $50 的钞票和 1 张 $500 的钞票。

提示：
`banknotesCount.length == 5`
`0 <= banknotesCount[i] <= 10^9`
`1 <= amount <= 10^9`
总共 最多有 `5000` 次 `withdraw` 和 `deposit` 的调用。
函数 `withdraw` 和 `deposit` 至少各有 一次 调用。
"""

from typing import List, Optional


class ATM:

    def __init__(self):
        self.denominations = [20, 50, 100, 200, 500]
        self.counts = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.counts[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        result = [0] * 5
        remaining = amount

        # Greedy: always try larger denominations first
        for i in range(4, -1, -1):
            if remaining <= 0:
                break
            denom = self.denominations[i]
            take = min(remaining // denom, self.counts[i])
            result[i] = take
            remaining -= take * denom

        # If we cannot make exact change greedily, reject
        if remaining > 0:
            return [-1]

        # Deduct the withdrawn notes from storage
        for i in range(5):
            self.counts[i] -= result[i]

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Design, Array
#
# 解题思路:
# 初始化时存储5种面额 [20, 50, 100, 200, 500] 及其对应数量。
# deposit: 直接累加各面额的存入数量。
# withdraw: 采用贪心策略，从大面额到小面额依次尝试取款。
#   对于每种面额，尽可能多地取出（不超过剩余金额所需的张数和当前库存的张数）。
#   如果遍历完所有面额后仍有剩余金额，说明贪心方式无法凑出，返回 [-1] 且不修改库存。
#   否则，从库存中扣除已取出的钞票并返回结果。
# 注意：本题的取款规则强制要求优先使用大面额（贪心），而非寻找任意可行的组合。
#
# 时间复杂度: O(1) per operation — 面额数量固定为5，每次存取都是常数时间
# 空间复杂度: O(1) — 只存储5种面额的计数
#
# 关键点:
# - 贪心取款：从大到小尝试，每次取 min(需要张数, 库存张数)
# - 取款失败时不能修改库存（要先计算再确认）
# - 面额数量固定为5，所有操作 O(1)
