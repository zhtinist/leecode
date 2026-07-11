"""
LeetCode #1352 - Product of the Last K Numbers
中文题名：最后 K 个数的乘积
https://leetcode.com/problems/product-of-the-last-k-numbers/

Implement the class `ProductOfNumbers` that supports two methods:

1.` add(int num)`

Adds the number `num` to the back of the current list of numbers.

2.` getProduct(int k)`

Returns the product of the last `k` numbers in the current list.

You can assume that always the current list has at least `k`
numbers.

At any time, the product of any contiguous sequence of numbers will fit into a single
32-bit integer without overflowing.

Example:

Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[null,null,null,null,null,null,20,40,0,null,32]

Explanation
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32

Constraints:

There will be at most `40000` operations considering both `add`
and `getProduct`.

`0 <= num <= 100`

`1 <= k <= 40000`

【中文翻译】
实现 `ProductOfNumbers` 类，支持两种方法：

1. `add(int num)`：将数字 `num` 添加到当前数字列表的末尾。

2. `getProduct(int k)`：返回当前列表中最后 `k` 个数字的乘积。假设当前列表始终至少有 `k` 个数字。任意连续子序列的乘积始终在 32 位整数范围内。

示例：
输入
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

输出
[null,null,null,null,null,null,20,40,0,null,32]

解释
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // 返回 20。最后 2 个数字的乘积是 5 * 4 = 20
productOfNumbers.getProduct(3); // 返回 40。最后 3 个数字的乘积是 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // 返回 0。最后 4 个数字的乘积是 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // 返回 32。最后 2 个数字的乘积是 4 * 8 = 32
"""

from typing import List


class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-k - 1]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 维护前缀乘积列表 prefix，prefix[i] 表示从开头到第 i 个元素的乘积（prefix[0]=1）。
# add(num): 如果 num==0，清空列表重置为 [1]（因为任何包含 0 的乘积都为 0）；
# 否则将 prefix[-1] * num 追加到列表末尾。
# getProduct(k): 如果 k >= len(prefix)，说明最近 k 个数中包含 0，返回 0；
# 否则返回 prefix[-1] // prefix[-k-1]，即总乘积除以去掉最后 k 个后的乘积。
#
# 时间复杂度: 每次操作 O(1)
# 空间复杂度: O(N)，N 为 add 操作次数（不含清零重置）
#
# 关键点:
# - 前缀乘积数组快速计算连续乘积
# - 遇到 0 时重置前缀数组，用 k >= len(prefix) 判断是否包含 0
# - 利用整数除法从总乘积中剔除前缀部分













