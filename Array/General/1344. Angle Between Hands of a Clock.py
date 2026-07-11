"""
LeetCode #1344 - Angle Between Hands of a Clock
中文题名：时钟指针的夹角
https://leetcode.com/problems/angle-between-hands-of-a-clock/

Given two numbers, `hour` and `minutes`. Return the smaller
angle (in sexagesimal units) formed between the `hour` and the
`minute` hand.

Example 1:

Input: hour = 12, minutes = 30
Output: 165

Example 2:

Input: hour = 3, minutes = 30
Output: 75

Example 3:

Input: hour = 3, minutes = 15
Output: 7.5

Example 4:

Input: hour = 4, minutes = 50
Output: 155

Example 5:

Input: hour = 12, minutes = 0
Output: 0

Constraints:

`1 <= hour <= 12`

`0 <= minutes <= 59`

Answers within `10^-5` of the actual value will be accepted
as correct.

【中文翻译】
给定两个数字 `hour` 和 `minutes`。返回时针和分针之间形成的较小角度（以六十进制角度制表示）。

示例 1：

输入: hour = 12, minutes = 30
输出: 165
解释: 12:30 时，时针指向 12 和 1 之间的中间位置（165°），分针指向 6（180°），夹角为 165°。

示例 2：

输入: hour = 3, minutes = 30
输出: 75
解释: 3:30 时，时针在 3 和 4 之间（105°），分针指向 6（180°），夹角为 75°。

示例 3：

输入: hour = 3, minutes = 15
输出: 7.5
解释: 3:15 时，时针稍微超过 3 的位置（97.5°），分针指向 3（90°），夹角为 7.5°。

示例 4：

输入: hour = 4, minutes = 50
输出: 155

示例 5：

输入: hour = 12, minutes = 0
输出: 0
解释: 12:00 时两根指针重叠，夹角为 0°。

约束条件：

`1 <= hour <= 12`

`0 <= minutes <= 59`

答案与实际值的误差在 `10^-5` 以内即可被接受。
"""

from typing import List, Optional


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 时针每小时走 30°，每分钟再走 0.5°
        hour_angle = (hour % 12) * 30 + minutes * 0.5

        # 分针每分钟走 6°
        minute_angle = minutes * 6

        # 计算两针夹角
        diff = abs(hour_angle - minute_angle)

        # 取较小角（不超过 180°）
        return min(diff, 360 - diff)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 计算时针的角度位置：
#    - 12 小时对应一周 360°，每小时对应 30°。使用 (hour % 12) 处理 12 点钟的情况。
#    - 时针还会随分钟偏移：60 分钟时针走 30°，所以每分钟时针走 0.5°。
#    - 时针总角度 = (hour % 12) * 30 + minutes * 0.5
# 2. 计算分针的角度位置：
#    - 60 分钟对应一周 360°，每分钟对应 6°。
#    - 分针角度 = minutes * 6
# 3. 计算两角度之差的绝对值 diff = |hour_angle - minute_angle|。
# 4. 较小夹角 = min(diff, 360 - diff)，因为钟面上的角度不超过 180°。
#
# 时间复杂度: O(1) — 纯数学计算
# 空间复杂度: O(1) — 只使用常数个变量
#
# 关键点:
# - 时针不仅取决于小时，还受分钟影响（连续移动而非跳跃）
# - 处理 hour=12 时，hour % 12 = 0，即 12 点等价于 0 点位置
# - 取较小角的关键：min(diff, 360 - diff)
# - 所有计算使用浮点数，确保精度










