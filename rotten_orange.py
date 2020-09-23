from collections import deque

from astroid import List


class Solution:
    def orangesRotting(self, grid):

        # Constant for grid state
        VISITED = -1
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2

        # Get dimension of grid
        h, w = len(grid), len(grid[0])

        # record for fresh oranges
        fresh_count = 0

        # record for position of initial rotten oranges
        rotten_grid = []

        # board prescan for parameter initialization
        for y in range(h):
            for x in range(w):

                if grid[y][x] == FRESH:
                    fresh_count += 1

                elif grid[y][x] == ROTTEN:
                    rotten_grid.append((x, y, 0))

        traversal_queue = deque(rotten_grid)

        time_record = 0

        # BFS to rotting oranges
        while traversal_queue:

            x, y, time_stamp = traversal_queue.popleft()

            for dx, dy in ((-1, 0), (+1, 0), (0, -1), (0, +1)):

                next_x, next_y = x + dx, y + dy

                if 0 <= next_x < w and 0 <= next_y < h and grid[next_y][next_x] == FRESH:
                    fresh_count -= 1
                    grid[next_y][next_x] = VISITED

                    # update time record
                    time_record = time_stamp + 1

                    # adding current rotten orange to traversal queue
                    traversal_queue.append((next_x, next_y, time_stamp + 1))

        if fresh_count == 0:
            return time_record
        else:
            return -1
s = Solution()

print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))