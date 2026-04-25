from loader import Loader
from trie import Trie

class Autocomplete:
  def __init__(self, filepath: str):
    loader = Loader()
    words = loader.load(filepath)
    self.trie = Trie()
    for word in words:
      self.trie.insert(word)

  def suggest(self, prefix: str) -> list[str]:
    return self.trie.search(prefix)

  def run(self) -> None:
    print("Autocomplete Search Engine")
    print("Type a prefix to search. Press enter with no input to quit.\n")
    
    while True:
      prefix = input("Enter prefix: ").strip()
      if not prefix:
        print("Goodbye.")
        break
      results = self.suggest(prefix)
      if not results:
        print(f' No matches found for "{prefix}".\n')
      else:
        for word in results:
          print(f" {word}")
        print(f" ({len(results)} match{'es' if len(results) != 1 else ''} found)\n")
