class Loader:
  def load(self, filepath: str) -> list[str]:
    words = []
    with open(filepath, "r", encoding="utf-8") as file:
      for line in file:
        word = line.strip()
        if word:
          words.append(word)
    return words
