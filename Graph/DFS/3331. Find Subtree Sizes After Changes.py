"""
LeetCode #3331 - Find Subtree Sizes After Changes
修改后子树的大小
https://leetcode.cn/problems/find-subtree-sizes-after-changes/

给你一棵 `n` 个节点且根节点为编号 0 的树，节点编号为 `0` 到 `n - 1` 。这棵树用一个长度为 `n` 的数组 `parent` 表示，其中 `parent[i]` 是第 `i` 个节点的父亲节点的编号。由于节点 0 是根，`parent[0] == -1` 。
给你一个长度为 `n` 的字符串 `s` ，其中 `s[i]` 是节点 `i` 对应的字符。
对于节点编号从 `1` 到 `n - 1` 的每个节点 `x` ，我们 同时 执行以下操作 一次 ：
找到距离节点 `x` 最近 的祖先节点 `y` ，且 `s[x] == s[y]` 。
如果节点 `y` 不存在，那么不做任何修改。
否则，将节点 `x` 与它父亲节点之间的边 删除 ，在 `x` 与 `y` 之间连接一条边，使 `y` 变为 `x` 新的父节点。
请你返回一个长度为 `n` 的数组 `answer` ，其中 `answer[i]` 是 最终 树中，节点 `i` 为根的 子树 的 大小 。

示例 1：

输入：parent = [-1,0,0,1,1,1], s = "abaabc"
输出：[6,3,1,1,1,1]
解释：

节点 3 的父节点从节点 1 变为节点 0 。
示例 2：

输入：parent = [-1,0,4,0,1], s = "abbba"
输出：[5,2,1,1,1]
解释：

以下变化会同时发生：
节点 4 的父节点从节点 1 变为节点 0 。
节点 2 的父节点从节点 4 变为节点 1 。

提示：
`n == parent.length == s.length`
`1 <= n <= 10^5`
对于所有的 `i >= 1` ，都有 `0 <= parent[i] <= n - 1` 。
`parent[0] == -1`
`parent` 表示一棵合法的树。
`s` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        stack = [[] for _ in range(26)]

        def dfs(u: int):
            c = ord(s[u]) - 97
            if stack[c]:
                new_parent[u] = stack[c][-1]
            stack[c].append(u)
            for v in children[u]:
                dfs(v)
            stack[c].pop()

        dfs(0)

        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [0] * n

        def dfs_size(u: int) -> int:
            total = 1
            for v in new_children[u]:
                total += dfs_size(v)
            ans[u] = total
            return total

        dfs_size(0)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Array, Hash Table, String
#
# 解题思路:
# 利用DFS和字符栈追踪每个节点最近的同字符祖先。对于每个字符'a'-'z'维护一个栈，
# 记录DFS路径上该字符的节点。访问节点时，若对应字符栈非空，则栈顶即为最近同字符祖先，
# 更新new_parent。DFS完成后，根据new_parent构建新树，再DFS计算每棵子树的大小。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 所有节点的重定向同时发生，因此在DFS时需要基于原始树找祖先
# - 使用字符分类的栈来O(1)找到最近同字符祖先
# - 最后在新树上做子树大小统计
