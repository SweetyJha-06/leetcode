from math import gcd
from functools import reduce

class Solution:
    def findKthSmallest(self, coins, k):
        coins = list(set(coins))
        
        def lcm(a, b):
            return a // gcd(a, b) * b
        
        def count(x):
            total = 0
            n = len(coins)
            for mask in range(1, 1 << n):
                v = 1
                bits = 0
                for i in range(n):
                    if mask >> i & 1:
                        v = lcm(v, coins[i])
                        if v > x:
                            break
                        bits += 1
                else:
                    if bits & 1:
                        total += x // v
                    else:
                        total -= x // v
            return total
        
        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        
        return lo