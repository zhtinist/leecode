"""
LeetCode #638 - Shopping Offers
中文题名：大礼包
https://leetcode.com/problems/shopping-offers/

In LeetCode Store, there are some kinds of items to sell. Each item has a price.

However, there are some special offers, and a special offer consists of one or more
different kinds of items with a sale price.

You are given the each item's price, a set of special offers, and the number we need to buy
for each item.
The job is to output the lowest price you have to pay for exactly certain items as
given, where you could make optimal use of the special offers.

Each special offer is represented in the form of an array, the last number represents the
price you need to pay for this special offer, other numbers represents how many specific
items you could get if you buy this offer.

You could use any of special offers as many times as you want.

Example 1:

Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation:
There are two kinds of items, A and B. Their prices are $2 and $5 respectively.
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B.
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.

Example 2:

Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
Output: 11
Explanation:
The price of A is $2, and $3 for B, $4 for C.
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C.
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C.
You cannot add more items, though only $9 for 2A ,2B and 1C.

Note:

There are at most 6 kinds of items, 100 special offers.

For each item, you need to buy at most 6 of them.

You are not allowed to buy more items than you want, even if that would lower the
overall price.

【中文翻译】
在 LeetCode 商店中，有一些商品在出售。每件商品都有一个价格。

然而，也有一些大礼包，每个大礼包包含一种或多种不同的商品，并有一个优惠价格。

给定每件商品的单价、一组大礼包以及每件商品需要购买的数量。
你的任务是输出恰好购买指定数量的商品所需支付的最低价格，
你可以以最佳方式使用大礼包。

每个大礼包以数组形式表示，最后一个数字表示购买这个大礼包需要支付的价格，
其他数字表示购买这个大礼包可以获得的各商品数量。

你可以使用任意大礼包任意次。

示例 1：

输入：[2,5], [[3,0,5],[1,2,10]], [3,2]
输出：14
解释：
有两种商品 A 和 B。单价分别为 2 和 5 美元。
大礼包 1：支付 5 美元获得 3 个 A 和 0 个 B。
大礼包 2：支付 10 美元获得 1 个 A 和 2 个 B。
你需要购买 3 个 A 和 2 个 B，所以你可以支付 10 美元获得 1 个 A 和 2 个 B（大礼包 #2），再支付 4 美元购买 2 个 A。

示例 2：

输入：[2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
输出：11
解释：
商品 A 的价格为 2 美元，B 的价格为 3 美元，C 的价格为 4 美元。
你可以支付 4 美元获得 1 个 A 和 1 个 B，支付 9 美元获得 2 个 A、2 个 B 和 1 个 C。
你需要购买 1 个 A、2 个 B 和 1 个 C，所以你可以支付 4 美元获得 1 个 A 和 1 个 B（大礼包 #1），再支付 3 美元买 1 个 B，4 美元买 1 个 C。
你不能添加更多商品，即使只需 9 美元获得 2A、2B 和 1C。

注意：

商品种类最多 6 种，大礼包最多 100 种。

每种商品你最多需要购买 6 个。

你不能购买超过需要数量的商品，即使这能降低总价。
"""

from functools import lru_cache


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)

        # Filter out special offers that cost more than buying items individually
        valid_specials = []
        for offer in special:
            individual_cost = sum(offer[i] * price[i] for i in range(n))
            if individual_cost > offer[-1]:
                valid_specials.append(offer)

        @lru_cache(maxsize=None)
        def dfs(*needs_tuple: int) -> int:
            needs_list = list(needs_tuple)
            # Base cost：buy all remaining items at full price
            min_cost = sum(needs_list[i] * price[i] for i in range(n))

            # Try each valid special offer
            for offer in valid_specials:
                new_needs = []
                for i in range(n):
                    if needs_list[i] < offer[i]:
                        break  # Cannot use this offer (not enough need)
                    new_needs.append(needs_list[i] - offer[i])
                else:
                    # All items can be covered by this offer
                    min_cost = min(min_cost, offer[-1] + dfs(*new_needs))

            return min_cost

        return dfs(*needs)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 DFS + 记忆化搜索（或可说 DP）：
# 1. 首先过滤掉不划算的大礼包：如果大礼包的总价比单买还贵，直接排除。
# 2. 定义递归函数 dfs(*needs)，返回满足当前 needs 的最低花费。
# 3. 基础情况（base case）：不用任何大礼包，全部单买的价格。
# 4. 对于每个有效大礼包，检查是否可以使用（needs >= offer），
#    如果能用，更新 needs，递归计算加上礼包价格后的总价，取最小值。
# 5. 使用 @lru_cache 记忆化，避免重复计算相同的 needs 状态。
#
# 时间复杂度: O(S * (max_need + 1)^n) - S 为礼包数，n 为商品种类数（<= 6），
#            max_need <= 6，所以状态数最多 7^6 ≈ 117,649，在可接受范围内
# 空间复杂度: O((max_need + 1)^n) - 记忆化缓存
#
# 关键点:
# - 先过滤不划算的礼包，减少搜索空间
# - @lru_cache 对 tuple 参数进行记忆化
# - 每种商品最多买 6 个，最多 6 种商品 -> 状态空间有限
# - 不能购买超过需要的数量
