class Solution:
  def intToRoman(self, num: int) -> str:
      values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
      symbols = {1 : "I", 4: "IV", 5: "V", 9 : "IX",10: "X", 40 : "XL", 50: "L", 90 : "XC", 100: "C", 400 : "CD",500: "D", 900: "CM",1000: "M"}
      i = 0
      w = []
      while i < len(values):
          if num >= values[i]:
              w.append(symbols[values[i]])
              num -= values[i]
          else:
              i += 1
      return "".join(w)

