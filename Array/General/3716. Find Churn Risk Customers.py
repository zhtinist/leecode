"""
LeetCode #3716 - Find Churn Risk Customers
寻找流失风险客户
https://leetcode.cn/problems/find-churn-risk-customers/

表：`subscription_events`
+------------------+---------+ | Column Name      | Type    |  +------------------+---------+ | event_id         | int     | | user_id          | int     | | event_date       | date    | | event_type       | varchar | | plan_name        | varchar | | monthly_amount   | decimal | +------------------+---------+ event_id 是这张表的唯一主键。 event_type 可以是 start，upgrade，downgrade 或 cancel。 plan_name 可以是 basic，standard，premium 或 NULL（当 event_type 是 cancel）。 monthly_amount 表示此次事件后的月度订阅费用。 对于 cancel 的事件，monthly_amount 为 0。
编写一个解决方案来 寻找流失风险用户 - 出现预流失信号的用户。如果用户符合以下所有条件，则被视为 有流失风险 的客户：
目前有 有效的订阅（他们的最后事件不是 cancel）。
已在其订阅历史中 至少进行过一次 降级。
他们 目前的订阅费用 低于历史最高订阅费用的 `50%`。
已订阅 至少 `60` 天。
返回结果表按 `days_as_subscriber` 降序 排序，然后按 `user_id` 升序 排序。
结果格式如下所示。

示例：

输入：
subscription_events 表：
+----------+---------+------------+------------+-----------+----------------+ | event_id | user_id | event_date | event_type | plan_name | monthly_amount | +----------+---------+------------+------------+-----------+----------------+ | 1        | 501     | 2024-01-01 | start      | premium   | 29.99          | | 2        | 501     | 2024-02-15 | downgrade  | standard  | 19.99          | | 3        | 501     | 2024-03-20 | downgrade  | basic     | 9.99           | | 4        | 502     | 2024-01-05 | start      | standard  | 19.99          | | 5        | 502     | 2024-02-10 | upgrade    | premium   | 29.99          | | 6        | 502     | 2024-03-15 | downgrade  | basic     | 9.99           | | 7        | 503     | 2024-01-10 | start      | basic     | 9.99           | | 8        | 503     | 2024-02-20 | upgrade    | standard  | 19.99          | | 9        | 503     | 2024-03-25 | upgrade    | premium   | 29.99          | | 10       | 504     | 2024-01-15 | start      | premium   | 29.99          | | 11       | 504     | 2024-03-01 | downgrade  | standard  | 19.99          | | 12       | 504     | 2024-03-30 | cancel     | NULL      | 0.00           | | 13       | 505     | 2024-02-01 | start      | basic     | 9.99           | | 14       | 505     | 2024-02-28 | upgrade    | standard  | 19.99          | | 15       | 506     | 2024-01-20 | start      | premium   | 29.99          | | 16       | 506     | 2024-03-10 | downgrade  | basic     | 9.99           | +----------+---------+------------+------------+-----------+----------------+
输出：
+----------+--------------+------------------------+-----------------------+--------------------+ | user_id  | current_plan | current_monthly_amount | max_historical_amount | days_as_subscriber | +----------+--------------+------------------------+-----------------------+--------------------+ | 501      | basic        | 9.99                   | 29.99                 | 79                 | | 502      | basic        | 9.99                   | 29.99                 | 69                 | +----------+--------------+------------------------+-----------------------+--------------------+
解释：
用户 501：
当前订阅有效：最近一次事件是降级到基础（未取消）
有降级记录：是，历史上有 2 次降级
当前订阅（9.99）vs 最大订阅（29.99）：9.99/29.99 = 33.3%（少于 50%）
订阅天数：1 月 1 日到 3 月 20 日 = 79 天（至少 60 天）
结果：流失风险客户
用户 502：
当前订阅有效：最近一次事件是降级到基础（未取消）
有降级记录：是，历史上有 1 次降级
当前订阅（9.99）vs 最大订阅（29.99）：9.99/29.99 = 33.3%（少于 50%）
订阅天数：1 月 5 日到 5 月 15 日 = 70 天（至少 60 天）
结果：流失风险客户
用户 503：
当前订阅有效：最近一次事件是升级到高级（未取消）
有降级记录：历史上没有降级
结果：无风险客户（没有降级历史）
用户 504：
当前订阅有效：最近一次事件是取消
结果：无风险客户（已取消订阅）
用户 505：
当前订阅有效：最近一次事件是升级到标准（未取消）
有降级记录：历史上没有降级
结果：无风险客户（没有降级历史）
用户 506：
当前订阅有效：最近一次事件是降级到标准（未取消）
有降级记录：是，历史上有 1 次降级
当前订阅（9.99）vs 最大订阅（29.99）：9.99/29.99 = 33.3%（少于 50%）
订阅天数：1 月 20 日到 5 月 10 日 = 50 天（少于 60 天）
结果：无风险客户（订阅时长不足）
结果表按 days_as_subscriber 降序排序，然后按 user_id 升序排序。
注意：days_as_subscriber 按照每个用户的第一个事件日期到最后一个事件日期进行计算。
"""

from typing import List, Optional


class Solution:
    def find_churn_risk_customers(self, subscription_events: 'pd.DataFrame') -> 'pd.DataFrame':
        import pandas as pd
        df = subscription_events.sort_values(['user_id', 'event_date'])

        grouped = df.groupby('user_id').agg(
            last_event_type=('event_type', 'last'),
            last_plan=('plan_name', 'last'),
            last_amount=('monthly_amount', 'last'),
            max_amount=('monthly_amount', 'max'),
            first_date=('event_date', 'min'),
            last_date=('event_date', 'max'),
            downgrade_count=('event_type', lambda x: (x == 'downgrade').sum())
        ).reset_index()

        # days as subscriber = difference in days between first and last event
        grouped['days_as_subscriber'] = (
            pd.to_datetime(grouped['last_date']) - pd.to_datetime(grouped['first_date'])
        ).dt.days

        # apply all four filter conditions
        result = grouped[
            (grouped['last_event_type'] != 'cancel') &
            (grouped['downgrade_count'] >= 1) &
            (grouped['last_amount'] < grouped['max_amount'] * 0.5) &
            (grouped['days_as_subscriber'] >= 60)
        ].copy()

        result['current_plan'] = result['last_plan']
        result['current_monthly_amount'] = result['last_amount']
        result['max_historical_amount'] = result['max_amount']

        output = result[['user_id', 'current_plan', 'current_monthly_amount',
                          'max_historical_amount', 'days_as_subscriber']]
        output = output.sort_values(
            ['days_as_subscriber', 'user_id'], ascending=[False, True]
        )
        return output










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Pandas, Data Aggregation, Filtering
#
# 解题思路:
# 1. 按 user_id 和 event_date 排序，确保事件按时间顺序排列
# 2. 按 user_id 分组，聚合以下信息：
#    - last_event_type: 最后一次事件类型（判断是否取消）
#    - last_plan/last_amount: 当前订阅方案和金额
#    - max_amount: 历史最高订阅金额
#    - first_date/last_date: 首次和末次事件日期（计算订阅天数）
#    - downgrade_count: 降级事件次数
# 3. 计算订阅天数 = (last_date - first_date).days
# 4. 应用四个过滤条件：
#    - 最后事件不是 cancel（当前订阅有效）
#    - 至少有一次 downgrade
#    - 当前金额 < 历史最高金额的 50%
#    - 订阅天数 >= 60
# 5. 重命名列并选择输出列
# 6. 按 days_as_subscriber 降序、user_id 升序排序
#
# 时间复杂度: O(N) — 一次分组聚合和过滤
# 空间复杂度: O(N) — 存储分组结果
#
# 关键点:
# - 使用 groupby().agg() 一次性计算多个聚合值
# - last/max 聚合函数直接获取最后一条记录和最大值
# - lambda 统计特定事件类型的出现次数
# - dt.days 从 timedelta 提取天数差值
# - 排序时注意 descending=[False, True] 对应先降序后升序
