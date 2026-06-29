class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionaire = {}
        count = 0
        for elt in ransomNote:
            if elt not in dictionaire:
                dictionaire[elt] = 1
            else:
                dictionaire[elt] += 1
        for ltr in dictionaire:
            nbr = dictionaire[ltr]
            magaz = magazine.count(ltr)
            if nbr > magaz:
                return False
        return True
