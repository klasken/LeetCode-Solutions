class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        tab = []
        for k in range(2):
            for i in range(len(nums)):
                tab.append(nums[i])
        return tab
