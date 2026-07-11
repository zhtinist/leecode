"""
LeetCode #2166 - Design Bitset
设计位集
https://leetcode.cn/problems/design-bitset/

位集 Bitset 是一种能以紧凑形式存储位的数据结构。
请你实现 `Bitset` 类。
`Bitset(int size)` 用 `size` 个位初始化 Bitset ，所有位都是 `0` 。
`void fix(int idx)` 将下标为 `idx` 的位上的值更新为 `1` 。如果值已经是 `1` ，则不会发生任何改变。
`void unfix(int idx)` 将下标为 `idx` 的位上的值更新为 `0` 。如果值已经是 `0` ，则不会发生任何改变。
`void flip()` 翻转 Bitset 中每一位上的值。换句话说，所有值为 `0` 的位将会变成 `1` ，反之亦然。
`boolean all()` 检查 Bitset 中 每一位 的值是否都是 `1` 。如果满足此条件，返回 `true` ；否则，返回 `false` 。
`boolean one()` 检查 Bitset 中 是否 至少一位 的值是 `1` 。如果满足此条件，返回 `true` ；否则，返回 `false` 。
`int count()` 返回 Bitset 中值为 1 的位的 总数 。
`String toString()` 返回 Bitset 的当前组成情况。注意，在结果字符串中，第 `i` 个下标处的字符应该与 Bitset 中的第 `i` 位一致。

示例：
输入 ["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"] [[5], [3], [1], [], [], [0], [], [], [0], [], []] 输出 [null, null, null, null, false, null, null, true, null, 2, "01010"]  解释 Bitset bs = new Bitset(5); // bitset = "00000". bs.fix(3);     // 将 idx = 3 处的值更新为 1 ，此时 bitset = "00010" 。 bs.fix(1);     // 将 idx = 1 处的值更新为 1 ，此时 bitset = "01010" 。 bs.flip();     // 翻转每一位上的值，此时 bitset = "10101" 。 bs.all();      // 返回 False ，bitset 中的值不全为 1 。 bs.unfix(0);   // 将 idx = 0 处的值更新为 0 ，此时 bitset = "00101" 。 bs.flip();     // 翻转每一位上的值，此时 bitset = "11010" 。 bs.one();      // 返回 True ，至少存在一位的值为 1 。 bs.unfix(0);   // 将 idx = 0 处的值更新为 0 ，此时 bitset = "01010" 。 bs.count();    // 返回 2 ，当前有 2 位的值为 1 。 bs.toString(); // 返回 "01010" ，即 bitset 的当前组成情况。

提示：
`1 <= size <= 10^5`
`0 <= idx <= size - 1`
至多调用 `fix`、`unfix`、`flip`、`all`、`one`、`count` 和 `toString` 方法 总共 `10^5` 次
至少调用 `all`、`one`、`count` 或 `toString` 方法一次
至多调用 `toString` 方法 `5` 次
"""

from typing import List, Optional


class Bitset:
    def __init__(self, size: int):
        self.size = size
        self.bits = [0] * size
        self.flipped = False
        self.ones = 0

    def fix(self, idx: int) -> None:
        if self.flipped:
            if self.bits[idx] == 1:
                self.bits[idx] = 0
                self.ones += 1
        else:
            if self.bits[idx] == 0:
                self.bits[idx] = 1
                self.ones += 1

    def unfix(self, idx: int) -> None:
        if self.flipped:
            if self.bits[idx] == 0:
                self.bits[idx] = 1
                self.ones -= 1
        else:
            if self.bits[idx] == 1:
                self.bits[idx] = 0
                self.ones -= 1

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        if self.flipped:
            return ''.join('1' if b == 0 else '0' for b in self.bits)
        return ''.join(str(b) for b in self.bits)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Design, Array, Hash Table, String
#
# 解题思路:
# 使用一个数组 bits 存储位的实际值，一个布尔变量 flipped 记录全局翻转状态，一个整数
# ones 实时维护当前值为 1 的位数。核心优化在于懒翻转：flip 操作仅切换 flipped 标志，
# 并将 ones 更新为 size - ones，实现 O(1) 时间。fix 和 unfix 操作需要根据 flipped
# 状态反向判断实际要修改的值，只在确实需要改变时才更新数组和 ones。toString 输出时
# 根据 flipped 标志决定是否对数组值进行取反显示。
#
# 时间复杂度: fix/unfix/flip/all/one/count 均为 O(1)，toString 为 O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 使用 flipped 标志实现 O(1) 全局翻转（懒翻转/Lazy Flip）
# - fix/unfix 需要根据 flipped 状态反向判断数组中的实际值
# - ones 计数器实时维护，flip 时直接 size - ones 更新
# - toString 输出时根据 flipped 标志反转每一位的显示值
