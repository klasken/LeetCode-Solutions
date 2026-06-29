class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        somme_total = sum(nums)
        somme_gauche = 0

        for i in range(len(nums)):
            somme_droite = somme_total - somme_gauche - nums[i]
            if somme_gauche == somme_droite:
                return i
            somme_gauche += nums[i]
        return -1
