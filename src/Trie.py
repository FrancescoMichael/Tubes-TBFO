import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode.TrieNode()

    def insertToken(self, token):
        tempNode = self.root
        for char in token:
            if char not in tempNode.child:
                tempNode.child[char] = TrieNode.TrieNode()
            tempNode = tempNode.child[char]
        tempNode.endOfWord = True

    def searchToken(self, token):
        tempNode = self.root
        for char in token:
            if char not in tempNode.child:
                return False
            tempNode = tempNode.child[char]
        return tempNode.endOfWord