"""
LeetCode #1169 - Invalid Transactions
中文题名：查询无效交易
https://leetcode.com/problems/invalid-transactions/

A transaction is possibly invalid if:

the amount exceeds $1000, or;

if it occurs within (and including) 60 minutes of another transaction with the same name
in a different city.

Each transaction string `transactions[i]` consists of comma separated
values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of `transactions`, return a list of transactions that are
possibly invalid.  You may return the answer in any order.

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.

Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]

Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]

Constraints:

`transactions.length <= 1000`

Each `transactions[i]` takes the form `"{name},{time},{amount},{city}"`

Each `{name}` and `{city}` consist of lowercase English
letters, and have lengths between `1` and `10`.

Each `{time}` consist of digits, and represent an integer between `0`
and `1000`.

Each `{amount}` consist of digits, and represent an integer between
`0` and `2000`.

【中文翻译】
交易可能无效的情况包括：

金额超过 $1000；或者

在与另一笔同名交易的时间相差不超过 60 分钟（含 60 分钟）内，且发生地点与当前交易的城市不同。

每笔交易字符串 transactions[i] 由逗号分隔的值组成，分别表示交易的名称、时间（以分钟为单位）、金额和城市。

给定一个交易列表 transactions，返回所有可能无效的交易列表。你可以按任意顺序返回答案。

示例 1：

输入：transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
输出：["alice,20,800,mtv","alice,50,100,beijing"]
解释：第一笔交易无效，因为第二笔交易在 60 分钟时间差内发生，名字相同且在不同的城市。同理第二笔交易也无效。

示例 2：

输入：transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
输出：["alice,50,1200,mtv"]

示例 3：

输入：transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
输出：["bob,50,1200,mtv"]

约束条件：

`transactions.length <= 1000`

每笔交易 transactions[i] 的格式为 `"{name},{time},{amount},{city}"`

每个 {name} 和 {city} 仅由小写英文字母组成，长度在 1 到 10 之间。

每个 {time} 由数字组成，表示 0 到 1000 之间的整数。

每个 {amount} 由数字组成，表示 0 到 2000 之间的整数。
"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # Parse transactions into tuples
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city))

        n = len(parsed)
        invalid = [False] * n

        # Check each transaction
        for i in range(n):
            name_i, time_i, amount_i, city_i = parsed[i]

            # Condition 1: amount > 1000
            if amount_i > 1000:
                invalid[i] = True

            # Condition 2: same name, within 60 min, different city
            for j in range(n):
                if i == j:
                    continue
                name_j, time_j, amount_j, city_j = parsed[j]
                if (name_i == name_j and
                        abs(time_i - time_j) <= 60 and
                        city_i != city_j):
                    invalid[i] = True
                    break

        return [transactions[i] for i in range(n) if invalid[i]]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 暴力枚举法（输入规模 n <= 1000，O(n^2) 可行）：
# 1. 解析每笔交易字符串，提取 name、time、amount、city 四个字段。
# 2. 对每笔交易 i，检查两个无效条件：
#    a. amount > 1000（金额超过 1000）。
#    b. 存在另一笔交易 j，满足：
#       - name 相同
#       - |time_i - time_j| <= 60
#       - city_i != city_j
# 3. 将满足任一条件的交易标记为无效。
# 4. 返回所有标记为无效的原始交易字符串。
#
# 优化思路：可以按 name 分组，每组内按 time 排序后用滑动窗口检查。
# 但对于 n <= 1000，O(n^2) 足够。
#
# 时间复杂度: O(n^2) - 双重循环比较每笔交易
# 空间复杂度: O(n) - 存储解析后的交易和标记数组
#
# 关键点:
# - 两个条件是"或"的关系，满足任一即为无效
# - 条件二要求改名、时间差 <= 60、城市不同，三者同时满足
# - 一笔交易可能因为与多笔其他交易相关而无效
# - 返回的是原始字符串，不是解析后的元组
