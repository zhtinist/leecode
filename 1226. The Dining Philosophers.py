"""
LeetCode #1226 - The Dining Philosophers
中文题名：哲学家进餐
https://leetcode.com/problems/the-dining-philosophers/

Five silent philosophers sit at a round table with bowls of spaghetti. Forks are placed
between each pair of adjacent philosophers.

Each philosopher must alternately think and eat. However, a philosopher can only eat
spaghetti when they have both left and right forks. Each fork can be held by only one
philosopher and so a philosopher can use the fork only if it is not being used by another
philosopher. After an individual philosopher finishes eating, they need to put down both
forks so that the forks become available to others. A philosopher can take the fork on their
right or the one on their left as they become available, but cannot start eating before
getting both forks.

Eating is not limited by the remaining amounts of spaghetti or stomach space; an infinite
supply and an infinite demand are assumed.

Design a discipline of behavior (a concurrent algorithm) such that no philosopher will
starve; i.e., each can forever continue to alternate between eating and
thinking, assuming that no philosopher can know when others may want to eat or think.

The problem statement and the image above are taken from wikipedia.org

The philosophers' ids are numbered from 0 to 4 in a
clockwise order. Implement the function `void
wantsToEat(philosopher, pickLeftFork, pickRightFork, eat, putLeftFork,
putRightFork)` where:

`philosopher` is the id of the philosopher who wants to eat.

`pickLeftFork` and `pickRightFork` are functions
you can call to pick the corresponding forks of that philosopher.

`eat` is a function you can call to let the philosopher eat once he has
picked both forks.

`putLeftFork` and `pickRightFork` are functions you
can call to put down the corresponding forks of that philosopher.

The philosophers are assumed to be thinking as long as they are not asking to eat (the
function is not being called with their number).

Five threads, each representing a philosopher, will simultaneously use one object of
your class to simulate the process. It is possible that the function will be called for the
same philosopher more than once, even before the last call ends.

Example 1:

Input: n = 1
Output: [[4,2,1],[4,1,1],[0,1,1],[2,2,1],[2,1,1],[2,0,3],[2,1,2],[2,2,2],[4,0,3],[4,1,2],[0,2,1],[4,2,2],[3,2,1],[3,1,1],[0,0,3],[0,1,2],[0,2,2],[1,2,1],[1,1,1],[3,0,3],[3,1,2],[3,2,2],[1,0,3],[1,1,2],[1,2,2]]
Explanation:
n is the number of times each philosopher will call the function.
The output array describes the calls you made to the functions controlling the forks and the eat function, its format is:
output[i] = [a, b, c] (three integers)
- a is the id of a philosopher.
- b specifies the fork: {1 : left, 2 : right}.
- c specifies the operation: {1 : pick, 2 : put, 3 : eat}.

Constraints:

`1 <= n <= 60`

【中文翻译】
五个沉默的哲学家坐在一张圆桌前，每人面前放着一盘意大利面。叉子放在每对相邻哲学家之间。

每个哲学家必须交替地思考和进餐。然而，哲学家只有在同时拿到左手边和右手边的叉子时才能吃面。每个叉子只能被一个哲学家使用，因此哲学家只能在没有其他哲学家使用时才能使用叉子。在哲学家吃完后，他们需要放下两把叉子，以便其他人使用。哲学家可以在右手或左手的叉子可用时拿起它，但不能在拿到两把叉子之前开始进食。

进餐不受剩余意大利面或胃量的限制；假设无限供应和无限需求。

设计一种行为规范（并发算法），使得没有哲学家会饿死；即每个哲学家可以永远继续交替进餐和思考，假设没有一个哲学家知道其他人何时想要进餐或思考。

问题陈述和上图来自 wikipedia.org。

哲学家的 ID 从 0 到 4 按顺时针方向编号。实现函数 void wantsToEat(philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork)：

philosopher 是想要进餐的哲学家的 ID。
pickLeftFork 和 pickRightFork 是你可以调用来拿起相应叉子的函数。
eat 是你可以调用的函数，让哲学家在拿到两把叉子后进餐。
putLeftFork 和 putRightFork 是你可以调用来放下相应叉子的函数。
哲学家在未请求进餐时假定处于思考状态（即没有以其编号调用函数）。

五个线程，每个代表一个哲学家，将同时使用你的类的一个对象来模拟这个过程。函数可能会在同一个哲学家上次调用还未结束时再次被调用。

示例 1：

输入：n = 1
输出：[[4,2,1],[4,1,1],[0,1,1],[2,2,1],[2,1,1],[2,0,3],[2,1,2],[2,2,2],[4,0,3],[4,1,2],[0,2,1],[4,2,2],[3,2,1],[3,1,1],[0,0,3],[0,1,2],[0,2,2],[1,2,1],[1,1,1],[3,0,3],[3,1,2],[3,2,2],[1,0,3],[1,1,2],[1,2,2]]
解释：
n 表示每个哲学家调用函数的次数。
输出数组描述了你对控制叉子和进餐函数的调用，其格式为：
output[i] = [a, b, c]（三个整数）
- a 是哲学家的 ID。
- b 指定叉子：{1 : 左, 2 : 右}。
- c 指定操作：{1 : 拿起, 2 : 放下, 3 : 进食}。

约束条件：

1 <= n <= 60

"""

from typing import List, Optional, Callable
from threading import Lock, Semaphore


class Solution:
    """
    LeetCode expects class DiningPhilosophers, but this file uses Solution.
    The wantsToEat method below is the required interface.

    策略：限制最多 4 个哲学家同时尝试拿叉子（Semaphore(4)），
    加上每把叉子一个 Lock，破坏死锁的四个必要条件之一（循环等待）。
    """
    def __init__(self):
        self.forks = [Lock() for _ in range(5)]
        self.sem = Semaphore(4)  # 最多允许 4 个哲学家同时尝试

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: Callable[[], None],
                   pickRightFork: Callable[[], None],
                   eat: Callable[[], None],
                   putLeftFork: Callable[[], None],
                   putRightFork: Callable[[], None]) -> None:
        left = philosopher
        right = (philosopher + 1) % 5

        with self.sem:
            with self.forks[left]:
                with self.forks[right]:
                    pickLeftFork()
                    pickRightFork()
                    eat()
                    putLeftFork()
                    putRightFork()










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 经典的"哲学家就餐问题"(Dining Philosophers Problem)，由 Edsger Dijkstra 提出，
# 是并发编程中死锁和饥饿问题的经典案例。
#
# 死锁的四个必要条件（Coffman 条件）：
# 1. 互斥：资源不可共享
# 2. 持有并等待：持有资源的同时等待其他资源
# 3. 不可抢占：资源不能被强制剥夺
# 4. 循环等待：存在进程-资源的循环等待链
#
# 本解法采用"限制同时进食人数"策略打破循环等待：
# - 每把叉子用一个 Lock 保护（满足互斥）。
# - 使用 Semaphore(4) 限制最多 4 个哲学家同时尝试拿叉子。
# - 当 4 个哲学家各拿一把叉子时，至少有一对相邻的哲学家之间，
#   其中一个的"第二把叉子"是空闲的（共 5 把叉子，4 人持有 4 把），
#   所以不会形成循环等待，不会死锁。
#
# 其他可行策略：
# - 让奇数号哲学家先拿左叉，偶数号先拿右叉（打破对称性）
# - 使用 try-acquire 并在失败时释放已持有的叉子
# - 使用一个全局锁串行化所有进餐操作
#
# 时间复杂度: O(1) 每次调用 - 锁获取和释放是常数时间
# 空间复杂度: O(1) - 5 个 Lock + 1 个 Semaphore，固定大小
#
# 关键点:
# - Semaphore(4) 是关键：打破循环等待，防止 5 个哲学家各持一把叉子而僵持
# - 左右叉子的编号规则：左叉 = philosopher，右叉 = (philosopher + 1) % 5
# - 使用 context manager (with) 确保锁的正确释放，即使发生异常也不会泄漏
# - 注意确保 pick/put callbacks 的调用顺序：先拿后吃，吃完再放
