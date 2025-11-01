"""
208. Implement Trie (Prefix Tree)
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a
dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
* void insert(String word) Inserts the string word into the trie.
* boolean search(String word) Returns true if the string word is in the trie
(i.e., was inserted before), and false otherwise.
* boolean startsWith(String prefix) Returns true if there is a previously inserted string word
that has the prefix `prefix`, and false otherwise.

Constraints:
* 1 <= word.length, prefix.length <= 2000
* word and prefix consist only of lowercase English letters.
* At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""

class Constants:
    LOWER_ALPHA_COUNT: int = 26
    ORD_A_LOWER: int = 97


class TrieNode:

    def __init__(self) -> None:
        self.children: list["TrieNode | None"] = [None] * Constants.LOWER_ALPHA_COUNT
        self.is_end_of_word: bool = False


class Trie:
    def __init__(self):
        self.root: TrieNode = TrieNode()

    def _find_index(self, char: str) -> int:
        return ord(char) - Constants.ORD_A_LOWER

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            index = self._find_index(char)
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = self._find_index(char)
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            index = self._find_index(char)
            if node.children[index] is None:
                return False
            node = node.children[index]
        return True
