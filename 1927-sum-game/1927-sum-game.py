class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num) // 2
        a = num[:n]
        b = num[n:]

        sa = sum(int(x) for x in a if x != '?')
        sb = sum(int(x) for x in b if x != '?')
        ca = a.count('?')
        cb = b.count('?')

        if (ca + cb) % 2:
            return True

        diff = sa - sb
        qdiff = ca - cb

        return diff != -qdiff * 9 // 2