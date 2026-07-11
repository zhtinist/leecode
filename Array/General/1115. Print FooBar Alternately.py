"""
LeetCode #1115 - Print FooBar Alternately
中文题名：交替打印FooBar
https://leetcode.com/problems/print-foobar-alternately/

Suppose you are given the following code:

class FooBar {
public void foo() {
for (int i = 0; i < n; i++) {
print("foo");
}
}

public void bar() {
for (int i = 0; i < n; i++) {
print("bar");
}
}
}

The same instance of `FooBar` will be passed to two different threads. Thread A
will call `foo()` while thread B will call `bar()`. Modify
the given program to output "foobar" n times.

Example 1:

Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar(). "foobar" is being output 1 time.

Example 2:

Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.

【中文翻译】
假设给你以下代码：

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}

相同的 FooBar 实例将被传递给两个不同的线程。线程 A 将调用 foo()，而线程 B 将调用 bar()。修改给定的程序，使其输出 "foobar" n 次。

示例 1：

输入：n = 1
输出："foobar"
解释：有两个线程被异步启动。其中一个调用 foo()，另一个调用 bar()。"foobar" 被输出 1 次。

示例 2：

输入：n = 2
输出："foobarfoobar"
解释："foobar" 被输出 2 次。
"""

from typing import List, Optional


class FooBar:
    def __init__(self, n):
        self.n = n
        from threading import Lock
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用两个锁（Lock）实现线程交替执行：
# 1. foo_lock 初始为解锁状态，bar_lock 初始为加锁状态。
# 2. foo() 方法：先获取 foo_lock，打印 "foo"，然后释放 bar_lock。
# 3. bar() 方法：先获取 bar_lock，打印 "bar"，然后释放 foo_lock。
# 4. 循环 n 次后，两个线程交替输出 "foo" 和 "bar"，形成 "foobar" 重复 n 次的效果。
# 也可以用 threading.Semaphore(0) 和 threading.Semaphore(1) 实现类似效果。
#
# 时间复杂度: O(n) - 每个方法循环 n 次
# 空间复杂度: O(1) - 只使用了两个锁对象
#
# 关键点:
# - 使用两个锁形成"乒乓"效应：A 释放 B 的锁，B 释放 A 的锁
# - 初始状态：foo 的锁可用，bar 的锁被占用，确保 foo 先执行
# - LeetCode 多线程题需要正确使用 threading 同步原语
