class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dist[i][j] = 0
                    q.append((i, j))

        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            x, y = q.popleft()
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        pq = [(-dist[0][0], 0, 0)]
        seen = [[False] * n for _ in range(n)]
        seen[0][0] = True

        while pq:
            s, x, y = heapq.heappop(pq)
            s = -s
            if x == n - 1 and y == n - 1:
                return s
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not seen[nx][ny]:
                    seen[nx][ny] = True
                    heapq.heappush(pq, (-min(s, dist[nx][ny]), nx, ny))