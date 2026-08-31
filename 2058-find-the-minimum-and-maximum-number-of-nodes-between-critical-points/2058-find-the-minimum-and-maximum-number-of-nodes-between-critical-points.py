class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        cur = head.next
        pos = 1
        first = -1
        last = -1
        mn = float('inf')

        while cur.next:
            if (cur.val > prev.val and cur.val > cur.next.val) or (cur.val < prev.val and cur.val < cur.next.val):
                if first == -1:
                    first = pos
                else:
                    mn = min(mn, pos - last)
                last = pos

            prev = cur
            cur = cur.next
            pos += 1

        if first == -1 or first == last:
            return [-1, -1]

        return [mn, last - first]