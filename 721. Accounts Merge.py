"""
LeetCode #721 - Accounts Merge
中文题名：账户合并
https://leetcode.com/problems/accounts-merge/

Given a list `accounts`, each element `accounts[i]` is a list of
strings, where the first element `accounts[i][0]` is a name, and the rest
of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person
if there is some email that is common to both accounts. Note that even if two accounts have
the same name, they may belong to different people as people could have the same name. A
person can have any number of accounts initially, but all of their accounts definitely have
the same name.

After merging the accounts, return the accounts in the following format: the first element of
each account is the name, and the rest of the elements are emails in sorted order.
The accounts themselves can be returned in any order.

Example 1:

Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Note:

The length of `accounts` will be in the range `[1, 1000]`.

The length of `accounts[i]` will be in the range `[1, 10]`.

The length of `accounts[i][j]` will be in the range `[1, 30]`.

【中文翻译】
给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是名称 (name)，其余元素是 emails 表示该账户的邮箱地址。

现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。

合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。账户本身可以以任意顺序返回。

示例 1：

输入：
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
输出：[["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
解释：
第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。
第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他账户使用。
我们可以以任何顺序返回这些列表，例如答案 [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] 仍然会被接受。

注意：

accounts 的长度将在 [1, 1000] 的范围内。

accounts[i] 的长度将在 [1, 10] 的范围内。

accounts[i][j] 的长度将在 [1, 30] 的范围内。
"""

from typing import List, Optional


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        owner = {}

        def find(x: str) -> str:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: str, y: str) -> None:
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                    owner[email] = name
                union(email, account[1])

        groups: dict = {}
        for email in parent:
            root = find(email)
            if root not in groups:
                groups[root] = []
            groups[root].append(email)

        result = []
        for emails in groups.values():
            result.append([owner[emails[0]]] + sorted(emails))
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用并查集（Union-Find）解决账户合并问题。
# 将每封邮件看作一个节点，同一账户下的邮件属于同一个连通分量。
# 对于每个账户，将其第一个邮箱与其余邮箱逐一合并。
# 使用 owner 字典记录每个邮箱对应的账户名。
# 最后，对于每个连通分量，将所有邮箱收集起来并排序，加上账户名即可。
#
# 时间复杂度: O(E * α(E) + E log E) - E 为邮箱总数，α 为反阿克曼函数近乎常数，排序占主导
# 空间复杂度: O(E) - 存储并查集和家长、所有者映射
#
# 关键点:
# - 核心洞察：通过邮箱将不同账户关联起来，相同邮箱表示同一个人
# - 并查集的 find 操作使用路径压缩优化
# - 最终每个连通分量的邮箱需要按字典序排序
# - 不能仅凭名字合并账户，必须通过共同邮箱来判断
