"""
LeetCode #1357 - Apply Discount Every n Orders
中文题名：每隔 n 个顾客打折
https://leetcode.com/problems/apply-discount-every-n-orders/

There is a sale in a supermarket, there will be a `discount` every
`n` customer.

There are some products in the supermarket where the id of the `i-th` product
is `products[i]` and the price per unit of this product is `prices[i]`.

The system will count the number of customers and when the `n-th` customer
arrive he/she will have a `discount` on the bill. (i.e if the cost is
`x` the new cost is `x - (discount * x) / 100`). Then the system
will start counting customers again.

The customer orders a certain amount of each product where `product[i]` is
the id of the `i-th` product the customer ordered and `amount[i]`
is the number of units the customer ordered of that product.

Implement the `Cashier` class:

`Cashier(int n, int discount, int[] products, int[] prices)`
Initializes the object with `n`, the `discount`, the
`products` and their `prices`.

`double getBill(int[] product, int[] amount)` returns the
value of the bill and apply the discount if needed. Answers within
`10^-5` of the actual value will be accepted as correct.

Example 1:

Input
["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill"]
[[3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,9,9,9,7]],[[2,3,5],[5,3,2]]]
Output
[null,500.0,4000.0,800.0,4000.0,4000.0,7350.0,2500.0]
Explanation
Cashier cashier = new Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]);
cashier.getBill([1,2],[1,2]);                        // return 500.0, bill = 1 * 100 + 2 * 200 = 500.
cashier.getBill([3,7],[10,10]);                      // return 4000.0
cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]);    // return 800.0, The bill was 1600.0 but as this is the third customer, he has a discount of 50% which means his bill is only 1600 - 1600 * (50 / 100) = 800.
cashier.getBill([4],[10]);                           // return 4000.0
cashier.getBill([7,3],[10,10]);                      // return 4000.0
cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]); // return 7350.0, Bill was 14700.0 but as the system counted three more customers, he will have a 50% discount and the bill becomes 7350.0
cashier.getBill([2,3,5],[5,3,2]);                    // return 2500.0

Constraints:

`1 <= n <= 10^4`

`0 <= discount <= 100`

`1 <= products.length <= 200`

`1 <= products[i] <= 200`

There are not repeated elements in the array
`products`.

`prices.length == products.length`

`1 <= prices[i] <= 1000`

`1 <= product.length <= products.length`

`product[i]` exists in `products`.

`amount.length == product.length`

`1 <= amount[i] <= 1000`

At most `1000` calls will be made to `getBill`.

Answers within `10^-5` of the actual value will be accepted
as correct.

【中文翻译】
超市正在进行促销活动，每隔 `n` 位顾客将获得 `discount` 折扣。

超市中有一些商品，第 `i` 个商品的 ID 为 `products[i]`，单价为 `prices[i]`。

系统会统计顾客数量，当第 `n` 位顾客到来时，他/她将获得账单折扣。（即如果原价为 `x`，新价格为 `x - (discount * x) / 100`）。然后系统重新开始计数。

每位顾客订购一定数量的每种商品，其中 `product[i]` 是顾客订购的第 `i` 个商品的 ID，`amount[i]` 是该商品的订购数量。

实现 `Cashier` 类：

`Cashier(int n, int discount, int[] products, int[] prices)`：用 `n`、`discount`、`products` 和 `prices` 初始化对象。

`double getBill(int[] product, int[] amount)`：返回账单金额，并根据需要打折。误差在 `10^-5` 以内即视为正确。

示例 1：
输入
["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill"]
[[3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,9,9,9,7]],[[2,3,5],[5,3,2]]]
输出
[null,500.0,4000.0,800.0,4000.0,4000.0,7350.0,2500.0]
解释
Cashier cashier = new Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]);
cashier.getBill([1,2],[1,2]);                        // 返回 500.0，账单 = 1 * 100 + 2 * 200 = 500
cashier.getBill([3,7],[10,10]);                      // 返回 4000.0
cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]);    // 返回 800.0，账单原本为 1600.0，但这是第三位顾客，享受 50% 折扣，实际支付 1600 - 1600 * (50 / 100) = 800
cashier.getBill([4],[10]);                           // 返回 4000.0
cashier.getBill([7,3],[10,10]);                      // 返回 4000.0
cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]); // 返回 7350.0，账单原本为 14700.0，但系统又计满三位顾客，享受 50% 折扣，实际支付 7350.0
cashier.getBill([2,3,5],[5,3,2]);                    // 返回 2500.0
"""

from typing import List


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.price_map = {p: price for p, price in zip(products, prices)}
        self.customer_count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1
        total = sum(self.price_map[p] * a for p, a in zip(product, amount))
        if self.customer_count % self.n == 0:
            total = total * (1 - self.discount / 100)
        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用哈希表存储商品 ID 到价格的映射，维护顾客计数器。
# 构造函数 Cashier: 构建 product_id -> price 的映射表，初始化顾客计数器为 0。
# getBill: 顾客计数加 1，遍历当前订单中所有产品，累加 product * amount 得到总账单。
# 如果该顾客是第 n 的倍数位（customer_count % n == 0），则应用折扣公式：total * (1 - discount / 100)。
#
# 时间复杂度: getBill O(P)，其中 P 为当前订单中的产品数量，构造函数 O(N)，N 为产品总数
# 空间复杂度: O(N)，存储价格映射表
#
# 关键点:
# - 哈希表快速查找商品价格
# - 计数器取模判断是否需要打折
# - 折扣公式：折后价 = 原价 * (1 - discount/100)













