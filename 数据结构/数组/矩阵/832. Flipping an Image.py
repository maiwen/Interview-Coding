class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for row in A:
            row.reverse()
            row = [(x+1) % 2 for x in row]
            result.append(row)
        return result
