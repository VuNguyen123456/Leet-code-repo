class TrieNode:
  def __init__(self):
      self.children = {}
      self.isEnd = False

class WordDictionary:

  def __init__(self):
      self.root = TrieNode()

  def addWord(self, word: str) -> None:
      cur = self.root
      for c in word:
          if c not in cur.children:
              cur.children[c] = TrieNode()
          cur =  cur.children[c]
      cur.isEnd = True


  def search(self, word: str) -> bool:
      def dfs(j, root):
          cur = root
          for i in range(j, len(word)):
              if word[i] == ".":
                  for child in cur.children.values():
                      if dfs(i + 1, child): #child is . but here it's getting replace by: a , b, c, d, .... anything that's the child of the the thing above this wildcard ".": 
                          return True
                  return False 
              else:
                  if word[i] not in cur.children:
                      return False
                  cur = cur.children[word[i]]
          return cur.isEnd
      return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)