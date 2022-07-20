from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        phoneletters = {
            2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7:'pqrs', 8:'tuv', 9:'wxyz' 
        }

        def backtrack(i, current_string):
            # print(f"backtrack function: i:{i}, cur str: {current_string}")
            # print(f"res: {res}")
            if len(current_string) == len(digits):
                res.append(current_string)
                return
            for c in phoneletters[int(digits[i])]:
                backtrack(i+1, current_string + c)
        if digits:
            backtrack(0,"")

        return res


s= Solution()
print(s.letterCombinations('23'))
