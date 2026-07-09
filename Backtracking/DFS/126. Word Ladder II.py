"""
LeetCode #126 - Word Ladder II
https://leetcode.com/problems/word-ladder-ii/

A transformation sequence from word beginWord to word endWord using a dictionary
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList.
- beginWord does not appear in wordList.
- sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return all
the shortest transformation sequences from beginWord to endWord, or an empty list
if no such sequence exists.

Example 1:
    Input: beginWord = "hit", endWord = "cog",
           wordList = ["hot","dot","dog","lot","log","cog"]
    Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

Example 2:
    Input: beginWord = "hit", endWord = "cog",
           wordList = ["hot","dot","dog","lot","log"]
    Output: []

Constraints:
    1 <= beginWord.length <= 5
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
    All words in wordList are unique.
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        graph = defaultdict(list)
        distance = {beginWord: 0}
        queue = deque([beginWord])
        found = False

        while queue and not found:
            level_size = len(queue)
            for _ in range(level_size):
                word = queue.popleft()
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue
                        next_word = word[:i] + c + word[i + 1:]
                        if next_word not in word_set:
                            continue
                        if next_word not in distance:
                            distance[next_word] = distance[word] + 1
                            queue.append(next_word)
                        if distance[next_word] == distance[word] + 1:
                            graph[word].append(next_word)
                if word == endWord:
                    found = True

        if endWord not in distance:
            return []

        result = []

        def backtrack(path: List[str]) -> None:
            if path[-1] == endWord:
                result.append(path[:])
                return
            for neighbor in graph[path[-1]]:
                if distance[neighbor] == distance[path[-1]] + 1:
                    path.append(neighbor)
                    backtrack(path)
                    path.pop()

        backtrack([beginWord])
        return result
