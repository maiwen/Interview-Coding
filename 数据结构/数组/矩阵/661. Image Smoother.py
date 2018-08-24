class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in range(R)]
        
        for r in range(R):
            for c in range(C):
                count = 0
                for i in (r-1, r, r+1):
                    for j in (c-1, c, c+1):
                        if 0 <= i < R and 0 <= j < C:
                            ans[r][c] += M[i][j]
                            count += 1          
                ans[r][c] //= count 
                
        return ans
