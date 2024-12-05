## Represents a single node in the Trie
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False
    def add_child(self,char:str) -> 'TrieNode':
        if char not in self.children:
            self.children[char] = TrieNode()
        return self.children[char]

    def suffixes(self, suffix: str = '') -> list[str]:
        ## Recursive function that collects the suffix for
        ## all complete words below this point

        result = []

        if suffix and self.endOfWord:
            result.append(suffix)
        for char,child_node in self.children.items():
            result.extend(child_node.suffixes(suffix + char))
        return result
## Add a child node in this Trie

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self) -> None:
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        ## Add a word to the Trie
        curr = self.root
        for char in word:
            curr = curr.add_child(char)
        curr.endOfWord =True


    def find(self, prefix: str) -> TrieNode | None:
        ## Find the Trie node that represents this prefix
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return None
            curr = curr.children[char]
        return curr



MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Edge case: Empty string
print("Test case 2: Empty value")
prefixNode = MyTrie.find("")
if prefixNode:
    print('\n'.join(prefixNode.suffixes()))
else:
    print("Empty prefix not found")
# Expected output: False
# Normal case: Word present in the Trie
print("Test case 2: Valid prefix")
prefixNode = MyTrie.find("ant")
if prefixNode:
    print('\n'.join(prefixNode.suffixes()))
else:
    print(" prefix not found")
# Expected output: True

# Normal case: Word present in the Trie
if prefixNode:
    print('\n'.join(prefixNode.suffixes()))
else:
    print("Empty prefix not found")
# Expected output: True

# Normal case: Prefix of a word present in the Trie
prefixNode = MyTrie.find("fun")
if prefixNode:
    print('\n'.join(prefixNode.suffixes()))
else:
    print("Empty prefix not found")
# Expected output: True