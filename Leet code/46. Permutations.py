class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
      ## Iterations:
      # Basically start with empty list, insert number in according to list
      # For every new number insert at a new position according to the current list
      # Ex: [] -> [1] -> [2,1], [1,2] -> [3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2], [1,2,3]

      # perms = [[]]

      # for n in nums:
      #     new_perms = []
      #     for p in perms:
      #         for i in range(len(p) + 1):
      #             p_copy = p.copy()
      #             p_copy.insert(i, n)
      #             new_perms.append(p_copy)
      #     perms = new_perms
      # return perms

      ## Backtrack
      if len(nums) == 1:
          return [nums[:]]
      result = []

      for _ in range(len(nums)):
          n = nums.pop(0)
          perms = self.permute(nums)
          for p in perms:
              p.append(n)

          result.extend(perms)
          nums.append(n)

      return result


# permute([1,2,3])
# ├── pick 1 → permute([2,3])
# │   ├── pick 2 → permute([3]) → [3] → append 2 → [3,2]
# │   └── pick 3 → permute([2]) → [2] → append 3 → [2,3]
# │   → add 1 → [3,2,1], [2,3,1]
# ├── pick 2 → permute([1,3])
# │   → [3,1] → [3,1,2], [1,3,2]
# ├── pick 3 → permute([1,2])
# │   → [2,1], [1,2] → [2,1,3], [1,2,3]