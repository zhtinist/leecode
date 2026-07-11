"""
LeetCode #380 - Insert Delete GetRandom O(1)
中文题名：O(1) 时间插入、删除和获取随机元素
https://leetcode.com/problems/insert-delete-getrandom-o1/

Design a data structure that supports all following operations in average O(1)
time.

`insert(val)`: Inserts an item val to the set if not already present.

`remove(val)`: Removes an item val from the set if present.

`getRandom`: Returns a random element from current set of elements. Each
element must have the same probability of being returned.

Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

【中文翻译】
设计一个数据结构，支持在平均 O(1) 时间复杂度下执行以下所有操作。

insert(val)：如果元素 val 不存在，则将其插入到集合中。

remove(val)：如果元素 val 存在，则将其从集合中移除。

getRandom：从当前元素集合中随机返回一个元素。每个元素被返回的概率必须相同。

示例：

// 初始化一个空的集合。
RandomizedSet randomSet = new RandomizedSet();

// 向集合中插入 1。返回 true，因为 1 被成功插入。
randomSet.insert(1);

// 返回 false，因为 2 不在集合中。
randomSet.remove(2);

// 向集合中插入 2，返回 true。集合现在包含 [1,2]。
randomSet.insert(2);

// getRandom 应随机返回 1 或 2。
randomSet.getRandom();

// 从集合中移除 1，返回 true。集合现在包含 [2]。
randomSet.remove(1);

// 2 已经在集合中，因此返回 false。
randomSet.insert(2);

// 由于 2 是集合中唯一的数字，getRandom 始终返回 2。
randomSet.getRandom();
"""

import random
from typing import List, Optional


class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}  # val -> index in values list
        self.values = []        # dynamic array storing values

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        # 将要删除的元素与数组末尾元素交换，然后 pop 末尾（O(1)）
        idx = self.val_to_index[val]
        last_val = self.values[-1]
        self.values[idx] = last_val
        self.val_to_index[last_val] = idx
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 要实现 O(1) 时间复杂度的插入、删除和随机获取，核心是结合哈希表（字典）和动态数组。
# 两种数据结构互补不足：
# - 哈希表 O(1) 查找/插入/删除，但无法 O(1) 随机获取元素
# - 动态数组 O(1) 随机访问，O(1) 末尾插入，但 O(N) 按值查找/删除
#
# 具体设计：
# - insert(val)：检查 val 是否在哈希表中存在，如果不存在则追加到数组末尾，
#   并在哈希表中记录 val -> index 的映射，O(1)
# - getRandom()：使用 random.choice 从数组中随机选取，O(1)
# - remove(val)：这是最关键的操作。不能直接从数组中间删除（需要移动 O(N) 个元素），
#   技巧是将要删除的元素与数组最后一个元素交换，然后弹出末尾：
#   1. 在哈希表中找到要删除元素 val 的索引 idx
#   2. 获取数组最后一个元素 last_val
#   3. 将 last_val 放到 idx 位置（覆盖 val）
#   4. 更新 last_val 在哈希表中的索引为 idx
#   5. pop 掉数组末尾元素
#   6. 从哈希表中删除 val 的映射
#   注意：步骤 4 和 5 的顺序很重要，先更新映射再 pop
#
# 时间复杂度: 所有操作均为 O(1) 平均时间
# 空间复杂度: O(N) - N 为存储的元素数量
#
# 关键点:
# - 哈希表 + 数组是经典组合：数组支持随机访问，哈希表补足快速查找
# - 删除时用"交换到末尾再弹出"的技巧避免 O(N) 的元素移动
# - 删除时注意先更新 last_val 的索引映射，再 pop（否则如果 val 恰好是最后一个元素会出错）
# - random.choice 对列表是 O(1) 操作
