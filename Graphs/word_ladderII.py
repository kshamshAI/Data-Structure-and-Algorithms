'''26. Word Ladder II
Attempted
Hard
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
Constraints:
1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 500
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
The sum of all shortest transformation sequences does not exceed 105.'''
from typing import List
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        queue = deque()
        result=[]
        word_set = set(wordList)
        queue = deque()
        result=[]
        if endWord not in word_set:
            return []
        queue.append((beginWord,1))
        while queue:
            curr_word,level = queue.popleft()
            for _ in range(level):
                if curr_word == endWord:
                    return result
                for c in range(97,123):
                    ch = chr(c)
                    for i in range(len(curr_word)):
                        if ch == curr_word[i]:
                            continue
                        new_word = curr_word[:i]+ch+curr_word[i+1:]
                        if new_word in word_set:
                            queue.append((new_word,level+1))
                            result.append(queue)
                            word_set.remove(new_word)
        return []
                            
                

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().findLadders(beginWord,endWord,wordList))