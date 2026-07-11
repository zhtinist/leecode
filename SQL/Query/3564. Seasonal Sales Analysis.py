"""
LeetCode #3564 - Seasonal Sales Analysis
季节性销售分析
https://leetcode.cn/problems/seasonal-sales-analysis/

表：`sales`
+---------------+---------+ | Column Name   | Type    | +---------------+---------+ | sale_id       | int     | | product_id    | int     | | sale_date     | date    | | quantity      | int     | | price         | decimal | +---------------+---------+ sale_id 是这张表的唯一主键。 每一行包含一件产品的销售信息，包括 product_id，销售日期，销售数量，以及单价。
表：`products`
+---------------+---------+ | Column Name   | Type    | +---------------+---------+ | product_id    | int     | | product_name  | varchar | | category      | varchar | +---------------+---------+ product_id 是这张表的唯一主键。 每一行包含一件产品的信息，包括它的名字和分类。
编写一个解决方案来找到每个季节最受欢迎的产品分类。季节定义如下：
冬季：十二月，一月，二月
春季：三月，四月，五月
夏季：六月，七月，八月
秋季：九月，十月，十一月
一个 分类 的 受欢迎度 由某个 季节 的 总销售量 决定。如果有并列，选择总收入最高的类别 (`quantity × price`)。如果依然并列，返回字典序更小的分类。
返回结果表以季节 升序 排序。
结果格式如下所示。

示例：

输入：
sales 表：
+---------+------------+------------+----------+-------+ | sale_id | product_id | sale_date  | quantity | price | +---------+------------+------------+----------+-------+ | 1       | 1          | 2023-01-15 | 5        | 10.00 | | 2       | 2          | 2023-01-20 | 4        | 15.00 | | 3       | 3          | 2023-03-10 | 3        | 18.00 | | 4       | 4          | 2023-04-05 | 1        | 20.00 | | 5       | 1          | 2023-05-20 | 2        | 10.00 | | 6       | 2          | 2023-06-12 | 4        | 15.00 | | 7       | 5          | 2023-06-15 | 5        | 12.00 | | 8       | 3          | 2023-07-24 | 2        | 18.00 | | 9       | 4          | 2023-08-01 | 5        | 20.00 | | 10      | 5          | 2023-09-03 | 3        | 12.00 | | 11      | 1          | 2023-09-25 | 6        | 10.00 | | 12      | 2          | 2023-11-10 | 4        | 15.00 | | 13      | 3          | 2023-12-05 | 6        | 18.00 | | 14      | 4          | 2023-12-22 | 3        | 20.00 | | 15      | 5          | 2024-02-14 | 2        | 12.00 | +---------+------------+------------+----------+-------+
products 表：
+------------+-----------------+----------+ | product_id | product_name    | category | +------------+-----------------+----------+ | 1          | Warm Jacket     | Apparel  | | 2          | Designer Jeans  | Apparel  | | 3          | Cutting Board   | Kitchen  | | 4          | Smart Speaker   | Tech     | | 5          | Yoga Mat        | Fitness  | +------------+-----------------+----------+
输出：
+---------+----------+----------------+---------------+ | season  | category | total_quantity | total_revenue | +---------+----------+----------------+---------------+ | Fall    | Apparel  | 10             | 120.00        | | Spring  | Kitchen  | 3              | 54.00         | | Summer  | Tech     | 5              | 100.00        | | Winter  | Apparel  | 9              | 110.00        | +---------+----------+----------------+---------------+
解释：
秋季（九月，十月，十一月）：
服装：售出 10 件商品（在 9 月有 6 件夹克，在 11 月 有 4 条牛仔裤），收入 $120.00（6×$10.00 + 4×$15.00）
健身: 9 月售出 3 张瑜伽垫，收入 $36.00
最受欢迎：服装总数量最多（10）
春季（三月，四月，五月）：
厨房：5 月 售出 3 张菜板，收入 $54.00
科技：4 月 售出 1 台智能音箱，收入 $20.00
服装: 五月售出 2 件保暖夹克，收入 $20.00
最受欢迎：厨房总数量最多（3）且收入最多（$54.00）
夏季（六月，七月，八月）：
服装：六月售出 4 件名牌牛仔裤，收入 $60.00
健身：六月售出 5 张瑜伽垫，收入 $60.00
厨房：七月售出 2 张菜板，收入 $36.00
科技：八月售出 5 台智能音箱，收入 $100.00
最受欢迎：科技和健身都有 5 件商品，但科技收入更多（$100.00 vs $60.00）
冬季（十二月，一月，二月）：
服装：售出 9 件商品（一月有 5 件夹克和 4 条牛仔裤），收入 $110.00
厨房：十二月售出 6 张菜板，收入 $108.00
科技：十二月售出 3 台智能音箱，收入 $60.00
健身：二月售出 2 张瑜伽垫，收入 $24.00
最受欢迎：服装总数量最多（9）且收入最多（$110.00）
结果表以季节升序排序。
"""

from typing import List, Optional


class Solution:
    def seasonalSalesAnalysis(self, sales: 'pd.DataFrame', products: 'pd.DataFrame') -> 'pd.DataFrame':
        import pandas as pd

        # Step 1: Merge sales with products on product_id
        merged = sales.merge(products, on='product_id', how='inner')

        # Step 2: Extract month and map to season
        merged['month'] = pd.to_datetime(merged['sale_date']).dt.month

        def month_to_season(m):
            if m in (12, 1, 2):
                return 'Winter'
            elif m in (3, 4, 5):
                return 'Spring'
            elif m in (6, 7, 8):
                return 'Summer'
            else:
                return 'Fall'

        merged['season'] = merged['month'].apply(month_to_season)

        # Step 3: Calculate revenue for each row
        merged['revenue'] = merged['quantity'] * merged['price']

        # Step 4: Aggregate by season and category
        agg = merged.groupby(['season', 'category']).agg(
            total_quantity=('quantity', 'sum'),
            total_revenue=('revenue', 'sum')
        ).reset_index()

        # Step 5: Rank within each season by (total_quantity DESC, total_revenue DESC, category ASC)
        agg['rnk'] = agg.sort_values(
            ['total_quantity', 'total_revenue', 'category'],
            ascending=[False, False, True]
        ).groupby('season').cumcount()

        # Step 6: Keep only the top category per season
        result = agg[agg['rnk'] == 0][['season', 'category', 'total_quantity', 'total_revenue']]

        # Step 7: Sort season in alphabetical order
        season_order = {'Fall': 0, 'Spring': 1, 'Summer': 2, 'Winter': 3}
        result['season_sort'] = result['season'].map(season_order)
        result = result.sort_values('season_sort').drop(columns=['season_sort'])

        # Format revenue to 2 decimal places
        result['total_revenue'] = result['total_revenue'].round(2)

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: 数据库
#
# 解题思路:
# 使用 pandas 的数据处理能力模拟 SQL 分组聚合和排序逻辑：
# 1. 将 sales 表和 products 表按 product_id 进行内连接。
# 2. 从 sale_date 提取月份，按月份映射到四季（冬季12-2月，春季3-5月，夏季6-8月，秋季9-11月）。
# 3. 计算每行销售额 = quantity * price。
# 4. 按 (season, category) 分组，聚合计算总销售量和总收入。
# 5. 在每个季节内按 (total_quantity DESC, total_revenue DESC, category ASC) 排名，取第一名。
# 6. 按季节名称字母顺序排序输出（Fall < Spring < Summer < Winter）。
#
# 时间复杂度: O(N log N)，其中 N 为 sales 表行数。连接 O(N)，排序 O(N log N)。
# 空间复杂度: O(N)，存储连接后的中间结果和聚合结果。
#
# 关键点:
# - 月份到季节的映射：使用字典或函数将月份转换为季节名称。
# - 排名规则：先比总销量（多者胜），销量相同比总收入（多者胜），再相同比类别字母序（小者胜）。
# - 季节排序按英文字母升序（Fall, Spring, Summer, Winter）。
