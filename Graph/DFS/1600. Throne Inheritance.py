"""
LeetCode #1600 - Throne Inheritance
中文题名：皇位继承顺序
https://leetcode.com/problems/throne-inheritance/


A kingdom consists of a king, his children, his grandchildren, and so on. Every once
in a while, someone in the family dies or a child is born.

The kingdom has a well-defined order of inheritance that consists of the king as the
first member. Let's define the recursive function `Successor(x,
curOrder)`, which given a person `x` and the inheritance order
so far, returns who should be the next person after `x` in the order of
inheritance.

Successor(x, curOrder):
if x has no children or all of x's children are in curOrder:
if x is the king return null
else return Successor(x's parent, curOrder)
else return x's oldest child who's not in curOrder

For example, assume we have a kingdom that consists of the king, his children Alice
and Bob (Alice is older than Bob), and finally Alice's son Jack.

In the beginning, `curOrder` will be `["king"]`.

Calling `Successor(king, curOrder)` will return Alice, so we append
to `curOrder` to get `["king", "Alice"]`.

Calling `Successor(Alice, curOrder)` will return Jack, so we append
to `curOrder` to get `["king", "Alice", "Jack"]`.

Calling `Successor(Jack, curOrder)` will return Bob, so we append to
`curOrder` to get `["king", "Alice", "Jack", "Bob"]`.

Calling `Successor(Bob, curOrder)` will return `null`.
Thus the order of inheritance will be `["king", "Alice", "Jack",
"Bob"]`.

Using the above function, we can always obtain a unique order of inheritance.

Implement the `ThroneInheritance` class:

`ThroneInheritance(string kingName)` Initializes an object of the
`ThroneInheritance` class. The name of the king is given as part of
the constructor.

`void birth(string parentName, string childName)` Indicates that
`parentName` gave birth to `childName`.

`void death(string name)` Indicates the death of `name`.
The death of the person doesn't affect the `Successor` function nor
the current inheritance order. You can treat it as just marking the person as
dead.

`string[] getInheritanceOrder()` Returns a list representing the
current order of inheritance excluding dead people.

Example 1:

Input
["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death", "getInheritanceOrder"]
[["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [null], ["bob"], [null]]
Output
[null, null, null, null, null, null, null, ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"], null, ["king", "andy", "matthew", "alex", "asha", "catherine"]]

Explanation
ThroneInheritance t= new ThroneInheritance("king"); // order: king
t.birth("king", "andy"); // order: king > andy
t.birth("king", "bob"); // order: king > andy > bob
t.birth("king", "catherine"); // order: king > andy > bob > catherine
t.birth("andy", "matthew"); // order: king > andy > matthew > bob > catherine
t.birth("bob", "alex"); // order: king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha"); // order: king > andy > matthew > bob > alex > asha > catherine
t.getInheritanceOrder(); // return ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob"); // order: king > andy > matthew > bob > alex > asha > catherine
t.getInheritanceOrder(); // return ["king", "andy", "matthew", "alex", "asha", "catherine"]

Constraints:

`1 <= kingName.length, parentName.length, childName.length, name.length
<= 15`

`kingName`, `parentName`, `childName`, and
`name` consist of lowercase English letters only.

All arguments `childName` and `kingName` are distinct.

All `name` arguments of `death` will be passed to either
the constructor or as `childName` to `birth` first.

For each call to `birth(parentName, childName)`, it is
guaranteed that `parentName` is alive.

At most `105` calls will be made to `birth` and
`death`.

At most `10` calls will be made to `getInheritanceOrder`.

【中文翻译】
一个王国由国王及其后代组成。继承顺序按 先嫡长子 规则：
国王的子女按出生顺序排列，每个人的后代也按相同规则排列。
实现 ThroneInheritance 类：birth(parentName, childName) - 孩子出生；
death(name) - 某人死亡（不影响继承顺序，只是被跳过）；
getInheritanceOrder() - 返回当前继承顺序列表（排除死亡的人）。

示例：略（详见 LeetCode 原题）
"""

from typing import List, Optional
from collections import defaultdict


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = kingName
        self.children = defaultdict(list)
        self.dead = set()
    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)
    def death(self, name: str) -> None:
        self.dead.add(name)
    def getInheritanceOrder(self) -> List[str]:
        result = []
        def dfs(name: str):
            if name not in self.dead:
                result.append(name)
            for child in self.children[name]:
                dfs(child)
        dfs(self.king)
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 多叉树的前序遍历（Preorder DFS）。继承顺序 = 树的前序遍历结果（跳过死亡节点）。
# 使用 defaultdict(list) 存储每个节点的子节点列表（按出生顺序）。
# death 将节点标记为死亡（加入集合）。
# getInheritanceOrder 执行前序遍历，跳过死亡节点。
#
# 时间复杂度: birth: O(1), death: O(1), getInheritanceOrder: O(N)
# 空间复杂度: O(N) — 存储树结构和死亡集合
#
# 关键点:
# - 继承顺序 = 树的前序遍历
# - 死亡不影响继承顺序，只是跳过
# - 子节点按出生顺序存储












