from trie_node import TrieNode

def __init__(self):
  self.root = TrieNode()

def insert(self, word: str) -> None:
  current = self.root
  for char in word.lower():
    if char not in current.children:
      current.children[char] = TrieNode()
    current = current.children[char]
  current.is_end_of_word = True

def search(self, prefix: str) -> list[str]:
  current = self.root
  for char in prefix.lower():
    if char not in current.children:
      return []
    current = current.children[char]
  matches = []
  self._collect_words(current, prefix.lower(), matches)
  return sorted(matches)

def _collect_words(self, node: TrieNode, current_word: str, matches: list[str]) -> None:
  if node.is_end_of_word:
    matches.append(current_word)
  for char, child_node in node.children.items():
    self._collect_words(child_node, current_word + char, matches)
