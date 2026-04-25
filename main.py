import sys
from autocomplete import Autocomplete

def main():
  filepath = sys.argv[1] if len(sys.argv) > 1 else "words.txt"
  try:
    engine = Autocomplete(filename)
  except:
    print(f"Could not find word list file '{filepath}'.")
    print("Usage: python main.py [path/to/words.txt]")
    sys.exit(1)

  engine.run()

if __name__ == "__main__":
  main()
      
