'''
Given an integer n, return true if it is a power of two. Otherwise, return false.
 An integer n is a power of two, if there exists an integer x such that n == 2x.

Input: n = 1
Output: true
Explanation: 20 = 1
-----------------------------------------------------------------------------------------
If a number is in power of 2 it will have only 1 set bit i.e., the most significant bit
Example:

64: 1000000
16: 10000
and when the number is subtracted by 1 results in all 1s.
Example:

8 - 1: 0111
2 - 1: 01
Now we can use the property if bitwise and operator, which gives 0 if the set bits are opposite and while returning we just return ! (not) of the result.

Suppose 8 is in power of 2 so 8 & 8-1 will result 0, so return 1 (true)
1000 & 0111= 0000

and consider a number not in power of 2, lets say 7
7 & 7-1 will result in 1
111 & 110 = 1, so just return !1 which is false

'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
        
