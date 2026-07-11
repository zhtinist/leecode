"""
LeetCode #636 - Exclusive Time of Functions
中文题名：函数的独占时间
https://leetcode.com/problems/exclusive-time-of-functions/

On a single threaded CPU, we execute some functions.  Each function has
a unique id between `0` and `N-1`.

We store logs in timestamp order that describe when a function is entered or exited.

Each log is a string with this format: `"{function_id}:{"start" | "end"}:{timestamp}"`.
For example, `"0:start:3"` means the function with id
`0` started at the beginning of timestamp `3`.
`"1:end:2"` means the function with id `1` ended at
the end of timestamp `2`.

A function's exclusive time is the number of units of time spent in this
function.  Note that this does not include any recursive calls to
child functions.

The CPU is single threaded which means that only one function is being
executed at a given time unit.

Return the exclusive time of each function, sorted by their function id.

Example 1:

Input:
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3, 4]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 units of time and reaches the end of time 1.
Now function 1 starts at the beginning of time 2, executes 4 units of time and ends at time 5.
Function 0 is running again at the beginning of time 6, and also ends at the end of time 6, thus executing for 1 unit of time.
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.

Note:

`1 <= n <= 100`

Two functions won't start or end at the same time.

Functions will always log when they exit.

【中文翻译】
在单线程 CPU 上，我们执行一些函数。每个函数有唯一的 ID，范围在 `0` 到 `N-1` 之间。

我们按时间戳顺序存储了描述函数进入和退出的日志。

每个日志是一个字符串，格式为：`"{function_id}:{"start" | "end"}:{timestamp}"`。
例如，`"0:start:3"` 表示 ID 为 `0` 的函数在时间戳 `3` 的开始时启动。
`"1:end:2"` 表示 ID 为 `1` 的函数在时间戳 `2` 的结束时退出。

一个函数的独占时间是在该函数内部花费的时间单位数。
注意这不包括任何对子函数的递归调用。

CPU 是单线程的，这意味着任一给定时间单位内只有一个函数在执行。

返回每个函数按函数 ID 排序的独占时间。

示例 1：

输入：
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
输出：[3, 4]
解释：
函数 0 在时间 0 开始时启动，执行 2 个时间单位，在时间 1 结束时暂停。
现在函数 1 在时间 2 开始时启动，执行 4 个时间单位，在时间 5 时结束。
函数 0 在时间 6 开始时恢复运行，同时在时间 6 结束时结束，因此执行了 1 个时间单位。
所以函数 0 总共执行了 2 + 1 = 3 个时间单位，函数 1 总共执行了 4 个时间单位。

注意：

`1 <= n <= 100`

两个函数不会同时开始或结束。

函数退出时总是会有日志记录。
"""

from typing import List, Optional


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack: list[int] = []  # stores function IDs
        prev_time = 0

        for log in logs:
            fid, typ, time = log.split(':')
            fid, time = int(fid), int(time)

            if typ == 'start':
                if stack:
                    # Add elapsed time to the function currently on top of stack
                    result[stack[-1]] += time - prev_time
                stack.append(fid)
                prev_time = time
            else:  # 'end'
                # Function at top of stack ends; add its exclusive time
                result[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用栈模拟函数调用栈：
# 1. 维护一个栈存储正在执行的函数 ID，prev_time 记录上一个日志的时间点。
# 2. 遇到 start 日志时：
#    - 如果栈非空，栈顶函数从上个时间点到当前时间点的耗时加入结果。
#    - 将当前函数 ID 入栈，prev_time 设为当前时间。
# 3. 遇到 end 日志时：
#    - 栈顶函数（必须是当前日志的函数 ID）出栈，它的独占时间加上
#      (当前时间 - prev_time + 1)。
#    - prev_time 设为当前时间 + 1（因为 end 时间戳意味着整个时间单位被占用）。
#
# 时间复杂度: O(L) - L 为日志条数
# 空间复杂度: O(n) - 栈深度最多为 n（函数嵌套深度）
#
# 关键点:
# - end 日志时加 1：因为 end:t 表示该函数占满了时间戳 t
# - start 时不加 1：因为 start:t 表示在 t 开始时启动，还没消耗 t 这个时间单位
# - 栈模拟的是单线程 CPU 的函数调用栈
# - 栈顶始终是当前正在执行的函数
