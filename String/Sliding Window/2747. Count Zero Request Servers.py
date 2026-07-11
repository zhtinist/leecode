"""
LeetCode #2747 - Count Zero Request Servers
统计没有收到请求的服务器数目
https://leetcode.cn/problems/count-zero-request-servers/

给你一个整数 `n` ，表示服务器的总数目，再给你一个下标从 0 开始的 二维 整数数组 `logs` ，其中 `logs[i] = [server_id, time]` 表示 id 为 `server_id` 的服务器在 `time` 时收到了一个请求。
同时给你一个整数 `x` 和一个下标从 0 开始的整数数组 `queries`  。
请你返回一个长度等于 `queries.length` 的数组 `arr` ，其中 `arr[i]` 表示在时间区间 `[queries[i] - x, queries[i]]` 内没有收到请求的服务器数目。
注意时间区间是个闭区间。

示例 1：
输入：n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11] 输出：[1,2] 解释： 对于 queries[0]：id 为 1 和 2 的服务器在区间 [5, 10] 内收到了请求，所以只有服务器 3 没有收到请求。 对于 queries[1]：id 为 2 的服务器在区间 [6,11] 内收到了请求，所以 id 为 1 和 3 的服务器在这个时间段内没有收到请求。
示例 2：
输入：n = 3, logs = [[2,4],[2,1],[1,2],[3,1]], x = 2, queries = [3,4] 输出：[0,1] 解释： 对于 queries[0]：区间 [1, 3] 内所有服务器都收到了请求。 对于 queries[1]：只有 id 为 3 的服务器在区间 [2,4] 内没有收到请求。

提示：
`1 <= n <= 10^5`
`1 <= logs.length <= 10^5`
`1 <= queries.length <= 10^5`
`logs[i].length == 2`
`1 <= logs[i][0] <= n`
`1 <= logs[i][1] <= 10^6`
`1 <= x <= 10^5`
`x < queries[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda e: e[1])

        q_with_idx = sorted([(q, i) for i, q in enumerate(queries)])
        m = len(queries)
        ans = [0] * m

        cnt = {}
        left = 0
        right = 0
        for q, idx in q_with_idx:
            L = q - x
            R = q
            while right < len(logs) and logs[right][1] <= R:
                sid = logs[right][0]
                cnt[sid] = cnt.get(sid, 0) + 1
                right += 1
            while left < len(logs) and logs[left][1] < L:
                sid = logs[left][0]
                cnt[sid] -= 1
                if cnt[sid] == 0:
                    del cnt[sid]
                left += 1
            ans[idx] = n - len(cnt)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Sorting, Sliding Window
#
# 解题思路:
# 离线查询 + 滑动窗口。将所有查询按时间排序，logs 也按时间排序。
# 对于每个查询 [L, R]，维护一个滑动窗口包含时间在 [L, R] 内的所有日志。
# 用哈希表记录窗口内有哪些服务器收到了请求，则没有收到请求的服务器数量 = n - len(cnt)。
# 按查询顺序返回答案。
#
# 时间复杂度: O((m+k) log(m+k)) 其中 m=len(queries), k=len(logs)，排序占主导
# 空间复杂度: O(n + m) 哈希表和答案数组
#
# 关键点:
# - 离线处理：排序查询后按时间顺序滑动窗口，避免对每个查询重建区间
# - 双指针维护时间窗口 [q-x, q]
# - 哈希表 key 为 server_id，value 为出现次数
