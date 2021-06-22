class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in matrix:
            if target not in i:
                continue
            else:
                for j in i:
                    if j == target:
                        return True
            
        return False

# ===============

