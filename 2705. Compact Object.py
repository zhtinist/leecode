"""
LeetCode #2705 - Compact Object
精简对象
https://leetcode.cn/problems/compact-object/

现给定一个对象或数组 `obj`，返回一个 精简对象 。
精简对象 与原始对象相同，只是将包含 假 值的键移除。该操作适用于对象及其嵌套对象。数组被视为索引作为键的对象。当 `Boolean(value)` 返回 `false` 时，值被视为 假 值。
你可以假设 `obj` 是 `JSON.parse` 的输出结果。换句话说，它是有效的 JSON。

示例 1：
输入：obj = [null, 0, false, 1] 输出：[1] 解释：数组中的所有假值已被移除。
示例 2：
输入：obj = {"a": null, "b": [false, 1]} 输出：{"b": [1]} 解释：obj["a"] 和 obj["b"][0] 包含假值，因此被移除。
示例 3：
输入：obj = [null, 0, 5, [0], [false, 16]] 输出：[5, [], [16]] 解释：obj[0], obj[1], obj[3][0], 和 obj[4][0] 包含假值，因此被移除。

提示：
`obj` 是一个有效的 JSON 对象
`2 <= JSON.stringify(obj).length <= 10^6`
"""

from typing import List, Optional


class Solution:

    def compactObject(self, obj):
        """Remove falsy values from objects/arrays recursively.
        Arrays keep their structure; falsy elements are filtered out.
        Objects drop keys whose values are falsy.
        Empty arrays/objects are kept (they are truthy)."""
        if isinstance(obj, list):
            result = []
            for item in obj:
                compacted = self.compactObject(item)
                # Only add to array if the value is truthy after compaction
                # Lists/dicts are always truthy (even empty)
                if isinstance(compacted, (list, dict)):
                    result.append(compacted)
                elif bool(compacted):
                    result.append(compacted)
            return result
        elif isinstance(obj, dict):
            result = {}
            for k, v in obj.items():
                compacted = self.compactObject(v)
                # Keep key if value is truthy after compaction
                if isinstance(compacted, (list, dict)):
                    result[k] = compacted
                elif bool(compacted):
                    result[k] = compacted
            return result
        else:
            return obj



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: 
#
# 解题思路:
# 递归处理对象和数组。对于数组，递归压缩每个元素后保留truthy值（非falsy）。
# 对于字典，递归压缩每个值后移除值为falsy的键。基本类型直接返回。
# 空数组和空字典被视为truthy（它们是容器对象），应保留。
#
# 时间复杂度: O(N) 其中N是所有嵌套元素总数
# 空间复杂度: O(N + D) 其中D是嵌套深度
#
# 关键点:
# - 区分基本类型和容器类型（list/dict始终truthy）
# - 递归处理嵌套结构
# - Python中falsy值: None, False, 0, 0.0, "", [], {}
