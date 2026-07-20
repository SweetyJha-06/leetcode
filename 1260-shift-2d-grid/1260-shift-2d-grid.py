class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        a = sum(grid, [])
        k %= m * n
        a = a[-k:] + a[:-k]
        return [a[i*n:(i+1)*n] for i in range(m)]