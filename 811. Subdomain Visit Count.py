"""
LeetCode #811 - Subdomain Visit Count
中文题名：子域名访问计数
https://leetcode.com/problems/subdomain-visit-count/

A website domain like "discuss.leetcode.com" consists of various subdomains. At the
top level, we have "com", at the next level, we have "leetcode.com", and
at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com",
we will also visit the parent domains "leetcode.com" and "com"
implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits
this domain received), followed by a space, followed by the address. An example of a
count-paired domain might be "9001 discuss.leetcode.com".

We are given a list `cpdomains` of count-paired domains. We would like a list of
count-paired domains, (in the same format as the input, and in any order), that explicitly
counts the number of visits to each subdomain.

Example 1:
Input:
["9001 discuss.leetcode.com"]
Output:
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation:
We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain "leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

Example 2:
Input:
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output:
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation:
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

Notes:

The length of `cpdomains` will not exceed `100`.

The length of each domain name will not exceed `100`.

Each address will have either 1 or 2 "." characters.

The input count in any count-paired domain will not exceed `10000`.

The answer output can be returned in any order.

【中文翻译】
像 "discuss.leetcode.com" 这样的网站域名由多个子域名组成。最顶层是 "com"，下一层是 "leetcode.com"，最底层是 "discuss.leetcode.com"。当我们访问像 "discuss.leetcode.com" 这样的域名时，我们也会隐式地访问父域名 "leetcode.com" 和 "com"。

现在，将"计数配对域名"定义为一个计数（表示该域名收到的访问次数），后跟一个空格，再跟地址。一个计数配对域名的示例是 "9001 discuss.leetcode.com"。

给定一个计数配对域名列表 `cpdomains`。我们需要一个计数配对域名列表（格式与输入相同，顺序任意），明确记录每个子域名的访问次数。

示例 1：
输入：["9001 discuss.leetcode.com"]
输出：["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
解释：只有一个网站域名 "discuss.leetcode.com"。如上所述，子域名 "leetcode.com" 和 "com" 也会被访问。所以它们都会被访问 9001 次。

示例 2：
输入：["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
输出：["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
解释：我们将访问 "google.mail.com" 900 次，"yahoo.com" 50 次，"intel.mail.com" 1 次，"wiki.org" 5 次。对于子域名，我们将访问 "mail.com" 900 + 1 = 901 次，"com" 900 + 50 + 1 = 951 次，"org" 5 次。

注意：
`cpdomains` 的长度不超过 `100`。
每个域名的长度不超过 `100`。
每个地址将包含 1 或 2 个 "." 字符。
每个计数配对域名的输入计数不超过 `10000`。
答案可以按任意顺序返回。
"""

from typing import List, Optional


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        from collections import defaultdict
        counts = defaultdict(int)

        for cpdomain in cpdomains:
            cnt_str, domain = cpdomain.split()
            cnt = int(cnt_str)

            # Add count to full domain and all subdomains
            parts = domain.split('.')
            for i in range(len(parts)):
                sub = '.'.join(parts[i:])
                counts[sub] += cnt

        return [f"{cnt} {domain}" for domain, cnt in counts.items()]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用哈希表（defaultdict）统计每个域名和子域名的访问次数。
# 对于每个计数配对域名：
#   1. 按空格分割得到计数值和完整域名。
#   2. 将完整域名按 '.' 分割成各部分。
#   3. 从每个部分开始，生成该级别的子域名，
#      例如 "discuss.leetcode.com" 生成：
#      "discuss.leetcode.com", "leetcode.com", "com"
#   4. 将计数值累加到哈希表中对应域名。
# 最后将哈希表中的键值对格式化为列表返回。
#
# 时间复杂度: O(N * M) - 其中 N 是 cpdomains 长度，
#   M 是域名部分的平均长度（生成子串操作）
# 空间复杂度: O(K) - 其中 K 是不同子域名的数量
#
# 关键点:
# - defaultdict 自动初始化为 0，方便累加
# - 用 split('.') 和 join 生成各级子域名
# - 输出格式要求完全按输入格式
