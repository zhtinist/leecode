"""
LeetCode #1117 - Building H2O
中文题名：H2O 生成
https://leetcode.com/problems/building-h2o/

There are two kinds of threads, `oxygen` and `hydrogen`. Your goal is
to group these threads to form water molecules. There is a barrier where each thread
has to wait until a complete molecule can be formed. Hydrogen and oxygen threads will
be given `releaseHydrogen` and `releaseOxygen` methods
respectively, which will allow them to pass the barrier. These threads should pass the
barrier in groups of three, and they must be able to immediately bond with each other to
form a water molecule. You must guarantee that all the threads from one molecule bond
before any other threads from the next molecule do.

In other words:

If an oxygen thread arrives at the barrier when no hydrogen threads are present, it has
to wait for two hydrogen threads.

If a hydrogen thread arrives at the barrier when no other threads are present, it has to
wait for an oxygen thread and another hydrogen thread.

We don&rsquo;t have to worry about matching the threads up explicitly; that is, the threads
do not necessarily know which other threads they are paired up with. The key is just that
threads pass the barrier in complete sets; thus, if we examine the sequence of threads that
bond and divide them into groups of three, each group should contain one oxygen and two
hydrogen threads.

Write synchronization code for oxygen and hydrogen molecules that enforces these
constraints.

【中文翻译】
有两种线程：氧线程 oxygen 和氢线程 hydrogen。你的目标是将这些线程分组以形成水分子。存在一个屏障，每个线程必须等待直到可以形成一个完整的分子。氢线程和氧线程将分别被赋予 releaseHydrogen 和 releaseOxygen 方法，这两个方法将允许它们通过屏障。这些线程应该以三个为一组通过屏障，并且它们必须能够立即相互结合形成一个水分子。你必须保证一个分子的所有线程先结合，然后下一个分子的线程才能开始。

换句话说：

如果一个氧线程到达屏障时没有氢线程存在，它必须等待两个氢线程。

如果一个氢线程到达屏障时没有其他线程存在，它必须等待一个氧线程和另一个氢线程。

我们不需要明确地匹配线程；也就是说，线程不一定知道它们与哪些其他线程配对。关键只是线程以完整的组通过屏障；因此，如果我们检查结合的线程序列并将它们分成三个一组，每组应包含一个氧和两个氢线程。

编写同步代码以强制执行这些约束。
"""

from typing import List, Optional


class H2O:
    def __init__(self):
        from threading import Semaphore
        self.h_sem = Semaphore(2)
        self.o_sem = Semaphore(0)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_sem.acquire()
        releaseHydrogen()
        self.o_sem.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_sem.acquire()
        self.o_sem.acquire()
        releaseOxygen()
        self.h_sem.release()
        self.h_sem.release()










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用两个信号量（Semaphore）控制 H 和 O 的数量比例（2:1）：
# 1. h_sem 初始值为 2（最多允许 2 个 H 线程通过）。
# 2. o_sem 初始值为 0（O 线程初始被阻塞）。
# 3. hydrogen() 方法：
#    - 获取 h_sem（消耗一个 H 配额）。
#    - 释放 H 原子（调用 releaseHydrogen）。
#    - 释放 o_sem（通知 O 线程："有一个 H 准备好了"）。
# 4. oxygen() 方法：
#    - 两次获取 o_sem（等待 2 个 H 线程都完成）。
#    - 释放 O 原子（调用 releaseOxygen）。
#    - 两次释放 h_sem（恢复 2 个 H 配额，允许下一轮）。
# 这个设计天然保证了 H:H:O = 2:1 的顺序且每组之间互不干扰。
#
# 时间复杂度: O(1) - 每个线程执行的操作为常数时间
# 空间复杂度: O(1) - 两个信号量对象
#
# 关键点:
# - 信号量 Semaphore 是天然的计数工具，非常适合控制"2个H配1个O"的比例
# - h_sem 初始 2，确保最多 2 个 H 可以先通过（如果没有 O，后续 H 会被阻塞）
# - o_sem 初始 0，O 必须等待两个 H 都完成（acquire 两次）才能通过
# - 关键逻辑：H 完成后释放 o_sem，O 完成后释放 h_sem，形成完美的资源交换
