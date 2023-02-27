"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.build( grid , 0, len(grid)-1 ,0, len(grid[0])-1 )

     



    def build(self,grid, row_start,row_end,col_start,col_end):
        if row_start>row_end or col_start>col_end:
            return None

        isLeaf=True
        val=grid[row_start][col_start]

        for i in range(row_start,row_end+1):
            for j in range(col_start,col_end+1):
                if grid[i][j]!=val:
                    isLeaf=False
                    break
            if isLeaf==False:
                break
        if isLeaf:
            return Node(val==1,True,None,None,None,None)
        

        mid_row=(row_start+row_end)//2
        mid_col=(col_start+col_end)//2
        
        
    
        topLeft=self.build(grid,row_start,mid_row,col_start,mid_col)
        topRight=self.build(grid,row_start,mid_row,mid_col+1,col_end)
        bottomLeft=self.build(grid,mid_row+1,row_end,col_start,mid_col)
        bottomRight=self.build(grid,mid_row+1,row_end,mid_col+1,col_end)
        
        return Node(False,False, topLeft,topRight,bottomLeft,bottomRight)
        
        





        
