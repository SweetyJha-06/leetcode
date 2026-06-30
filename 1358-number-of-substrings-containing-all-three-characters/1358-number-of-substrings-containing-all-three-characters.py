class Solution:
    def numberOfSubstrings(self, s):
        cnt = {'a': 0, 'b': 0, 'c': 0}
        l = ans = 0

        for r in range(len(s)):
            cnt[s[r]] += 1
            while cnt['a'] and cnt['b'] and cnt['c']:
                ans += len(s) - r
                cnt[s[l]] -= 1
                l += 1

        return ans