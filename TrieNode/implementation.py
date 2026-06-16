class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count_prefix = 0
        self.ends_with = 0

# Space Complexity=O(L*N)        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    # Time Complexity= O(L),L=vg.length of word
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count_prefix+=1
        node.is_end = True
        node.ends_with+=1

        
    # Time Complexity= O(L),L=vg.length of word
    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    

    # Time Complexity= O(L),L=vg.length of word
    def stars_with(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    
    
    def count_wordsEqualto(self,words):
        node = self.root
        for char in words:
            if char not in node.children:
                return 0
            node = node.children[char]
        
        return node.ends_with
    
    def countWordsStrtingWith(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count_prefix

    def erase(self,words):
        node = self.root
        for char in words:
            if char not in node.children:
                return "No word found"
            else:
                node = node.children[char]
                node.count_prefix-=1
        node.ends_with-=1
        node.is_end = False