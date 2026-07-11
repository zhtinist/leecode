"""
LeetCode #799 - Champagne Tower
中文题名：香槟塔
https://leetcode.com/problems/champagne-tower/

We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses,
and so on until the 100th row.  Each glass holds one cup (250ml) of champagne.

Then, some champagne is poured in the first glass at the top.  When the top most glass
is full, any excess liquid poured will fall equally to the glass immediately to the left and
right of it.  When those glasses become full, any excess champagne will fall equally to
the left and right of those glasses, and so on.  (A glass at the bottom row has it's
excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After
two cups of champagne are poured, the two glasses on the second row are half full.
After three cups of champagne are poured, those two cups become full - there are 3 full
glasses total now.  After four cups of champagne are poured, the third row has the
middle glass half full, and the two outside glasses are a quarter full, as pictured
below.

Now after pouring some non-negative integer cups of champagne, return how full the j-th glass
in the i-th row is (both i and j are 0 indexed.)

Example 1:
Input: poured = 1, query_glass = 1, query_row = 1
Output: 0.0
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

Example 2:
Input: poured = 2, query_glass = 1, query_row = 1
Output: 0.5
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.

Note:

`poured` will be in the range of `[0, 10 ^ 9]`.

`query_glass` and `query_row` will be in the range of `[0,
99]`.

【中文翻译】
我们将酒杯堆叠成金字塔形，第一行有 1 个杯子，第二行有 2 个杯子，依此类推直到第 100 行。每个杯子可以装一杯（250 毫升）香槟。

然后，将一些香槟倒入最顶部的第一个杯子中。当顶部杯子装满时，任何多余的液体会等量地流到它左下方和右下方的杯子中。当那些杯子装满后，多余的香槟会继续等量地流向它们的左下和右下，依此类推。（最底部一行的杯子多余的香槟会流到地上。）

例如，倒入一杯香槟后，顶部杯子是满的。倒入两杯后，第二行的两个杯子各半满。倒入三杯后，第二行的两个杯子变满——现在共有 3 个满杯。倒入四杯后，第三行中间的杯子半满，两边的杯子各四分之一满，如下图所示。

现在，在倒入非负整数杯香槟后，返回第 i 行第 j 个杯子的装满程度（i 和 j 都从 0 开始索引）。

示例 1：
输入：poured = 1, query_glass = 1, query_row = 1
输出：0.0
解释：我们向塔顶部的杯子（索引为 (0, 0)）倒入 1 杯香槟，没有多余的液体，所以顶层以下的所有杯子都为空。

示例 2：
输入：poured = 2, query_glass = 1, query_row = 1
输出：0.5
解释：我们向塔顶部的杯子（索引为 (0, 0)）倒入 2 杯香槟。有一杯多余的液体。索引为 (1, 0) 和 (1, 1) 的杯子将平分多余的液体，每个得到半杯香槟。

注意：
`poured` 的范围是 `[0, 10^9]`。
`query_glass` 和 `query_row` 的范围是 `[0, 99]`。
"""

from typing import List, Optional


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp[row] stores the amount of champagne in each glass of current row
        dp = [float(poured)]

        for row in range(query_row):
            # next_row will have row + 2 glasses
            next_row = [0.0] * (row + 2)
            for col in range(len(dp)):
                if dp[col] > 1:
                    overflow = (dp[col] - 1) / 2.0
                    next_row[col] += overflow
                    next_row[col + 1] += overflow
            dp = next_row

        return min(1.0, dp[query_glass]) if query_glass < len(dp) else 0.0



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用动态规划逐行模拟香槟的流动。
# 维护当前行每个杯子的香槟量数组 dp。
# 从第 0 行开始，dp = [poured]。
# 对于每一行（直到 query_row 的前一行），创建下一行的数组，
# 检查当前行每个杯子是否有溢出（量 > 1），
# 如果有溢出，将溢出量的一半分别加到下一行的左下方和右下方杯子。
# 处理完 query_row 行后，返回目标杯子的量（上限为 1.0）。
#
# 时间复杂度: O(R^2) - 其中 R = query_row <= 100，
#   每行遍历该行的杯子数量（1 + 2 + ... + R = O(R^2)）
# 空间复杂度: O(R) - 只存储当前行和下一行
#
# 关键点:
# - 逐行模拟，只保留当前行数据即可（空间优化）
# - 杯子容量为 1，超过 1 的部分才会溢出
# - 溢出量均分给下一行的两个相邻杯子
# - 返回值为 min(1.0, amount)，因为杯子最多装 1
