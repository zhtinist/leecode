"""
LeetCode #1472 - Design Browser History
中文题名：设计浏览器历史记录
https://leetcode.com/problems/design-browser-history/

You have a browser of one tab where you start on the
`homepage` and you can visit another `url`, get back in the
history number of `steps` or move forward in the history number of `steps`.

Implement the `BrowserHistory` class:

`BrowserHistory(string homepage)` Initializes the object with the
`homepage` of the browser.

`void visit(string url)` visits `url` from the
current page. It clears up all the forward history.

`string back(int steps)` Move `steps` back in
history. If you can only return `x` steps in the history and `steps
> x`, you will return only `x` steps. Return the
current `url` after moving back in history at
most `steps`.

`string forward(int steps)` Move `steps` forward in
history. If you can only forward `x` steps in the history and `steps
> x`, you will forward only `x` steps. Return
the current `url` after forwarding in history at
most `steps`.

Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

Constraints:

`1 <= homepage.length <= 20`

`1 <= url.length <= 20`

`1 <= steps <= 100`

`homepage` and `url` consist of  '.' or lower case
English letters.

At most `5000` calls will be made to `visit`, `back`,
and `forward`.

【中文翻译】

你有一个只有一个标签页的浏览器，起始页面为 `homepage`，你可以访问其他 `url`，在历史记录中后退 `steps` 步或前进 `steps` 步。

实现 `BrowserHistory` 类：

`BrowserHistory(string homepage)` 用浏览器的 `homepage` 初始化对象。

`void visit(string url)` 从当前页面访问 `url`。它会清除所有前进历史记录。

`string back(int steps)` 在历史记录中后退 `steps` 步。如果只能后退 `x` 步（`x < steps`），则只后退 `x` 步。返回后退（最多 `steps` 步）后当前的 `url`。

`string forward(int steps)` 在历史记录中前进 `steps` 步。如果只能前进 `x` 步（`x < steps`），则只前进 `x` 步。返回前进（最多 `steps` 步）后当前的 `url`。

示例：
输入：
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
输出：
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

解释：
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // 当前在 "leetcode.com"，访问 "google.com"
browserHistory.visit("facebook.com");     // 当前在 "google.com"，访问 "facebook.com"
browserHistory.visit("youtube.com");      // 当前在 "facebook.com"，访问 "youtube.com"
browserHistory.back(1);                   // 当前在 "youtube.com"，后退到 "facebook.com"，返回 "facebook.com"
browserHistory.back(1);                   // 当前在 "facebook.com"，后退到 "google.com"，返回 "google.com"
browserHistory.forward(1);                // 当前在 "google.com"，前进到 "facebook.com"，返回 "facebook.com"
browserHistory.visit("linkedin.com");     // 当前在 "facebook.com"，访问 "linkedin.com"
browserHistory.forward(2);                // 当前在 "linkedin.com"，无法前进任何步
browserHistory.back(2);                   // 当前在 "linkedin.com"，后退两步到 "facebook.com" 再到 "google.com"，返回 "google.com"
browserHistory.back(7);                   // 当前在 "google.com"，只能后退一步到 "leetcode.com"，返回 "leetcode.com"

约束条件：
1 <= homepage.length <= 20
1 <= url.length <= 20
1 <= steps <= 100
homepage 和 url 由 '.' 或小写英文字母组成。
最多调用 5000 次 visit、back 和 forward。

"""

from typing import List, Optional


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0  # current index in history

    def visit(self, url: str) -> None:
        # Truncate forward history
        self.history = self.history[:self.cur + 1]
        self.history.append(url)
        self.cur += 1

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(len(self.history) - 1, self.cur + steps)
        return self.history[self.cur]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 使用一个列表（或两个栈）来维护浏览历史，并用一个指针 cur
#    表示当前页面在历史记录中的位置。
# 2. visit(url)：将 cur 之后的所有前进历史清除（截断列表），
#    然后将新 URL 追加到列表末尾，cur 指向新位置。
# 3. back(steps)：cur 向前移动 steps 步，但不能小于 0，
#    返回 history[cur]。
# 4. forward(steps)：cur 向后移动 steps 步，但不能超过
#    len(history)-1，返回 history[cur]。
# 5. 所有操作都是 O(1) 时间复杂度。
#
# 时间复杂度: O(1) 每次操作
# 空间复杂度: O(N)，其中 N 是访问的页面数量
#
# 关键点:
# - visit 时需要清除所有前进历史记录
# - back/forward 时注意边界检查
# - 使用列表 + 指针比两个栈更直观










