class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smallerStr = str2 if len(str2) <= len(str1) else str1
        largerStr = str1 if smallerStr == str2 else str2

        def gcd(a, b):
            print('GCD', "a =", a, "b =", b)
            if a == '':
                return b
            newB = b
            while newB[0:len(a)] == a:
                print('TRIM', newB)
                newB = newB[len(a):]
            if newB == b:
                return ''
            return gcd(newB, a)

        return gcd(smallerStr, largerStr)


# Solution().gcdOfStrings('ABCABC', 'ABC')

Solution().gcdOfStrings('ABABAB', 'ABAB')