"""
LeetCode #1396 - Design Underground System
中文题名：设计地铁系统
https://leetcode.com/problems/design-underground-system/

Implement the class `UndergroundSystem` that supports three methods:

1.` checkIn(int id, string stationName, int t)`

A customer with id card equal to `id`, gets in the station `stationName`
at time `t`.

A customer can only be checked into one place at a time.

2.` checkOut(int id, string stationName, int t)`

A customer with id card equal to `id`, gets out from the station
`stationName` at time `t`.

3. `getAverageTime(string startStation, string endStation)`

Returns the average time to travel between the `startStation` and the
`endStation`.

The average time is computed from all the previous traveling from `startStation`
to `endStation` that happened directly.

Call to `getAverageTime` is always valid.

You can assume all calls to `checkIn` and `checkOut` methods
are consistent. That is, if a customer gets in at time
t1 at some station, then it gets out at time
t2 with t2 >
t1. All events happen in chronological order.

Example 1:

Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output
[null,null,null,null,null,null,null,14.0,11.0,null,11.0,null,12.0]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);
undergroundSystem.checkOut(27, "Waterloo", 20);
undergroundSystem.checkOut(32, "Cambridge", 22);
undergroundSystem.getAverageTime("Paradise", "Cambridge");       // return 14.0. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.0. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.0
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.0
undergroundSystem.checkOut(10, "Waterloo", 38);
undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 12.0

Constraints:

There will be at most `20000` operations.

`1 <= id, t <= 10^6`

All strings consist of uppercase, lowercase English letters and digits.

`1 <= stationName.length <= 10`

Answers within `10^-5` of the actual value will be accepted
as correct.

【中文翻译】

实现 UndergroundSystem 类，支持三种方法：

1. checkIn(int id, string stationName, int t)
   卡号为 id 的乘客在时间 t 进入站台 stationName。
   乘客一次只能在一个地方入站。

2. checkOut(int id, string stationName, int t)
   卡号为 id 的乘客在时间 t 离开站台 stationName。

3. getAverageTime(string startStation, string endStation)
   返回从 startStation 到 endStation 的平均旅行时间。
   平均时间根据所有从 startStation 直接到 endStation 的历史记录计算。
   对 getAverageTime 的调用始终有效。

可以假设所有 checkIn 和 checkOut 的调用是一致的。即如果乘客在时间 t1 于某个站点入站，则在时间 t2 于某站点出站，且 t2 > t1。所有事件按时间顺序发生。

示例 1：
输入：
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
输出：
[null,null,null,null,null,null,null,14.0,11.0,null,11.0,null,12.0]
解释：
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);
undergroundSystem.checkOut(27, "Waterloo", 20);
undergroundSystem.checkOut(32, "Cambridge", 22);
undergroundSystem.getAverageTime("Paradise", "Cambridge");  // 返回 14.0。只有一次从 "Paradise"（时间 8）到 "Cambridge"（时间 22）的旅行
undergroundSystem.getAverageTime("Leyton", "Waterloo");     // 返回 11.0。有两次从 "Leyton" 到 "Waterloo" 的旅行，id=45 从 t=3 到 t=15，id=27 从 t=10 到 t=20。平均时间 = ((15-3)+(20-10))/2 = 11.0
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");     // 返回 11.0
undergroundSystem.checkOut(10, "Waterloo", 38);
undergroundSystem.getAverageTime("Leyton", "Waterloo");     // 返回 12.0

约束条件：
最多 20000 次操作。
1 <= id, t <= 10^6
所有字符串由大小写英文字母和数字组成。
1 <= stationName.length <= 10
答案与实际值误差在 10^-5 以内即视为正确。
"""

from typing import List, Optional


class UndergroundSystem:

    def __init__(self):
        # 记录入站信息：{id: (stationName, t)}
        self.check_in = {}
        # 记录行程统计：{(startStation, endStation): (total_time, count)}
        self.travel_stats = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in[id]
        travel_time = t - start_time
        key = (start_station, stationName)

        if key not in self.travel_stats:
            self.travel_stats[key] = (travel_time, 1)
        else:
            total_time, count = self.travel_stats[key]
            self.travel_stats[key] = (total_time + travel_time, count + 1)

        # 删除入站记录，释放空间
        del self.check_in[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_stats[(startStation, endStation)]
        return total_time / count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用两个哈希表：
# 1. check_in: 记录当前在途的乘客信息 {id: (stationName, t)}
# 2. travel_stats: 记录历史行程统计 {(start, end): (total_time, count)}
# checkIn: 存储乘客的入站信息
# checkOut: 计算旅行时间，更新统计，删除入站记录
# getAverageTime: 返回 total_time / count
#
# 时间复杂度: O(1)  所有操作均为 O(1)
# 空间复杂度: O(N)  N 为乘客数量和行程种类
#
# 关键点:
# - 使用元组 (startStation, endStation) 作为行程的复合键
# - 存储 (total_time, count) 而非单独存储每次行程时间，节省空间
# - checkOut 后删除 check_in 记录既节省空间又防止重复出站










