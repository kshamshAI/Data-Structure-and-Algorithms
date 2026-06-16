class TrieNode:
    def __init__(self):
        self.children ={}
        self.end = False
        self.count_prefix = 0
        self.count_endsWith = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        count = 0              
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                count+=1
            node = node.children[char]
            node.count_prefix+=1
        node.end = True
        node.count_endsWith+=1
        return count
    

def countDistinctSubstrings1(s):
    # Write your code here
   
    n = len(s)
    trie = Trie()
    ans =0
    for i in range(n):
        ans+=trie.insert(s[i:])
    return ans+1


def countDistinctSubstrings(s):
    # Write your code here
    
    my_set = set()
    n = len(s)
    for i in range(n):
        sub_string = ''
        for j in range(i,n):
            sub_string+=s[j]
            my_set.add(sub_string)
    return len(my_set)+1
s= 'abab'
s1=['sds'
,'abc',
'aa',
'abab']
print(countDistinctSubstrings(s))
for i in range(len(s1)):
    print(countDistinctSubstrings1(s1[i]))