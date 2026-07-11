"""
LeetCode #851 - Loud and Rich
中文题名：喧闹和富有
https://leetcode.com/problems/loud-and-rich/

In a group of N people (labelled `0, 1, 2, ..., N-1`), each person has different
amounts of money, and different levels of quietness.

For convenience, we'll call the person with label `x`, simply "person
`x`".

We'll say that `richer[i] = [x, y]` if person `x` definitely
has more money than person `y`.  Note that `richer` may
only be a subset of valid observations.

Also, we'll say `quiet[x] = q` if person x has
quietness `q`.

Now, return `answer`, where `answer[x] = y` if `y` is the
least quiet person (that is, the person `y` with the smallest value of `quiet[y]`),
among all people who definitely have equal to or more money than person
`x`.

Example 1:

Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
Output: [5,5,2,5,4,5,6,7]
Explanation:
answer[0] = 5.
Person 5 has more money than 3, which has more money than 1, which has more money than 0.
The only person who is quieter (has lower quiet[x]) is person 7, but
it isn't clear if they have more money than person 0.

answer[7] = 7.
Among all people that definitely have equal to or more money than person 7
(which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x])
is person 7.

The other answers can be filled out with similar reasoning.

【中文翻译】
在一组有 N 个人（标号为 0, 1, 2, ..., N-1）中，每个人的金钱数量不同，安静程度也不同。
为了方便，我们将标号为 x 的人简称为 "person x"。

如果 richer[i] = [x, y]，表示 person x 肯定比 person y 更有钱。注意 richer 可能只是有效观察的子集。

另外，quiet[x] = q 表示 person x 的安静程度为 q。

现在返回 answer，其中 answer[x] = y，表示在所有肯定比 person x 更有钱或同样有钱的人中（即所有能从 x 通过 richer 关系直接或间接到达的人，包括 x 自己），y 是最安静的人（即 quiet[y] 的值最小）。

"""

from typing import List, Optional


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)

        # Build adjacency list: graph[x] = list of people who are directly richer than x
        # We traverse from richer -> poorer, so edge direction: richer -> poorer
        graph = [[] for _ in range(n)]
        for x, y in richer:
            graph[x].append(y)

        # answer[i] = the least quiet person among all people >= to person i
        ans = [-1] * n

        def dfs(person: int) -> int:
            # Return the least quiet person in the subtree rooted at person
            if ans[person] != -1:
                return ans[person]
            # Initialize with self
            min_person = person
            for poorer in graph[person]:
                candidate = dfs(poorer)
                if quiet[candidate] < quiet[min_person]:
                    min_person = candidate
            ans[person] = min_person
            return min_person

        for i in range(n):
            dfs(i)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题是一个有向无环图(DAG)的DFS/记忆化搜索问题。
# richer 关系构成有向图：如果 x 比 y 有钱，则有一条从 x 到 y 的边。
# 我们需要对每个人，找到所有能到达的人中 quiet 值最小的那个人。
# 由于 richer 关系是有传递性的（如果 a 比 b 有钱，b 比 c 有钱，则 a 比 c 有钱），
# 等价于在有向图中从当前节点出发，能到达的所有节点的 quiet 最小值。
# 使用 DFS + 记忆化：对每个人递归地找到其"更穷的"人中 quiet 最小的，然后与自身比较。
# ans[i] 记忆化存储结果，避免重复计算。
#
# 时间复杂度: O(N + E) 其中 N 是人数，E 是 richer 关系数
# 空间复杂度: O(N + E) 邻接表存储图 + 递归栈 + 答案数组
#
# 关键点:
# - DAG 的传递闭包问题，等价于图的可达性分析
# - DFS + 记忆化(ans 数组)避免指数级重复计算
# - 注意 richer 关系的方向：x 比 y 有钱，我们需要找所有比当前人更有钱或同等的人中 quiet 最小的
# - 图的方向设为富 -> 穷，DFS 从富向穷遍历
