"""
LeetCode #2722 - Join Two Arrays by ID
根据 ID 合并两个数组
https://leetcode.cn/problems/join-two-arrays-by-id/

现给定两个数组 `arr1` 和 `arr2` ，返回一个新的数组 `joinedArray` 。两个输入数组中的每个对象都包含一个 `id` 字段。
`joinedArray` 是一个通过 `id` 将 `arr1` 和 `arr2` 连接而成的数组。`joinedArray` 的长度应为唯一值 `id` 的长度。返回的数组应按 `id` 升序 排序。
如果一个 `id` 存在于一个数组中但不存在于另一个数组中，则该对象应包含在结果数组中且不进行修改。
如果两个对象共享一个 `id` ，则它们的属性应进行合并：
如果一个键只存在于一个对象中，则该键值对应该包含在对象中。
如果一个键在两个对象中都包含，则 `arr2` 中的值应覆盖 `arr1` 中的值。

示例 1：
输入： arr1 = [     {"id": 1, "x": 1},     {"id": 2, "x": 9} ],  arr2 = [     {"id": 3, "x": 5} ] 输出： [     {"id": 1, "x": 1},     {"id": 2, "x": 9},     {"id": 3, "x": 5} ] 解释：没有共同的 id，因此将 arr1 与 arr2 简单地连接起来。
示例 2：
输入： arr1 = [     {"id": 1, "x": 2, "y": 3},     {"id": 2, "x": 3, "y": 6} ],  arr2 = [     {"id": 2, "x": 10, "y": 20},     {"id": 3, "x": 0, "y": 0} ] 输出： [     {"id": 1, "x": 2, "y": 3},     {"id": 2, "x": 10, "y": 20},     {"id": 3, "x": 0, "y": 0} ] 解释：id 为 1 和 id 为 3 的对象在结果数组中保持不变。id 为 2 的两个对象合并在一起。arr2 中的键覆盖 arr1 中的值。
示例 3：
输入： arr1 = [     {"id": 1, "b": {"b": 94},"v": [4, 3], "y": 48} ] arr2 = [     {"id": 1, "b": {"c": 84}, "v": [1, 3]} ] 输出： [     {"id": 1, "b": {"c": 84}, "v": [1, 3], "y": 48} ] 解释：具有 id 为 1 的对象合并在一起。对于键 "b" 和 "v" ，使用 arr2 中的值。由于键 "y" 只存在于 arr1 中，因此取 arr1 的值。

提示：
`arr1 和 arr2 都是有效的 JSON 数组`
`在 arr1 和 arr2 中都有唯一的键值 id`
`2 <= JSON.stringify(arr1).length <= 10^6`
`2 <= JSON.stringify(arr2).length <= 10^6`
"""

from typing import List, Optional


class Solution:
    def join(self, arr1: List[dict], arr2: List[dict]) -> List[dict]:
        merged = {}
        for obj in arr1:
            merged[obj["id"]] = dict(obj)
        for obj in arr2:
            if obj["id"] in merged:
                merged[obj["id"]].update(obj)
            else:
                merged[obj["id"]] = dict(obj)
        result = sorted(merged.values(), key=lambda x: x["id"])
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: 
#
# 解题思路:
# 原题为 JavaScript 的数组合并问题。使用字典按 id 合并两个数组中的对象。
# 先遍历 arr1 将对象存入字典，再遍历 arr2 更新或新增对象（arr2 的值覆盖 arr1）。
# 最后按 id 升序排序返回结果。
#
# 时间复杂度: O((n+m)log(n+m)) 其中 n,m 是两个数组的长度，排序占主导
# 空间复杂度: O(n+m) 用于存储合并后的字典
#
# 关键点:
# - 使用 id 作为字典键进行 O(1) 查找和合并
# - arr2 的值覆盖 arr1 的相同键（使用 dict.update）
# - 最终按 id 升序排序
# - Python 中使用 dict(obj) 创建副本避免修改原数据
