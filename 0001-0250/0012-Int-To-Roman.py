class Solution:
    def intToRoman(self, num: int) -> str:
        total = ""
        valeurs_romaines = [(1000, "M"),(900, "CM"),(500, "D"),(400, "CD"),(100, "C"),(90, "XC"),(50, "L"),(40, "XL"),(10, "X"),(9, "IX"),(5, "V"),(4, "IV"),(1, "I")]
        for cle, valeur in valeurs_romaines:
            nbr_de_fois = num // cle
            if nbr_de_fois > 0:
                total += valeur * nbr_de_fois
                num %= cle
        return total
