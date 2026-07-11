"""
LeetCode #433 - Minimum Genetic Mutation
中文题名：最小基因变化
https://leetcode.com/problems/minimum-genetic-mutation/

A gene string can be represented by an 8-character long string, with choices from `"A"`,
`"C"`, `"G"`, `"T"`.

Suppose we need to investigate about a mutation (mutation from "start" to "end"),
where ONE mutation is defined as ONE single character changed in the gene string.

For example, `"AACCGGTT"` -> `"AACCGGTA"` is 1
mutation.

Also, there is a given gene "bank", which records all the valid gene mutations. A
gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the minimum number
of mutations needed to mutate from "start" to "end". If there is no such
a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.

If multiple mutations are needed, all mutations during in the sequence must be valid.

You may assume start and end string is not the same.

Example 1:

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

return: 1

Example 2:

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

return: 2

Example 3:

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

return: 3

【中文翻译】
基因字符串由长度为 8 的字符串表示，字符从 "A"、"C"、"G"、"T" 中选择。
一次基因突变定义为基因字符串中一个字符的改变。例如 "AACCGGTT" -> "AACCGGTA" 是一次突变。

给定一个基因"银行"（bank），记录所有有效的基因突变。基因必须在 bank 中才是有效的。
给定 start、end 和 bank，确定从 start 突变到 end 所需的最少突变次数。
如果无法完成突变，返回 -1。

注意：
    起始基因假定有效，可能不在 bank 中。
    如果需多次突变，序列中所有突变都必须是有效的。
    假定 start 和 end 不相同。

示例 1：start="AACCGGTT", end="AACCGGTA", bank=["AACCGGTA"] → 返回 1
示例 2：start="AACCGGTT", end="AAACGGTA", bank=["AACCGGTA","AACCGCTA","AAACGGTA"] → 返回 2
示例 3：start="AAAAACCC", end="AACCCCCC", bank=["AAAACCCC","AAACCCCC","AACCCCCC"] → 返回 3
"""

from typing import List, Optional


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        from collections import deque
        genes = ["A", "C", "G", "T"]
        queue = deque([(startGene, 0)])
        visited = {startGene}

        while queue:
            gene, mutations = queue.popleft()

            if gene == endGene:
                return mutations

            for i in range(8):
                for g in genes:
                    if g != gene[i]:
                        mutated = gene[:i] + g + gene[i + 1:]
                        if mutated in bank_set and mutated not in visited:
                            visited.add(mutated)
                            queue.append((mutated, mutations + 1))

        return -1


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# BFS（广度优先搜索）求最短路径。将每个基因视为图中的一个节点，
# 如果两个基因相差一个字符（一次突变可达），则它们之间有边。
#
# 1. 将 bank 转为集合便于快速查找
# 2. 如果 endGene 不在 bank 中，直接返回 -1
# 3. 使用队列进行 BFS，每个状态包含（当前基因字符串，突变次数）
# 4. visited 集合避免重复访问
# 5. 对于当前基因的每个位置（共 8 个），尝试改为其他三个字符（A/C/G/T）
# 6. 如果新基因在 bank 中且未被访问过，加入队列
# 7. 找到 endGene 时返回当前步数
#
# 时间复杂度: O(B * 8 * 4) = O(B)，其中 B 是 bank 的大小。
#              最坏情况每个基因被访问一次，每条边来自 8×3 种可能的突变。
# 空间复杂度: O(B) — visited 集合和队列最多存储 bank 中的所有基因
#
# 关键点:
# - BFS 天然找到最短路径（最少突变次数）
# - 在图中，BFS 的边就是一次字符变化
# - 用 visited 集合防止重复访问导致无限循环
