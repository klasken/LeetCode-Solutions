class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        somme = 1
        final = 0
        addition = 0
        while n != 0:
            temp = n % 10
            n = n // 10
            somme = somme * temp
            addition = addition + temp
        final = somme - addition
        return final
