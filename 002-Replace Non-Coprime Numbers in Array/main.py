class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for val in nums:
            cur = val
            while len(stack) != 0:
                top = stack[len(stack)-1]
                gcd_value = gcd(cur, top)
                if gcd_value == 1:
                    break
                stack.pop()
                cur = (cur * top)//gcd_value
            stack.append(cur)

        return stack
    
    def gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        else:
            return gcd(b, a%b)
        