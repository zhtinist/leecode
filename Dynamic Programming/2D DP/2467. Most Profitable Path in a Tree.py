"""
LeetCode #2467 - Most Profitable Path in a Tree
树上最大得分和路径
https://leetcode.cn/problems/most-profitable-path-in-a-tree/

一个 `n` 个节点的无向树，节点编号为 `0` 到 `n - 1` ，树的根结点是 `0` 号节点。给你一个长度为 `n - 1` 的二维整数数组 `edges` ，其中 `edges[i] = [a_i, b_i]` ，表示节点 `a_i` 和 `b_i` 在树中有一条边。
在每一个节点 `i` 处有一扇门。同时给你一个都是偶数的数组 `amount` ，其中 `amount[i]` 表示：
如果 `amount[i]` 的值是负数，那么它表示打开节点 `i` 处门扣除的分数。
如果 `amount[i]` 的值是正数，那么它表示打开节点 `i` 处门加上的分数。
游戏按照如下规则进行：
一开始，Alice 在节点 `0` 处，Bob 在节点 `bob` 处。
每一秒钟，Alice 和 Bob 分别 移动到相邻的节点。Alice 朝着某个 叶子结点 移动，Bob 朝着节点 `0` 移动。
对于他们之间路径上的 每一个 节点，Alice 和 Bob 要么打开门并扣分，要么打开门并加分。注意：
如果门 已经打开 （被另一个人打开），不会有额外加分也不会扣分。
如果 Alice 和 Bob 同时 到达一个节点，他们会共享这个节点的加分或者扣分。换言之，如果打开这扇门扣 `c` 分，那么 Alice 和 Bob 分别扣 `c / 2` 分。如果这扇门的加分为 `c` ，那么他们分别加 `c / 2` 分。
如果 Alice 到达了一个叶子结点，她会停止移动。类似的，如果 Bob 到达了节点 `0` ，他也会停止移动。注意这些事件互相 独立 ，不会影响另一方移动。
请你返回 Alice 朝最优叶子结点移动的 最大 净得分。

示例 1：

输入：edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6] 输出：6 解释： 上图展示了输入给出的一棵树。游戏进行如下： - Alice 一开始在节点 0 处，Bob 在节点 3 处。他们分别打开所在节点的门。   Alice 得分为 -2 。 - Alice 和 Bob 都移动到节点 1 。   因为他们同时到达这个节点，他们一起打开门并平分得分。   Alice 的得分变为 -2 + (4 / 2) = 0 。 - Alice 移动到节点 3 。因为 Bob 已经打开了这扇门，Alice 得分不变。   Bob 移动到节点 0 ，并停止移动。 - Alice 移动到节点 4 并打开这个节点的门，她得分变为 0 + 6 = 6 。 现在，Alice 和 Bob 都不能进行任何移动了，所以游戏结束。 Alice 无法得到更高分数。
示例 2：

输入：edges = [[0,1]], bob = 1, amount = [-7280,2350] 输出：-7280 解释： Alice 按照路径 0->1 移动，同时 Bob 按照路径 1->0 移动。 所以 Alice 只打开节点 0 处的门，她的得分为 -7280 。

提示：
`2 <= n <= 10^5`
`edges.length == n - 1`
`edges[i].length == 2`
`0 <= a_i, b_i < n`
`a_i != b_i`
`edges` 表示一棵有效的树。
`1 <= bob < n`
`amount.length == n`
`amount[i]` 是范围 `[-10^4, 10^4]` 之间的一个 偶数 。
"""

from typing import List, Optional


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)

        # 1. 构建邻接表
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 2. 计算 Bob 到达每个节点的时间
        # Bob 从 bob 节点出发走向 0，只有一条固定路径
        # 用 DFS 找到 bob 到 0 的路径，并记录时间
        bob_time = [float('inf')] * n

        def dfs_bob(node: int, parent: int, time: int) -> bool:
            """找到从 bob 到 0 的路径，沿途记录时间。返回 True 表示当前路径通向 0"""
            bob_time[node] = time
            if node == 0:
                return True
            for nxt in adj[node]:
                if nxt != parent:
                    if dfs_bob(nxt, node, time + 1):
                        return True
            # 如果当前分支不包含 0，撤销时间记录
            bob_time[node] = float('inf')
            return False

        dfs_bob(bob, -1, 0)

        # 3. Alice 的 DFS，从 0 出发走向叶子节点
        def dfs_alice(node: int, parent: int, time: int, cur_profit: int) -> int:
            """返回从当前节点出发，Alice 能获得的最大净收益"""
            # 根据 Alice 和 Bob 到达时间的比较，计算当前节点的收益
            if time < bob_time[node]:
                cur_profit += amount[node]
            elif time == bob_time[node]:
                cur_profit += amount[node] // 2
            # 如果 time > bob_time[node]：Bob 先到，门已开，Alice 得 0

            # 检查是否是叶子节点（排除根节点 0 且只有一个邻居时才是叶子）
            is_leaf = True
            max_child_profit = float('-inf')

            for nxt in adj[node]:
                if nxt != parent:
                    is_leaf = False
                    child_profit = dfs_alice(nxt, node, time + 1, cur_profit)
                    max_child_profit = max(max_child_profit, child_profit)

            if is_leaf:
                return cur_profit
            else:
                return max_child_profit

        return dfs_alice(0, -1, 0, 0)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Breadth-First Search, Graph, Array
#
# 解题思路:
# 分为三个步骤：
# 1. 构建树的邻接表
# 2. 计算 Bob 到达每个节点的时间：
#    - Bob 从节点 bob 出发，目标是节点 0，路径是唯一的
#    - 使用 DFS 从 bob 开始，沿途记录时间，找到通往 0 的路径
#    - 不在 Bob 路径上的节点时间设为无穷大
# 3. Alice 的 DFS 遍历：
#    - Alice 从节点 0 出发，朝叶子节点移动
#    - 在每个节点比较 Alice 到达时间和 Bob 到达时间：
#      * alice_time < bob_time: Alice 独享该节点的 amount
#      * alice_time == bob_time: 两人平分 amount（除以 2）
#      * alice_time > bob_time: Bob 已开门，Alice 得 0
#    - 递归计算所有子路径的最大收益，返回叶子节点的收益
#
# 时间复杂度: O(n)，两次 DFS 各遍历整棵树一次
# 空间复杂度: O(n)，邻接表、bob_time 数组和递归栈
#
# 关键点:
# - Bob 只有一条到 0 的路径，需要沿途标记时间；不在路径上的节点时间设为 inf
# - amount[i] 都是偶数，所以除以 2 不会产生小数问题
# - Alice 到达叶子节点时停止，但她可能在到达叶子前经过多个节点
# - 注意区分"root 只有一个邻居"和"叶子节点"的情况
