# https://albertauyeung.github.io/2020/06/15/python-trie.html

from __future__ import annotations
from collections import defaultdict
from typing import DefaultDict, List, Tuple


class TrieNode:
    """ A node in the trie structure """

    def __init__(self, char: str) -> None:
        self.char = char
        self.eow = False
        self.counter = 0
        self.children: DefaultDict[str, TrieNode] = defaultdict()


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # char not found, create new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.eow = True
        node.counter += 1

    # todo: delete word

    def dfs(self, node: TrieNode, prefix: str, output: List[Tuple[str, int]]) -> None:
        if node.eow:
            output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char, output)

    def query(self, x: str) -> List[Tuple[str, int]]:
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        output: List[Tuple[str, int]] = []
        self.dfs(node, x[:-1], output)
        # words with most count sorted in front
        return sorted(output, key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    t = Trie()
    t.insert("was")
    t.insert("word")
    t.insert("war")
    t.insert("what")
    t.insert("where")
    print(t.query("wh"))
