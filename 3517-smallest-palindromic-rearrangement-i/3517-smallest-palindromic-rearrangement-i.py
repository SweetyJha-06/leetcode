class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1

        left = []
        mid = ""

        for i in range(26):
            left.append(chr(i + 97) * (cnt[i] // 2))
            if cnt[i] % 2:
                mid = chr(i + 97)

        left = "".join(left)
        return left + mid + left[::-1]