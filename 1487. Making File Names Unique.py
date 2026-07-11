"""
LeetCode #1487 - Making File Names Unique
中文题名：保证文件名唯一
https://leetcode.com/problems/making-file-names-unique/

Given an array of strings `names` of size `n`. You will create
`n` folders in your file system such that, at the
`ith` minute, you will create a folder with the name `names[i]`.

Since two files cannot have the same name, if you enter a folder
name which is previously used, the system will have a suffix addition
to its name in the form of `(k)`, where, `k` is the
smallest positive integer such that the obtained name remains
unique.

Return an array of strings of length `n` where
`ans[i]` is the actual name the system will assign to the
`ith` folder when you create it.

Example 1:

Input: names = ["pes","fifa","gta","pes(2019)"]
Output: ["pes","fifa","gta","pes(2019)"]
Explanation: Let's see how the file system creates folder names:
"pes" --> not assigned before, remains "pes"
"fifa" --> not assigned before, remains "fifa"
"gta" --> not assigned before, remains "gta"
"pes(2019)" --> not assigned before, remains "pes(2019)"

Example 2:

Input: names = ["gta","gta(1)","gta","avalon"]
Output: ["gta","gta(1)","gta(2)","avalon"]
Explanation: Let's see how the file system creates folder names:
"gta" --> not assigned before, remains "gta"
"gta(1)" --> not assigned before, remains "gta(1)"
"gta" --> the name is reserved, system adds (k), since "gta(1)" is also reserved, systems put k = 2. it becomes "gta(2)"
"avalon" --> not assigned before, remains "avalon"

Example 3:

Input: names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
Output: ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
Explanation: When the last folder is created, the smallest positive valid k is 4, and it becomes "onepiece(4)".

Example 4:

Input: names = ["wano","wano","wano","wano"]
Output: ["wano","wano(1)","wano(2)","wano(3)"]
Explanation: Just increase the value of k each time you create folder "wano".

Example 5:

Input: names = ["kaido","kaido(1)","kaido","kaido(1)"]
Output: ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
Explanation: Please note that system adds the suffix (k) to current name even it contained the same suffix before.

Constraints:

`1 <= names.length <= 5 * 10^4`

`1 <= names[i].length <= 20`

`names[i]` consists of lower case English letters, digits and/or
round brackets.

【中文翻译】

给定一个大小为 `n` 的字符串数组 `names`。你将创建 `n` 个文件夹，在第 `i` 分钟，你将创建一个名为 `names[i]` 的文件夹。

由于两个文件不能有相同的名称，如果你输入一个之前已使用过的文件夹名称，系统将在其名称后添加一个后缀 `(k)`，其中 `k` 是使所得名称保持唯一的最小正整数。

返回一个长度为 `n` 的字符串数组，其中 `ans[i]` 是系统在创建第 `i` 个文件夹时实际分配的名称。

示例 1：
输入：names = ["pes","fifa","gta","pes(2019)"]
输出：["pes","fifa","gta","pes(2019)"]
解释：让我们看看文件系统如何创建文件夹名称：
"pes" --> 之前未被分配，保持 "pes"
"fifa" --> 之前未被分配，保持 "fifa"
"gta" --> 之前未被分配，保持 "gta"
"pes(2019)" --> 之前未被分配，保持 "pes(2019)"

示例 2：
输入：names = ["gta","gta(1)","gta","avalon"]
输出：["gta","gta(1)","gta(2)","avalon"]
解释：
"gta" --> 之前未被分配，保持 "gta"
"gta(1)" --> 之前未被分配，保持 "gta(1)"
"gta" --> 名称已被占用，系统添加 (k)，由于 "gta(1)" 也被占用，系统设 k = 2，变为 "gta(2)"
"avalon" --> 之前未被分配，保持 "avalon"

示例 3：
输入：names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
输出：["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
解释：创建最后一个文件夹时，最小的正有效 k 是 4，变为 "onepiece(4)"。

示例 4：
输入：names = ["wano","wano","wano","wano"]
输出：["wano","wano(1)","wano(2)","wano(3)"]
解释：每次创建文件夹 "wano" 时递增 k 的值。

示例 5：
输入：names = ["kaido","kaido(1)","kaido","kaido(1)"]
输出：["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
解释：请注意，系统将后缀 (k) 添加到当前名称，即使它之前已包含相同的后缀。

约束条件：
1 <= names.length <= 5 * 10^4
1 <= names[i].length <= 20
names[i] 由小写英文字母、数字和/或圆括号组成。

"""

from typing import List, Optional


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # name -> next available suffix number
        used = {}

        result = []
        for name in names:
            if name not in used:
                used[name] = 1
                result.append(name)
            else:
                # Find next available number
                k = used[name]
                while True:
                    candidate = f"{name}({k})"
                    if candidate not in used:
                        used[name] = k + 1
                        used[candidate] = 1
                        result.append(candidate)
                        break
                    k += 1

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 使用哈希表 used 记录每个名称的状态：
#    - 如果名称未被占用，used[name] = 1（下一次尝试用的最小 k）
#    - 如果名称已被占用，used[name] 记录下一个可尝试的最小 k 值
# 2. 遍历每个 names[i]：
#    - 如果 name 不在 used 中，直接使用，设置 used[name] = 1
#    - 如果 name 已被占用，从 used[name] 开始尝试 name(k)，
#      每次 k++，直到找到一个未被占用的名称。
#      更新 used[name] = k+1 并标记新名称已使用。
# 3. 注意：原始名称和加了后缀的名称都要记录在哈希表中。
# 4. 虽然 while 循环看起来像 O(K^2)，但每个 k 值只会被尝试一次，
#    均摊时间复杂度为 O(N)。
#
# 时间复杂度: O(N) 均摊
# 空间复杂度: O(N)
#
# 关键点:
# - 哈希表记录每个名称的下一个可用 k 值，避免重复尝试
# - 原始名称和带后缀的名称都需要记录在 used 中
# - 即使名称本身包含 (k) 格式，也按原样处理（如 "kaido(1)" -> "kaido(1)(1)"）
# - 均摊分析：每个 k 值只被尝试一次










