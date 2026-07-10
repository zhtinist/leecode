"""
LeetCode #175 - Combine Two Tables
https://leetcode.com/problems/combine-two-tables/

Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key (column with unique values) for this table.

Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key for this table.

Each row in this table contains information about the city and state of a
person with Id = PersonId.

Write a solution to report the first name, last name, city, and state of each
person in the Person table. If the address of a personId is not present in the
Address table, report null instead.

Return the result table in any order.

Example 1:
    Input:
    Person table:
    +----------+----------+-----------+
    | PersonId | LastName | FirstName |
    +----------+----------+-----------+
    | 1        | Wang     | Allen     |
    | 2        | Alice    | Bob       |
    +----------+----------+-----------+
    Address table:
    +-----------+----------+---------------+------------+
    | AddressId | PersonId | City          | State      |
    +-----------+----------+---------------+------------+
    | 1         | 2        | New York City | New York   |
    | 2         | 3        | Leetcode      | California |
    +-----------+----------+---------------+------------+
    Output:
    +-----------+----------+---------------+----------+
    | FirstName | LastName | City          | State    |
    +-----------+----------+---------------+----------+
    | Allen     | Wang     | Null          | Null     |
    | Bob       | Alice    | New York City | New York |
    +-----------+----------+---------------+----------+
    Explanation: There is no address in the address table for the personId = 1
    so we return null in their city and state.

Constraints:
    Person table has at most 10^4 rows.
    Address table has at most 10^4 rows.
"""


class Solution:
    def query(self) -> str:
        return """
SELECT
    p.FirstName,
    p.LastName,
    a.City,
    a.State
FROM Person AS p
LEFT JOIN Address AS a
    ON p.PersonId = a.PersonId
"""
