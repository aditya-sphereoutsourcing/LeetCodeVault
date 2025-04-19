"""
LeetCode Problem #208: Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/

Date: April 5, 2025

Problem Description:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and 
retrieve keys in a dataset of strings. There are various applications of this data structure, such as 
autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Time Complexity:
- insert: O(m) - Where m is the length of the word.
- search: O(m) - Where m is the length of the word.
- startsWith: O(m) - Where m is the length of the prefix.

Space Complexity: O(N * M) - Where N is the number of words and M is the average length of words.
"""

class TrieNode:
    def __init__(self):
        # Initialize a dictionary to store children nodes
        # Keys are characters, values are TrieNode objects
        self.children = {}
        
        # Flag to mark the end of a word
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # The root node of the trie
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # Start from the root node
        current = self.root
        
        # Traverse the trie for each character in the word
        for char in word:
            # If the character is not in the current node's children,
            # create a new node for this character
            if char not in current.children:
                current.children[char] = TrieNode()
            
            # Move to the child node
            current = current.children[char]
        
        # Mark the end of the word
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # Start from the root node
        current = self.root
        
        # Traverse the trie for each character in the word
        for char in word:
            # If the character is not found, the word does not exist in the trie
            if char not in current.children:
                return False
            
            # Move to the child node
            current = current.children[char]
        
        # Return whether this is the end of a word
        # If true, the word exists in the trie
        # If false, this is just a prefix of another word
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # Start from the root node
        current = self.root
        
        # Traverse the trie for each character in the prefix
        for char in prefix:
            # If the character is not found, no word with this prefix exists
            if char not in current.children:
                return False
            
            # Move to the child node
            current = current.children[char]
        
        # If we've made it here, we found the prefix in the trie
        return True


# Alternative implementation using an array of fixed size for English lowercase letters
"""
class TrieNode:
    def __init__(self):
        # Initialize an array of 26 children nodes (for lowercase English letters)
        self.children = [None] * 26
        
        # Flag to mark the end of a word
        self.is_end_of_word = False
        
        # Helper method to get the index of a character (a-z)
        # where 'a' is 0, 'b' is 1, ..., 'z' is 25
        def _char_to_index(self, char):
            return ord(char) - ord('a')

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        current = self.root
        
        for char in word:
            index = self._char_to_index(char)
            
            # If the character's node doesn't exist, create it
            if not current.children[index]:
                current.children[index] = TrieNode()
            
            # Move to the child node
            current = current.children[index]
        
        # Mark the end of the word
        current.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        current = self.root
        
        for char in word:
            index = self._char_to_index(char)
            
            # If the character's node doesn't exist, the word doesn't exist
            if not current.children[index]:
                return False
            
            # Move to the child node
            current = current.children[index]
        
        # Return whether this is the end of a word
        return current.is_end_of_word
    
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        
        for char in prefix:
            index = self._char_to_index(char)
            
            # If the character's node doesn't exist, no word with this prefix exists
            if not current.children[index]:
                return False
            
            # Move to the child node
            current = current.children[index]
        
        # If we've made it here, we found the prefix in the trie
        return True
    
    # Helper method to get the index of a character (a-z)
    def _char_to_index(self, char):
        return ord(char) - ord('a')
"""


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)