"""
LeetCode #1116 - Print Zero Even Odd
中文题名：打印零与奇偶数
https://leetcode.com/problems/print-zero-even-odd/

Suppose you are given the following code:

class ZeroEvenOdd {
public ZeroEvenOdd(int n) { ... }      // constructor
public void zero(printNumber) { ... }  // only output 0's
public void even(printNumber) { ... }  // only output even numbers
public void odd(printNumber) { ... }   // only output odd numbers
}

The same instance of `ZeroEvenOdd` will be passed to three different threads:

Thread A will call `zero()` which should only output 0's.

Thread B will call `even()` which should only ouput even numbers.

Thread C will call `odd()` which should only output odd numbers.

Each of the threads is given a `printNumber` method to output an
integer. Modify the given program to output the series `010203040506`...
where the length of the series must be 2n.

Example 1:

Input: n = 2
Output: "0102"
Explanation: There are three threads being fired asynchronously. One of them calls zero(), the other calls even(), and the last one calls odd(). "0102" is the correct output.

Example 2:

Input: n = 5
Output: "0102030405"

【中文翻译】
假设给你以下代码：

class ZeroEvenOdd {
  public ZeroEvenOdd(int n) { ... }      // 构造函数
  public void zero(printNumber) { ... }  // 只输出 0
  public void even(printNumber) { ... }  // 只输出偶数
  public void odd(printNumber) { ... }   // 只输出奇数
}

相同的 ZeroEvenOdd 实例将被传递给三个不同的线程：

线程 A 将调用 zero()，应该只输出 0。

线程 B 将调用 even()，应该只输出偶数。

线程 C 将调用 odd()，应该只输出奇数。

每个线程都被赋予一个 printNumber 方法来输出一个整数。修改给定的程序，使其输出序列 "010203040506"...，其中序列的长度必须为 2n。

示例 1：

输入：n = 2
输出："0102"
解释：有三个线程被异步启动。其中一个调用 zero()，另一个调用 even()，最后一个调用 odd()。"0102" 是正确的输出。

示例 2：

输入：n = 5
输出："0102030405"
"""

from typing import List, Optional


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        from threading import Lock
        self.zero_lock = Lock()
        self.odd_lock = Lock()
        self.even_lock = Lock()
        self.odd_lock.acquire()
        self.even_lock.acquire()

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zero_lock.acquire()
            printNumber(0)
            if i % 2 == 1:
                self.odd_lock.release()
            else:
                self.even_lock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.even_lock.acquire()
            printNumber(i)
            self.zero_lock.release()










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用三个锁（Lock）实现三线程有序输出。控制逻辑：
# 1. 初始状态：zero_lock 解锁（先打印 0），odd_lock 和 even_lock 加锁。
# 2. zero() 方法：获取 zero_lock 后打印 0，然后根据当前序号 i 的奇偶性：
#    - 若 i 为奇数，释放 odd_lock（让 odd 线程打印奇数）
#    - 若 i 为偶数，释放 even_lock（让 even 线程打印偶数）
# 3. odd() 方法：循环奇数 1, 3, 5, ...，每次获取 odd_lock 后打印当前奇数，然后释放 zero_lock。
# 4. even() 方法：循环偶数 2, 4, 6, ...，每次获取 even_lock 后打印当前偶数，然后释放 zero_lock。
# 5. 输出序列为：0, 1, 0, 2, 0, 3, 0, 4, ... = "01020304..."
#
# 时间复杂度: O(n) - 总共输出 2n 个数
# 空间复杂度: O(1) - 三个锁对象
#
# 关键点:
# - 三个线程的协调：zero 线程是"调度器"，决定下一个执行 odd 还是 even
# - 初始状态设置：只让 zero 先跑，odd 和 even 被阻塞等待
# - LeetCode 多线程类名与题目一致（ZeroEvenOdd），需实现三个方法
