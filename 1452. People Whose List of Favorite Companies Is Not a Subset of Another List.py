"""
LeetCode #1452 - People Whose List of Favorite Companies Is Not a Subset of Another List
中文题名：收藏清单
https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

Given the array `favoriteCompanies` where
`favoriteCompanies[i]` is the list of favorites companies for the
`ith` person (indexed from 0).

Return the indices of people whose list of favorite companies is not a subset
of any other list of favorites companies. You must return the indices in
increasing order.

Example 1:

Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
Output: [0,1,4]
Explanation:
Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0.
Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"].
Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].

Example 2:

Input: favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
Output: [0,1]
Explanation: In this case favoriteCompanies[2]=["facebook","google"] is a subset of favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer is [0,1].

Example 3:

Input: favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
Output: [0,1,2,3]

Constraints:

`1 <= favoriteCompanies.length <= 100`

`1 <= favoriteCompanies[i].length <= 500`

`1 <= favoriteCompanies[i][j].length <= 20`

All strings in `favoriteCompanies[i]` are distinct.

All lists of favorite companies are distinct, that is, If we
sort alphabetically each list then `favoriteCompanies[i] !=
favoriteCompanies[j].`

All strings consist of lowercase English letters only.

【中文翻译】
给定数组 `favoriteCompanies`，其中 `favoriteCompanies[i]` 是
第 `i` 个人（从 0 开始索引）最喜欢的公司列表。

返回那些最喜欢的公司列表不是任何其他人收藏列表的子集的人的下标。
你必须按递增顺序返回下标。

示例 1：

输入：favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
输出：[0,1,4]
解释：
下标为 2 的人的 favoriteCompanies[2]=["google","facebook"] 是
favoriteCompanies[0]=["leetcode","google","facebook"] 的子集（对应下标为 0 的人）。
下标为 3 的人的 favoriteCompanies[3]=["google"] 是
favoriteCompanies[0]=["leetcode","google","facebook"] 和
favoriteCompanies[1]=["google","microsoft"] 的子集。
其他人的收藏公司列表不是任何其他列表的子集，因此答案是 [0,1,4]。

示例 2：

输入：favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
输出：[0,1]
解释：在这种情况下，favoriteCompanies[2]=["facebook","google"] 是
favoriteCompanies[0]=["leetcode","google","facebook"] 的子集，因此答案是 [0,1]。

示例 3：

输入：favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
输出：[0,1,2,3]

约束条件：

`1 <= favoriteCompanies.length <= 100`

`1 <= favoriteCompanies[i].length <= 500`

`1 <= favoriteCompanies[i][j].length <= 20`

`favoriteCompanies[i]` 中的所有字符串都是不同的。

所有收藏公司列表都是不同的，即按字母顺序排序后 `favoriteCompanies[i] != favoriteCompanies[j]`。

所有字符串仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        sets = [set(companies) for companies in favoriteCompanies]
        ans = []
        for i in range(n):
            is_subset = False
            for j in range(n):
                if i == j:
                    continue
                if sets[i].issubset(sets[j]):
                    is_subset = True
                    break
            if not is_subset:
                ans.append(i)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将每个人的公司列表转换为集合（set），便于快速子集判断。
# 对于每个人 i，检查是否存在另一个人 j (j != i) 使得 i 的集合是 j 的集合的子集。
# 如果没有任何 j 的集合是 i 的严格超集（即 i 不是任何其他人的子集），
# 则将 i 加入结果列表。
# 注意：由于所有列表互不相同，使用 issubset 时会自动处理严格子集的情况。
#
# 时间复杂度: O(N^2 * M)  -- N 是人数，M 是平均公司数，子集判断 O(M)
# 空间复杂度: O(N * M)  -- 存储 N 个集合
#
# 关键点:
# - 使用 Python set 的 issubset 方法高效判断子集关系
# - 由于题目保证所有列表互不相同，issubset 返回 True 意味着是严格子集
# - 结果需要按递增顺序返回下标









