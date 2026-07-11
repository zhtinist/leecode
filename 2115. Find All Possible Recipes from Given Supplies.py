"""
LeetCode #2115 - Find All Possible Recipes from Given Supplies
从给定原材料中找到所有可以做出的菜
https://leetcode.cn/problems/find-all-possible-recipes-from-given-supplies/

你有 `n` 道不同菜的信息。给你一个字符串数组 `recipes` 和一个二维字符串数组 `ingredients` 。第 `i` 道菜的名字为 `recipes[i]` ，如果你有它 所有 的原材料 `ingredients[i]` ，那么你可以 做出 这道菜。一份食谱也可以是 其它 食谱的原料，也就是说 `ingredients[i]` 可能包含 `recipes` 中另一个字符串。
同时给你一个字符串数组 `supplies` ，它包含你初始时拥有的所有原材料，每一种原材料你都有无限多。
请你返回你可以做出的所有菜。你可以以 任意顺序 返回它们。
注意两道菜在它们的原材料中可能互相包含。

示例 1：
输入：recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"] 输出：["bread"] 解释： 我们可以做出 "bread" ，因为我们有原材料 "yeast" 和 "flour" 。
示例 2：
输入：recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"] 输出：["bread","sandwich"] 解释： 我们可以做出 "bread" ，因为我们有原材料 "yeast" 和 "flour" 。 我们可以做出 "sandwich" ，因为我们有原材料 "meat" 且可以做出原材料 "bread" 。
示例 3：
输入：recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"] 输出：["bread","sandwich","burger"] 解释： 我们可以做出 "bread" ，因为我们有原材料 "yeast" 和 "flour" 。 我们可以做出 "sandwich" ，因为我们有原材料 "meat" 且可以做出原材料 "bread" 。 我们可以做出 "burger" ，因为我们有原材料 "meat" 且可以做出原材料 "bread" 和 "sandwich" 。
示例 4：
输入：recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast"] 输出：[] 解释： 我们没法做出任何菜，因为我们只有原材料 "yeast" 。

提示：
`n == recipes.length == ingredients.length`
`1 <= n <= 100`
`1 <= ingredients[i].length, supplies.length <= 100`
`1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10`
`recipes[i], ingredients[i][j]` 和 `supplies[k]` 只包含小写英文字母。
所有 `recipes` 和 `supplies` 中的值互不相同。
`ingredients[i]` 中的字符串互不相同。
"""

from typing import List, Optional


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)
        indegree = {}
        graph = {}

        for i, recipe in enumerate(recipes):
            for ing in ingredients[i]:
                if ing not in available:
                    if ing not in graph:
                        graph[ing] = []
                    graph[ing].append(recipe)
                    indegree[recipe] = indegree.get(recipe, 0) + 1

        queue = [r for r in recipes if indegree.get(r, 0) == 0]
        result = []

        while queue:
            recipe = queue.pop(0)
            result.append(recipe)
            for nxt in graph.get(recipe, []):
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Graph, Topological Sort, Array, Hash Table, String
#
# 解题思路:
# 使用拓扑排序（Kahn算法）解决食谱之间的依赖关系。
# 首先将初始原材料 supplies 标记为"可用"。
# 对于每道菜，遍历其原材料列表：如果某个原材料不在初始可用集合中，
# 则建立一条从该原材料到菜的有向边（表示该菜依赖这个原材料），并增加菜的入度。
# 入度为0的菜表示所有原材料都已具备，可以立即制作，将其加入队列。
# BFS处理队列：每做出一道菜，将其加入结果并标记为可用，
# 然后更新依赖这道菜的其他菜的入度（入度减1后若为0则加入队列）。
#
# 时间复杂度: O(N*M)，其中N为菜的数量，M为平均原材料数量。N,M <= 100。
# 空间复杂度: O(N + S)，存储图和入度表，S为supplies数量。
#
# 关键点:
# - 反向建图：从原材料指向菜（原材料 -> 依赖它的菜），而不是菜 -> 原材料。
# - 初始可用的原材料和后续做出来的菜一视同仁，都可以解锁依赖它们的菜。
# - 拓扑排序处理循环依赖：如果存在环，环中的菜入度永远不会为0，不会被加入结果。
