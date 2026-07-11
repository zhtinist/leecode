"""
LeetCode #1418 - Display Table of Food Orders in a Restaurant
中文题名：点菜展示表
https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

Given the array `orders`, which represents the orders that customers
have done in a restaurant. More
specifically `orders[i]=[customerNamei,tableNumberi,foodItemi]`
where `customerNamei` is the name of the customer, `tableNumberi` is
the table customer sit at, and `foodItemi` is the item
customer orders.

Return the restaurant's “display table”. The “display
table” is a table whose row entries denote how many of each food item each
table ordered. The first column is the table number and the remaining columns
correspond to each food item in alphabetical order. The first row should be a header
whose first column is “Table”, followed by the names of the food items. Note that
the customer names are not part of the table. Additionally, the rows should be
sorted in numerically increasing order.

Example 1:

Input: orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]
Explanation:
The displaying table looks like:
Table,Beef Burrito,Ceviche,Fried Chicken,Water
3    ,0           ,2      ,1            ,0
5    ,0           ,1      ,0            ,1
10   ,1           ,0      ,0            ,0
For the table 3: David orders "Ceviche" and "Fried Chicken", and Rous orders "Ceviche".
For the table 5: Carla orders "Water" and "Ceviche".
For the table 10: Corina orders "Beef Burrito".

Example 2:

Input: orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
Output: [["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]]
Explanation:
For the table 1: Adam and Brianna order "Canadian Waffles".
For the table 12: James, Ratesh and Amadeus order "Fried Chicken".

Example 3:

Input: orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
Output: [["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]

Constraints:

`1 <= orders.length <= 5 * 10^4`

`orders[i].length == 3`

`1 <= customerNamei.length, foodItemi.length <=
20`

`customerNamei` and `foodItemi`
consist of lowercase and uppercase English letters and the space character.

`tableNumberi `is a valid integer between
`1` and `500`.

【中文翻译】

给定数组 `orders`，表示顾客在餐厅的订单。具体来说，`orders[i] = [customerNamei, tableNumberi, foodItemi]`，其中 `customerNamei` 是顾客姓名，`tableNumberi` 是顾客所在的桌号，`foodItemi` 是顾客点的菜品。

返回餐厅的「点菜展示表」。展示表的每一行记录每桌点的每种菜品的数量。第一列是桌号，其余各列按字母顺序对应每种菜品。第一行应为表头，第一列为 "Table"，后面是各菜品名称。注意顾客姓名不在展示表中。此外，行应按桌号数值递增顺序排列。

示例 1：
输入：orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
输出：[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]
解释：
展示表如下所示：
Table,Beef Burrito,Ceviche,Fried Chicken,Water
3    ,0           ,2      ,1            ,0
5    ,0           ,1      ,0            ,1
10   ,1           ,0      ,0            ,0
对于桌 3：David 点了 "Ceviche" 和 "Fried Chicken"，Rous 点了 "Ceviche"。
对于桌 5：Carla 点了 "Water" 和 "Ceviche"。
对于桌 10：Corina 点了 "Beef Burrito"。

示例 2：
输入：orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
输出：[["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]]
解释：
对于桌 1：Adam 和 Brianna 点了 "Canadian Waffles"。
对于桌 12：James、Ratesh 和 Amadeus 点了 "Fried Chicken"。

示例 3：
输入：orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
输出：[["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]

约束条件：
`1 <= orders.length <= 5 * 10^4`
`orders[i].length == 3`
`1 <= customerNamei.length, foodItemi.length <= 20`
`customerNamei` 和 `foodItemi` 包含大小写英文字母和空格字符。
`tableNumberi` 是一个介于 `1` 到 `500` 之间的有效整数。

"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # 收集所有食物种类（去重排序）
        food_items = sorted(set(order[2] for order in orders))

        # 建立桌号到食物计数的映射
        table_orders = defaultdict(lambda: defaultdict(int))
        for _, table, food in orders:
            table_orders[int(table)][food] += 1

        # 构建结果矩阵
        result = []
        # 表头
        header = ["Table"] + food_items
        result.append(header)

        # 按桌号排序
        for table_num in sorted(table_orders.keys()):
            row = [str(table_num)]
            for food in food_items:
                row.append(str(table_orders[table_num][food]))
            result.append(row)

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 哈希表 + 排序法：
# 1. 遍历所有订单，收集所有出现的食物名称，去重并按字典序排序，得到食物的有序列表。
# 2. 使用嵌套字典（defaultdict）记录每桌各种食物的数量：
#    table_orders[桌号][食物] = 数量。
#    注意将桌号转为整数以便排序。
# 3. 构建结果矩阵：
#    a. 第一行为表头：["Table"] + 食物列表。
#    b. 按桌号升序排序，对每个桌号生成一行：
#       第一列为桌号（字符串），后续每列为该桌对应食物的数量。
# 4. 所有数据统一转为字符串返回。
#
# 时间复杂度: O(N + T * F)，其中 N 是订单数量，T 是不同桌号的数量，
#             F 是不同食物种类的数量。排序食物 O(F log F)，排序桌号 O(T log T)。
#             总体 O(N + F log F + T log T + T * F)，其中 T <= 500，F <= N。
# 空间复杂度: O(N + T * F)，用于存储桌号到食物计数的映射。
#
# 关键点:
# - 使用 set 收集所有食物种类并排序
# - 使用嵌套字典 defaultdict(int) 方便统计
# - 桌号需转为整数以正确排序（字符串排序 "10" < "2"）










