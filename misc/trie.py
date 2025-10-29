LOWERCASE_ALPHA_COUNT = 26
ORD_LOWER_A = 97


class TrieNode:
    def __init__(self, is_end_of_word: bool = False) -> None:
        self.children: list[TrieNode | None] = [None] * LOWERCASE_ALPHA_COUNT
        self.is_end_of_word = is_end_of_word


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, key: str) -> None:
        curr = self.root
        for char in key:
            index = ord(char) - ORD_LOWER_A
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end_of_word = True

    def search(self, key: str) -> bool:
        curr = self.root
        for char in key:
            index = ord(char) - ORD_LOWER_A
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.is_end_of_word
