class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      res = []
      dic = {}
      for i in strs:
          w = sorted(list(i))
          letter = ''.join(w)
          if letter not in dic:
              dic[letter] = [i]
          else:
              dic[letter].append(i)

      for i in dic:
          res.append(dic[i])

      return res