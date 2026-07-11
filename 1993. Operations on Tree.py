"""
LeetCode #1993 - Operations on Tree
树上的操作
https://leetcode.cn/problems/operations-on-tree/

给你一棵 `n` 个节点的树，编号从 `0` 到 `n - 1` ，以父节点数组 `parent` 的形式给出，其中 `parent[i]` 是第 `i` 个节点的父节点。树的根节点为 `0` 号节点，所以 `parent[0] = -1` ，因为它没有父节点。你想要设计一个数据结构实现树里面对节点的加锁，解锁和升级操作。
数据结构需要支持如下函数：
Lock：指定用户给指定节点 上锁 ，上锁后其他用户将无法给同一节点上锁。只有当节点处于未上锁的状态下，才能进行上锁操作。
Unlock：指定用户给指定节点 解锁 ，只有当指定节点当前正被指定用户锁住时，才能执行该解锁操作。
Upgrade：指定用户给指定节点 上锁 ，并且将该节点的所有子孙节点 解锁 。只有如下 3 个条件 全部 满足时才能执行升级操作：
指定节点当前状态为未上锁。
指定节点至少有一个上锁状态的子孙节点（可以是 任意 用户上锁的）。
指定节点没有任何上锁的祖先节点。
请你实现 `LockingTree` 类：
`LockingTree(int[] parent)` 用父节点数组初始化数据结构。
`lock(int num, int user)` 如果 id 为 `user` 的用户可以给节点 `num` 上锁，那么返回 `true` ，否则返回 `false` 。如果可以执行此操作，节点 `num` 会被 id 为 `user` 的用户 上锁 。
`unlock(int num, int user)` 如果 id 为 `user` 的用户可以给节点 `num` 解锁，那么返回 `true` ，否则返回 `false` 。如果可以执行此操作，节点 `num` 变为 未上锁 状态。
`upgrade(int num, int user)` 如果 id 为 `user` 的用户可以给节点 `num` 升级，那么返回 `true` ，否则返回 `false` 。如果可以执行此操作，节点 `num` 会被 升级 。

示例 1：

输入： ["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"] [[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]] 输出： [null, true, false, true, true, true, false]  解释： LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]); lockingTree.lock(2, 2);    // 返回 true ，因为节点 2 未上锁。                            // 节点 2 被用户 2 上锁。 lockingTree.unlock(2, 3);  // 返回 false ，因为用户 3 无法解锁被用户 2 上锁的节点。 lockingTree.unlock(2, 2);  // 返回 true ，因为节点 2 之前被用户 2 上锁。                            // 节点 2 现在变为未上锁状态。 lockingTree.lock(4, 5);    // 返回 true ，因为节点 4 未上锁。                            // 节点 4 被用户 5 上锁。 lockingTree.upgrade(0, 1); // 返回 true ，因为节点 0 未上锁且至少有一个被上锁的子孙节点（节点 4）。                            // 节点 0 被用户 1 上锁，节点 4 变为未上锁。 lockingTree.lock(0, 1);    // 返回 false ，因为节点 0 已经被上锁了。

提示：
`n == parent.length`
`2 <= n <= 2000`
对于 `i != 0` ，满足 `0 <= parent[i] <= n - 1`
`parent[0] == -1`
`0 <= num <= n - 1`
`1 <= user <= 10^4`
`parent` 表示一棵合法的树。
`lock` ，`unlock` 和 `upgrade` 的调用 总共 不超过 `2000` 次。
"""

from typing import List, Optional


class LockingTree:
    def __init__(self, parent: List[int]):
        self.n = len(parent)
        self.parent = parent
        self.children = [[] for _ in range(self.n)]
        for i in range(1, self.n):
            self.children[parent[i]].append(i)
        self.locked = [0] * self.n  # 0 = unlocked, else = user id

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] == 0:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = 0
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        # Condition 1: node must be unlocked
        if self.locked[num] != 0:
            return False

        # Condition 2: at least one locked descendant
        if not self._has_locked_descendant(num):
            return False

        # Condition 3: no locked ancestor
        if self._has_locked_ancestor(num):
            return False

        # Perform upgrade: lock node, unlock all descendants
        self.locked[num] = user
        self._unlock_descendants(num)
        return True

    def _has_locked_descendant(self, node: int) -> bool:
        for child in self.children[node]:
            if self.locked[child] != 0:
                return True
            if self._has_locked_descendant(child):
                return True
        return False

    def _has_locked_ancestor(self, node: int) -> bool:
        while self.parent[node] != -1:
            node = self.parent[node]
            if self.locked[node] != 0:
                return True
        return False

    def _unlock_descendants(self, node: int) -> None:
        for child in self.children[node]:
            self.locked[child] = 0
            self._unlock_descendants(child)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Breadth-First Search, Design, Array, Hash Table
#
# 解题思路:
# 使用三个关键数据结构：parent 数组（找到祖先）、children 邻接表（遍历子孙）、
# locked 数组（记录每个节点的锁定用户，0 表示未锁定）。
# lock: 检查是否未锁定，是则锁定。
# unlock: 检查是否是同一用户锁定的，是则解锁。
# upgrade: 满足三个条件 — 节点未锁定、至少一个上锁的子孙节点、没有上锁的祖先节点。
# 父节点和子节点分别用向上遍历和 DFS 检查。
#
# 时间复杂度: lock/unlock O(1), upgrade O(N)（遍历祖先和子孙）
# 空间复杂度: O(N)
#
# 关键点:
# - 三个条件要全部满足
# - upgrade 时需要解锁所有子孙节点（递归）
# - 检查祖先时沿 parent 向上遍历
