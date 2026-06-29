class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        longeur_2 = len(nums) / 2
        dictionaire = {}
        for elt in nums:
            if elt not in dictionaire:
                dictionaire[elt] = 1
            else:
                dictionaire[elt] += 1
        for keys, values in dictionaire.items():
            if values > longeur_2:
                return keys
