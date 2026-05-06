'''3. Longest Substring Without Repeating Characters
Solved
Medium
Given a string s, find the length of the longest substring without duplicate characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.'''




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = {}
        left = 0
        right = 0
        n = len(s)
        maxi = 0
        while right < n:
            if s[right] in my_dict:
                left = max(left,my_dict[s[right]]+1)
            maxi = max(maxi,right-left+1)
            my_dict[s[right]] = right
            right +=1
        return maxi

s = "pwwkew"
print(f'Output: {Solution().lengthOfLongestSubstring(s)}')
            
        