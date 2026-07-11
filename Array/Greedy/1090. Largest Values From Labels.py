"""
LeetCode #1090 - Largest Values From Labels
中文题名：受标签影响的最大值
https://leetcode.com/problems/largest-values-from-labels/

We have a set of items: the `i`-th item has value `values[i]` and label
`labels[i]`.

Then, we choose a subset `S` of these items, such that:

`|S| <= num_wanted`

For every label `L`, the number of items in `S` with label
`L` is `<= use_limit`.

Return the largest possible sum of the subset `S`.

Example 1:

Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], `num_wanted `= 3, use_limit = 1
Output: 9
Explanation: The subset chosen is the first, third, and fifth item.

Example 2:

Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], `num_wanted `= 3, use_limit = 2
Output: 12
Explanation: The subset chosen is the first, second, and third item.

Example 3:

Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], `num_wanted `= 3, use_limit = 1
Output: 16
Explanation: The subset chosen is the first and fourth item.

Example 4:

Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], `num_wanted `= 3, use_limit = 2
Output: 24
Explanation: The subset chosen is the first, second, and fourth item.

Note:

`1 <= values.length == labels.length <= 20000`

`0 <= values[i], labels[i] <= 20000`

`1 <= num_wanted, use_limit <= values.length`

【中文翻译】
我们有一个项的集合，其中第 i 项的值为 values[i]，标签为 labels[i]。

我们从这些项中选出一个子集 S，满足：

|S| <= num_wanted
对于每个标签 L，子集 S 中标签为 L 的项的数目 <= use_limit。

返回子集 S 的最大可能和。

示例 1：

输入：values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
输出：9
解释：选出的子集是第一项，第三项和第五项。

示例 2：

输入：values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2
输出：12
解释：选出的子集是第一项，第二项和第三项。

示例 3：

输入：values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1
输出：16
解释：选出的子集是第一项和第四项。

示例 4：

输入：values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2
输出：24
解释：选出的子集是第一项，第二项和第四项。

注意：

1 <= values.length == labels.length <= 20000
0 <= values[i], labels[i] <= 20000
1 <= num_wanted, use_limit <= values.length

"""

from typing import List, Optional


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), reverse=True)

        label_count = {}
        total = 0
        picked = 0

        for val, label in items:
            if picked >= numWanted:
                break
            if label_count.get(label, 0) >= useLimit:
                continue
            total += val
            label_count[label] = label_count.get(label, 0) + 1
            picked += 1

        return total










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心算法。要使得子集总和最大，应优先选择值最大的项。
# 1. 将项按 values 降序排列。
# 2. 按顺序遍历排列后的项：
#    - 如果已选数量达到 num_wanted，停止。
#    - 如果当前项的标签已选数量达到 use_limit，跳过。
#    - 否则选择该项，累加值和标签计数。
# 3. 返回总和。
#
# 时间复杂度: O(n log n) - 排序耗时
# 空间复杂度: O(n) - 排序和字典空间
#
# 关键点:
# - 贪心：优先选择值最大的项
# - 用字典跟踪每个标签已选的数量
# - 跳过已达 use_limit 的标签对应的项
# - 最多选 num_wanted 个项
