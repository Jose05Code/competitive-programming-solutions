#
# @lc app=leetcode id=861 lang=python3
#
# [861] Score After Flipping Matrix
#

# @lc code=start
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        
        #all rows start with 1
        for i in range(height):
            if grid[i][0] == 0:
                for j in range(width):
                    grid[i][j] = 1 - grid[i][j]
        
        #all columns have more 1s than 0s
        for j in range(1, width):
            count = sum(grid[i][j] for i in range(height))
            if(count < height - count):
                for i in range(height):
                    grid[i][j] = 1 - grid[i][j]
                    
        #calculate the score
        score = 0
        binary_to_decimal = 0
        for i in range(height):
            for j in range(width):
                score += grid[i][j] * (2 ** (width - j - 1))
            
            
        return score
# @lc code=end

