"""
LeetCode #1409 - Queries on a Permutation With Key
中文题名：查询带键的排列
https://leetcode.com/problems/queries-on-a-permutation-with-key/

Given the array `queries` of positive integers between `1` and
`m`, you have to process all `queries[i]` (from `i=0`
to `i=queries.length-1`) according to the following rules:

In the beginning, you have the permutation `P=[1,2,3,...,m]`.

For the current `i`, find the position of `queries[i]` in
the permutation `P` (indexing from 0) and then move
this at the beginning of the permutation `P.` Notice that the
position of `queries[i]` in `P` is the result for `queries[i]`.

Return an array containing the result for the given `queries`.

Example 1:

Input: queries = [3,1,2,1], m = 5
Output: [2,1,2,1]
Explanation: The queries are processed as follow:
For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is 2, then we move 3 to the beginning of P resulting in P=[3,1,2,4,5].
For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is 1, then we move 1 to the beginning of P resulting in P=[1,3,2,4,5].
For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is 2, then we move 2 to the beginning of P resulting in P=[2,1,3,4,5].
For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is 1, then we move 1 to the beginning of P resulting in P=[1,2,3,4,5].
Therefore, the array containing the result is [2,1,2,1].

Example 2:

Input: queries = [4,1,2,2], m = 4
Output: [3,1,2,0]

Example 3:

Input: queries = [7,5,5,8,3], m = 8
Output: [6,5,0,7,5]

Constraints:

`1 <= m <= 10^3`

`1 <= queries.length <= m`

`1 <= queries[i] <= m`

【中文翻译】

给定一个正整数数组 `queries`，其中的值在 `1` 到 `m` 之间。请按照以下规则处理所有 `queries[i]`（从 `i=0` 到 `i=queries.length-1`）：

一开始，你有一个排列 `P = [1,2,3,...,m]`。

对于当前的 `i`，找到 `queries[i]` 在排列 `P` 中的位置（下标从 0 开始），然后将该元素移动到排列 `P` 的开头。注意，`queries[i]` 在 `P` 中的位置就是 `queries[i]` 的结果。

返回一个数组，包含给定 `queries` 的结果。

示例 1：
输入：queries = [3,1,2,1], m = 5
输出：[2,1,2,1]
解释：处理过程如下：
i=0：queries[i]=3, P=[1,2,3,4,5]，3 在 P 中的位置是 2，然后将 3 移到 P 的开头，得到 P=[3,1,2,4,5]。
i=1：queries[i]=1, P=[3,1,2,4,5]，1 在 P 中的位置是 1，然后将 1 移到 P 的开头，得到 P=[1,3,2,4,5]。
i=2：queries[i]=2, P=[1,3,2,4,5]，2 在 P 中的位置是 2，然后将 2 移到 P 的开头，得到 P=[2,1,3,4,5]。
i=3：queries[i]=1, P=[2,1,3,4,5]，1 在 P 中的位置是 1，然后将 1 移到 P 的开头，得到 P=[1,2,3,4,5]。
因此，包含结果的数组是 [2,1,2,1]。

示例 2：
输入：queries = [4,1,2,2], m = 4
输出：[3,1,2,0]

示例 3：
输入：queries = [7,5,5,8,3], m = 8
输出：[6,5,0,7,5]

约束条件：
`1 <= m <= 10^3`
`1 <= queries.length <= m`
`1 <= queries[i] <= m`

"""

from typing import List, Optional


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        # 初始化排列 P = [1, 2, 3, ..., m]
        P = list(range(1, m + 1))
        result = []

        for q in queries:
            # 找到 q 在 P 中的位置
            pos = P.index(q)
            result.append(pos)
            # 将 q 移动到 P 的开头
            P.pop(pos)
            P.insert(0, q)

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 模拟法（列表实现）：
# 1. 初始化排列 P = [1, 2, 3, ..., m]。
# 2. 遍历 queries 中的每个查询 q：
#    a. 使用 P.index(q) 找到 q 在当前 P 中的位置 pos。
#    b. 将 pos 加入结果数组。
#    c. 从 P 中删除该位置的元素，然后将其插入到 P 的开头（索引 0）。
# 3. 返回结果数组。
#
# 由于 m <= 10^3 且 queries.length <= m，O(N*Q) 的简单模拟方法可以通过。
# 更优解：使用 Fenwick 树（树状数组），可以实现 O((N+Q)log N) 的时间复杂度。
#
# 时间复杂度: O(Q * M)，其中 Q = len(queries)，M = m。每次 index() 和 pop/insert 都是 O(M)。
# 空间复杂度: O(M)，用于存储排列 P。
#
# 关键点:
# - 直接模拟排列的查找和移动操作
# - 对于小约束（m <= 1000），O(M*Q) 的朴素养解法即可通过
# - 更优方法：使用 BIT/Fenwick 树在线查询位置并更新










