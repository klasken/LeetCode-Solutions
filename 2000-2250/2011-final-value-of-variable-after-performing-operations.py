class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        count = 0
        for i in range(len(operations)):
            if operations[i] == "--X" or operations[i] == "X--":
                count -= 1
            elif operations[i] == "X++" or operations[i] == "++X":
                count += 1
            else:
                count += 0
        return count
