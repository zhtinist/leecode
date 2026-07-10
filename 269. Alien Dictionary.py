"""
LeetCode #269 - Alien Dictionary
https://leetcode.com/problems/alien-dictionary/

There is a new alien language which uses the latin alphabet. However, the order among letters
are unknown to you. You receive a list of non-empty words from the dictionary, where
words are sorted lexicographically by the rules of this new language. Derive the
order of letters in this language.

Example 1:

Input:
[
"wrt",
"wrf",
"er",
"ett",
"rftt"
]

Output: `"wertf"`

Example 2:

Input:
[
"z",
"x"
]

Output: `"zx"`

Example 3:

Input:
[
"z",
"x",
"z"
]

Output: `""`

Explanation: The order is invalid, so return `""`.

Note:

You may assume all letters are in lowercase.

You may assume that if a is a prefix of b, then a must appear before b in the given
dictionary.

If the order is invalid, return an empty string.

There may be multiple valid order of letters, return any one of them is fine.
"""

from typing import List, Optional


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        from collections import defaultdict, deque

        # 构建图：邻接表和入度
        graph = defaultdict(set)
        indegree = {ch: 0 for word in words for ch in word}

        # 比较相邻单词找字符顺序关系
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            # 特殊情况：如果 w1 是 w2 的前缀且 w1 更长，非法
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            min_len = min(len(w1), len(w2))
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break  # 只取第一个不同字符

        # 拓扑排序（BFS Kahn 算法）
        queue = deque([ch for ch in indegree if indegree[ch] == 0])
        result = []

        while queue:
            ch = queue.popleft()
            result.append(ch)
            for neighbor in graph[ch]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # 如果结果长度不为字符集大小，说明存在环
        if len(result) != len(indegree):
            return ""

        return ''.join(result)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: Yes
#
# 解题思路：
# 拓扑排序（Kahn BFS 算法）。将字母看作图中的节点，相邻单词的第一个不同字符
# 给出字符间的先后顺序（有向边）。构建有向图和入度表后，使用 BFS 进行拓扑排序：
# 将所有入度为 0 的节点入队，依次出队加入结果，并将其邻接节点的入度减 1，
# 当入度为 0 时入队。最终若结果长度小于字符集大小，说明有环，返回空串。
# 特殊情况：如果 w1 是 w2 的前缀且 w1 更长（如 "abc" 在 "ab" 之前），非法。
#
# 时间复杂度: O(C) — C 为所有单词的总字符数
# 空间复杂度: O(1) — 字母只 26 个，图大小有界
#
# 关键点：
# - 相邻单词比较找到字符顺序
# - 拓扑排序检测环
# - 处理前缀非法情况
# - 结果可为任意合法拓扑序
