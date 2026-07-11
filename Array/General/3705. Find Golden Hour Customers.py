"""
LeetCode #3705 - Find Golden Hour Customers
寻找黄金时段客户
https://leetcode.cn/problems/find-golden-hour-customers/

表：`restaurant_orders`
+------------------+----------+ | Column Name      | Type     |  +------------------+----------+ | order_id         | int      | | customer_id      | int      | | order_timestamp  | datetime | | order_amount     | decimal  | | payment_method   | varchar  | | order_rating     | int      | +------------------+----------+ order_id 是这张表的唯一主键。 payment_method 可以是 cash，card 或 app。 order_rating 在 1 到 5 之间，其中 5 是最佳（如果没有评分则是 NULL）。 order_timestamp 同时包含日期和时间信息。
编写一个解决方案来寻找 黄金时间客户 - 高峰时段持续订购且满意度高的客户。客户若满足以下所有条件，则被视为 黄金时段客户：
进行 至少 `3` 笔订单。
他们有 至少 `60%` 的订单在 高峰时间 中（`11:00`-`14:00` 或 `18:00`-`21:00`）。
他们的 平均评分 至少为 `4.0`，四舍五入到小数点后 `2` 位。
已评价至少 `50%` 的订单。
返回结果表按 `average_rating` 降序 排序，然后按 `customer_id` 降序 排序。
结果格式如下所示。

示例：

输入：
restaurant_orders 表：
+----------+-------------+---------------------+--------------+----------------+--------------+ | order_id | customer_id | order_timestamp     | order_amount | payment_method | order_rating | +----------+-------------+---------------------+--------------+----------------+--------------+ | 1        | 101         | 2024-03-01 12:30:00 | 25.50        | card           | 5            | | 2        | 101         | 2024-03-02 19:15:00 | 32.00        | app            | 4            | | 3        | 101         | 2024-03-03 13:45:00 | 28.75        | card           | 5            | | 4        | 101         | 2024-03-04 20:30:00 | 41.00        | app            | NULL         | | 5        | 102         | 2024-03-01 11:30:00 | 18.50        | cash           | 4            | | 6        | 102         | 2024-03-02 12:00:00 | 22.00        | card           | 3            | | 7        | 102         | 2024-03-03 15:30:00 | 19.75        | cash           | NULL         | | 8        | 103         | 2024-03-01 19:00:00 | 55.00        | app            | 5            | | 9        | 103         | 2024-03-02 20:45:00 | 48.50        | app            | 4            | | 10       | 103         | 2024-03-03 18:30:00 | 62.00        | card           | 5            | | 11       | 104         | 2024-03-01 10:00:00 | 15.00        | cash           | 3            | | 12       | 104         | 2024-03-02 09:30:00 | 18.00        | cash           | 2            | | 13       | 104         | 2024-03-03 16:00:00 | 20.00        | card           | 3            | | 14       | 105         | 2024-03-01 12:15:00 | 30.00        | app            | 4            | | 15       | 105         | 2024-03-02 13:00:00 | 35.50        | app            | 5            | | 16       | 105         | 2024-03-03 11:45:00 | 28.00        | card           | 4            | +----------+-------------+---------------------+--------------+----------------+--------------+
输出：
+-------------+--------------+----------------------+----------------+ | customer_id | total_orders | peak_hour_percentage | average_rating | +-------------+--------------+----------------------+----------------+ | 103         | 3            | 100                  | 4.67           | | 101         | 4            | 100                  | 4.67           | | 105         | 3            | 100                  | 4.33           | +-------------+--------------+----------------------+----------------+
解释：
客户 101：
总订单数：4（至少 3 笔）
高峰时间订单：4 笔中有 4 笔（12:30，19:15，13:45 和 20:30 在高峰时间）
高峰时间占比：100%（至少 60%）
已评分的订单：4 笔中有 3 笔（75% 评分完成率）
平均评分：(5+4+5)/3 = 4.67（至少 4.0）
结果：黄金时段客户
客户 102:
总订单数：3（至少 3 笔）
高峰时间订单：3 笔中有 2 笔（11:30，12:00 都在高峰时间，但 15:30 不是）
高峰时间占比：2/3 = 66.67%（至少 60%）
已评分的订单：3 笔中有 2 笔（66.67% 评分完成率）
平均评分：(4+3)/2 = 3.5（少于 4.0）
结果：不是黄金时段客户（平均评分太低）
客户 103:
总订单数：3（至少 3 笔）
高峰时间订单：3 笔中有 3 （19:00，20:45，18:30 都在傍晚高峰时间）
高峰时间占比：3/3 = 100%（至少 60%）
已评分的订单：3 笔中有 3 笔（100% 评分完成率）
平均评分：(5+4+5)/3 = 4.67（至少 4.0）
结果：黄金时段客户
客户 104:
总订单数：3（至少 3 笔）
高峰时间订单：3 笔中有 0 笔（10:00，09:30，16:00 都不在高峰时间）
高峰时间占比：0/3 = 0%（至少 60%）
结果：不是黄金时段客户（高峰时段订单不足）
客户 105:
总订单数：3（至少 3 笔）
高峰时间订单：3 笔中有 3 笔（12:15，13:00，11:45 都在中午高峰时间）
高峰时间占比：3/3 = 100%（至少 60%）
已评分的订单：3 笔中有 3 笔（100% 评分完成率）
平均评分：(4+5+4)/3 = 4.33（至少 4.0）
结果：黄金时段客户
结果表按 average_rating 降序排序，然后按 customer_id 降序排序。
"""

from typing import List, Optional


class Solution:
    def find_golden_hour_customers(self, restaurant_orders: 'pd.DataFrame') -> 'pd.DataFrame':
        import pandas as pd
        df = restaurant_orders.copy()
        df['hour'] = pd.to_datetime(df['order_timestamp']).dt.hour
        df['is_peak'] = df['hour'].apply(
            lambda h: 1 if (11 <= h <= 14 or 18 <= h <= 21) else 0
        )
        df['is_rated'] = df['order_rating'].notna().astype(int)

        grouped = df.groupby('customer_id').agg(
            total_orders=('order_id', 'count'),
            peak_orders=('is_peak', 'sum'),
            rated_orders=('is_rated', 'sum'),
            avg_rating=('order_rating', 'mean')
        ).reset_index()

        grouped = grouped[grouped['total_orders'] >= 3]
        grouped['peak_pct'] = grouped['peak_orders'] / grouped['total_orders'] * 100
        grouped = grouped[grouped['peak_pct'] >= 60]
        grouped['rated_pct'] = grouped['rated_orders'] / grouped['total_orders'] * 100
        grouped = grouped[grouped['rated_pct'] >= 50]
        grouped = grouped[grouped['avg_rating'] >= 4.0]

        grouped['average_rating'] = grouped['avg_rating'].round(2)
        grouped['peak_hour_percentage'] = grouped['peak_pct'].round(2)

        result = grouped[['customer_id', 'total_orders', 'peak_hour_percentage', 'average_rating']]
        result = result.sort_values(
            ['average_rating', 'customer_id'], ascending=[False, False]
        )
        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Pandas, Data Aggregation, Filtering
#
# 解题思路:
# 1. 解析订单时间戳，使用 pd.to_datetime 提取小时信息
# 2. 判断每笔订单是否在高峰时段（11:00-14:00 或 18:00-21:00），用 is_peak 标记
# 3. 判断每笔订单是否有评分（非 NULL），用 is_rated 标记
# 4. 按 customer_id 分组聚合，计算总订单数、高峰订单数、已评分订单数、平均评分
# 5. 依次应用四个过滤条件：
#    - 总订单数 >= 3
#    - 高峰时段占比 >= 60%
#    - 已评分占比 >= 50%
#    - 平均评分 >= 4.0
# 6. 计算输出列（average_rating、peak_hour_percentage 保留两位小数）
# 7. 按 average_rating 降序、customer_id 降序排序返回
#
# 时间复杂度: O(N) — 遍历所有订单一次进行分组聚合
# 空间复杂度: O(N) — 存储分组结果
#
# 关键点:
# - 使用 dt.hour 从时间戳提取小时，判断是否在 [11,14] 或 [18,21] 区间
# - notna() 判断评分是否非空，astype(int) 转为 0/1 方便求和
# - round(2) 保留两位小数
# - 排序条件：平均评分降序优先，客户ID降序其次
