"""
LeetCode #1195 - Fizz Buzz Multithreaded
中文题名：交替打印字符串
https://leetcode.com/problems/fizz-buzz-multithreaded/

Write a program that outputs the string representation of numbers from 1 to n,
however:

If the number is divisible by 3, output "fizz".

If the number is divisible by 5, output "buzz".

If the number is divisible by both 3 and 5, output "fizzbuzz".

For example, for `n = 15`, we output: `1, 2, fizz, 4, buzz, fizz,
7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz`.

Suppose you are given the following code:

class FizzBuzz {
public FizzBuzz(int n) { ... }               // constructor
public void fizz(printFizz) { ... }          // only output "fizz"
public void buzz(printBuzz) { ... }          // only output "buzz"
public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
public void number(printNumber) { ... }      // only output the numbers
}

Implement a multithreaded version of `FizzBuzz` with four
threads. The same instance of `FizzBuzz` will be passed to four different
threads:

Thread A will call `fizz()` to check for divisibility of 3 and
outputs `fizz`.

Thread B will call `buzz()` to check for divisibility of 5 and
outputs `buzz`.

Thread C will call `fizzbuzz()` to check for divisibility of 3 and 5 and
outputs `fizzbuzz`.

Thread D will call `number()` which should only output the numbers.

【中文翻译】
编写一个程序，输出从 1 到 n 数字的字符串表示，但是：

如果数字是 3 的倍数，输出 "fizz"。
如果数字是 5 的倍数，输出 "buzz"。
如果数字同时是 3 和 5 的倍数，输出 "fizzbuzz"。

例如，对于 n = 15，输出：1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz。

假设有下面的代码：

class FizzBuzz {
  public FizzBuzz(int n) { ... }               // 构造函数
  public void fizz(printFizz) { ... }          // 只输出 "fizz"
  public void buzz(printBuzz) { ... }          // 只输出 "buzz"
  public void fizzbuzz(printFizzBuzz) { ... }  // 只输出 "fizzbuzz"
  public void number(printNumber) { ... }      // 只输出数字
}

实现一个多线程版本的 FizzBuzz，使用四个线程。同一个 FizzBuzz 实例会被传递给四个不同的线程：

线程 A 将调用 fizz() 来判断是否能被 3 整除并输出 fizz。
线程 B 将调用 buzz() 来判断是否能被 5 整除并输出 buzz。
线程 C 将调用 fizzbuzz() 来判断是否能被 3 和 5 整除并输出 fizzbuzz。
线程 D 将调用 number() 来输出数字。

"""

from typing import List, Optional, Callable
from threading import Lock


class Solution:
    """
    LeetCode expects class FizzBuzz, but this file uses Solution.
    The four methods below are the required interface.
    """
    def __init__(self, n: int = 1):
        self.n = n
        self.i = 1
        self.lock = Lock()

    def fizz(self, printFizz: Callable[[], None]) -> None:
        while self.i <= self.n:
            with self.lock:
                if self.i <= self.n and self.i % 3 == 0 and self.i % 5 != 0:
                    printFizz()
                    self.i += 1

    def buzz(self, printBuzz: Callable[[], None]) -> None:
        while self.i <= self.n:
            with self.lock:
                if self.i <= self.n and self.i % 5 == 0 and self.i % 3 != 0:
                    printBuzz()
                    self.i += 1

    def fizzbuzz(self, printFizzBuzz: Callable[[], None]) -> None:
        while self.i <= self.n:
            with self.lock:
                if self.i <= self.n and self.i % 15 == 0:
                    printFizzBuzz()
                    self.i += 1

    def number(self, printNumber: Callable[[int], None]) -> None:
        while self.i <= self.n:
            with self.lock:
                if self.i <= self.n and self.i % 3 != 0 and self.i % 5 != 0:
                    printNumber(self.i)
                    self.i += 1










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用互斥锁(Lock)实现四个线程之间的同步协调。
# 核心思想：用一个共享计数器 self.i（从 1 到 n），四个线程轮流检查当前数字是否满足自己的条件。
# - fizz 线程：检查 i % 3 == 0 and i % 5 != 0
# - buzz 线程：检查 i % 5 == 0 and i % 3 != 0
# - fizzbuzz 线程：检查 i % 15 == 0
# - number 线程：检查 i % 3 != 0 and i % 5 != 0
#
# 每个线程在 while 循环中不断尝试获取锁，获取到锁后：
# 1. 检查 i 是否已超过 n（结束条件）
# 2. 如果当前数字满足自己的条件，则调用对应的打印函数，并将 i 加 1
# 3. 释放锁（通过 with 语句自动完成）
#
# 这种实现是忙等(Busy-Waiting)方式，线程会不断尝试获取锁直到条件满足。
# 更优的方案可以使用 Condition 或 4 个 Semaphore 按顺序唤醒对应线程。
#
# 时间复杂度: O(n) - 每个线程最多循环 n 次，共享的 i 从 1 递增到 n
# 空间复杂度: O(1) - 仅使用常数个变量
#
# 关键点:
# - 四个线程通过共享锁实现互斥访问，确保同一时刻只有一个线程操作计数器
# - 每个线程只处理满足自己条件的数字，不满足条件时释放锁让其他线程尝试
# - 使用 with self.lock 确保锁的正确获取和释放，避免死锁
# - 在 with 块内再次检查 self.i <= self.n 防止超出范围（TOCTOU 问题）
# - 这种忙等方式在 LeetCode 测试中可通过，但生产中建议使用信号量或条件变量减少 CPU 空转
