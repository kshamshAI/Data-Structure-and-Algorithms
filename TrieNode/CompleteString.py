'''Problem statement
Ninja developed a love for arrays and strings so this time his teacher gave him an array of strings, ‘A’ of size ‘N’. Each element of this array is a string. The teacher taught Ninja about prefixes in the past, so he wants to test his knowledge.
A string is called a complete string if every prefix of this string is also present in the array ‘A’. Ninja is challenged to find the longest complete string in the array ‘A’.If there are multiple strings with the same length, return the lexicographically smallest one and if no string exists, return "None".
Note :
String ‘P’ is lexicographically smaller than string ‘Q’, if : 
1. There exists some index ‘i’ such that for all ‘j’ < ‘i’ , ‘P[j] = Q[j]’ and ‘P[i] < Q[i]’. E.g. “ninja” < “noder”.
2. If ‘P’ is a prefix of string ‘Q’, e.g. “code” < “coder”.
Example :
N = 4
A = [ “ab” , “abc” , “a” , “bp” ] 
Explanation : 
Only prefix of the string “a” is “a” which is present in array ‘A’. So, it is one of the possible strings.
Prefixes of the string “ab” are “a” and “ab” both of which are present in array ‘A’. So, it is one of the possible strings.
Prefixes of the string “bp” are “b” and “bp”. “b” is not present in array ‘A’. So, it cannot be a valid string.
Prefixes of the string “abc” are “a”,“ab” and “abc” all of which are present in array ‘A’. So, it is one of the possible strings.
We need to find the maximum length string, so “abc” is the required string.'''

from sys import *
from collections import *
from math import *


from typing import *

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.count_prefix = 0
        self.count_endWith = 0
class Trie:
    def __init__(self):
        self.root =  TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count_prefix+=1
        node.count_endWith+=1
        node.end = True

    def check_prefixes(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            if node.end == False:
                return False 
        return True


def completeString(n: int, a: List[str])-> str:
    trie = Trie()
    best_word =''
    for word in a:
        trie.insert(word)
    for word in a:    
        if trie.check_prefixes(word):
            if len(word)>len(best_word) or len(word)==len(best_word) and best_word>word:
                best_word = word
    if best_word == '':
        return "None"
    return best_word

    
      

    
   
    


    
   
    