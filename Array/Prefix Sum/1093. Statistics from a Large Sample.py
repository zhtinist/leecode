"""
LeetCode #1093 - Statistics from a Large Sample
中文题名：大样本统计
https://leetcode.com/problems/statistics-from-a-large-sample/

We sampled integers between `0` and `255`, and stored the results in an
array `count`:  `count[k]` is the number of integers we sampled
equal to `k`.

Return the minimum, maximum, mean, median, and mode of the sample respectively, as an array
of floating point numbers.  The mode is guaranteed to be unique.

(Recall that the median of a sample is:

The middle element, if the elements of the sample were sorted and the number of
elements is odd;

The average of the middle two elements, if the elements of the sample were sorted
and the number of elements is even.)

Example 1:

Input: count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: [1.00000,3.00000,2.37500,2.50000,3.00000]

Example 2:

Input: count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: [1.00000,4.00000,2.18182,2.00000,1.00000]

Constraints:

`count.length == 256`

`1 <= sum(count) <= 10^9`

The mode of the sample that count represents is unique.

Answers within `10^-5` of the true value will be accepted as correct.

【中文翻译】
我们对 0 到 255 之间的整数进行采样，并将结果存储在数组 count 中：count[k] 就是值为 k 的整数的采样数量。

分别返回样本的最小值、最大值、平均值、中位数和众数，以浮点数数组的形式返回。题目保证众数是唯一的。

（回想一下，样本的中位数是：

如果样本的元素排序后，元素数量是奇数，则为中间的元素；

如果样本的元素排序后，元素数量是偶数，则为中间两个元素的平均值。）

示例 1：

输入：count = [0,1,3,4,0,0,...,0]（256 个元素）
输出：[1.00000,3.00000,2.37500,2.50000,3.00000]

示例 2：

输入：count = [0,4,3,2,2,0,0,...,0]（256 个元素）
输出：[1.00000,4.00000,2.18182,2.00000,1.00000]

约束条件：

count.length == 256
1 <= sum(count) <= 10^9
count 表示的样本的众数是唯一的。
与真实值误差在 10^-5 以内的答案都将被接受为正确答案。

"""

from typing import List, Optional


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum = next(i for i, c in enumerate(count) if c > 0)
        maximum = next(i for i in range(255, -1, -1) if count[i] > 0)

        total_count = sum(count)
        total_sum = sum(i * c for i, c in enumerate(count))

        mean = total_sum / total_count

        mode = max(range(256), key=lambda i: count[i])

        def get_median():
            mid1 = (total_count + 1) // 2
            mid2 = (total_count + 2) // 2
            cum = 0
            found1 = False
            median1 = median2 = 0

            for i in range(256):
                cum += count[i]
                if not found1 and cum >= mid1:
                    median1 = i
                    found1 = True
                if cum >= mid2:
                    median2 = i
                    break

            return (median1 + median2) / 2.0

        median = get_median()
        return [float(minimum), float(maximum), mean, median, float(mode)]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 直接根据 count 数组统计各项指标。
# 最小值：从 0 开始找第一个 count[i] > 0 的 i。
# 最大值：从 255 开始找第一个 count[i] > 0 的 i。
# 平均值：总和（i * count[i] 的和）除以总数（count[i] 的和）。
# 中位数：找到第 (total+1)//2 和第 (total+2)//2 个元素的位置。
#   - 奇数个：两者相同，取该位置的值。
#   - 偶数个：取两个位置值的平均值。
#   通过累计计数实现：cum += count[i]，当 cum >= 目标位置时记录。
# 众数：count[i] 最大的 i（题目保证唯一）。
#
# 时间复杂度: O(256) = O(1) - count 数组固定大小 256
# 空间复杂度: O(1) - 只使用常数额外空间
#
# 关键点:
# - count 数组大小固定为 256，所以 O(1) 复杂度
# - 中位数的位置公式：(total+1)//2 和 (total+2)//2 统一处理奇偶
# - 使用累计计数（前缀和）定位中位数
# - 使用 found1 布尔变量避免中位数 0 被误判
# - 答案误差在 10^-5 内即正确
