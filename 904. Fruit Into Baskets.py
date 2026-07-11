"""
LeetCode #904 - Fruit Into Baskets
中文题名：水果成篮
https://leetcode.com/problems/fruit-into-baskets/

In a row of trees, the `i`-th tree produces fruit with type `tree[i]`.

You start at any tree of your choice, then repeatedly perform the
following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.

Move to the next tree to the right of the current tree.  If there is no tree to the
right, stop.

Note that you do not have any choice after the initial choice of starting tree: you must
perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each
basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].

Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].

Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].

Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.

【中文翻译】
在一排树中，第 `i` 棵树产生类型为 `tree[i]` 的水果。

你可以从任意一棵树开始，然后重复执行以下步骤：

将树上的一颗水果放入你的篮子中。如果不能放入，就停下。

移动到当前树右侧的下一棵树。如果右边没有树，就停下。

请注意，选择初始树后，你就没有任何选择了：你必须执行步骤 1，然后步骤 2，然后回到步骤 1，依此类推，直到停下。

你有两个篮子，每个篮子可以装任意数量的水果，但你希望每个篮子只装一种类型的水果。

按照此过程，你最多能收集多少水果？

示例 1：

输入：[1,2,1]
输出：3
解释：我们可以收集 [1,2,1]。

示例 2：

输入：[0,1,2,2]
输出：3
解释：我们可以收集 [1,2,2]。
如果从第一棵树开始，我们只能收集 [0,1]。

示例 3：

输入：[1,2,3,2,2]
输出：4
解释：我们可以收集 [2,3,2,2]。
如果从第一棵树开始，我们只能收集 [1,2]。

示例 4：

输入：[3,3,3,1,2,1,1,2,3,3,4]
输出：5
解释：我们可以收集 [1,2,1,1,2]。
如果从第一棵树或第八棵树开始，我们只能收集 4 个水果。

"""

from typing import List, Optional


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}          # 水果类型 -> 该类型在窗口中的最后出现位置
        left = 0
        max_fruits = 0

        for right, fruit in enumerate(fruits):
            basket[fruit] = right

            # 超过 2 种水果，收缩左边界
            if len(basket) > 2:
                # 找到最左出现位置的水果类型并删除
                min_type = min(basket, key=basket.get)
                left = basket.pop(min_type) + 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 滑动窗口（Sliding Window）+ 哈希表。本质上等价于"最多包含两个不同字符的最长子串"。
# 窗口内只允许最多 2 种水果类型：
# 1. right 指针每次右移，将当前水果加入 basket（记录最后出现位置）
# 2. 如果 basket 中的水果类型超过 2 种，需要收缩 left：
#    - 找到最左出现位置的水果类型，将其移除
#    - left 移动到该类型最后出现位置 + 1
# 3. 更新 max_fruits = right - left + 1
#
# 另一种写法：维护每种水果的计数，当超过 2 种时 while 收缩 left 直到种类恢复为 2。
#
# 时间复杂度: O(N) — 每个元素最多被访问两次（right 一次，left 一次）
# 空间复杂度: O(1) — basket 最多存 3 种水果的条目
#
# 关键点:
# - 问题转化：篮子只能装 2 种水果 → 滑动窗口最多 2 个不同值
# - 收缩策略：记录最后出现位置，从而一次性跳到正确位置（而非逐步收缩）
# - 也可以使用 collections.Counter 实现逐步收缩的版本
