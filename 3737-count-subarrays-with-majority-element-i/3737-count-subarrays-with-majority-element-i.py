class Solution:
    def countMajoritySubarrays(self, nums, target):
        p = [0]
        for x in nums:
            p.append(p[-1] + (1 if x == target else -1))

        mp = {v: i + 1 for i, v in enumerate(sorted(set(p)))}
        bit = [0] * (len(mp) + 1)

        def add(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def qry(i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        ans = 0
        for x in p:
            r = mp[x]
            ans += qry(r - 1)
            add(r)
        return ans