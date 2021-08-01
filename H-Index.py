class Solution:
    def h_index(self,citations):
        if not citations: return 0
        N = len(citations) 
        l = 0
        r = N - 1
        while l < r:
            mid = (l + r)//2
            if citations[mid] >= mid:
                r = mid
            else:   
                l = mid + 1
        if citations[l] == 0: return 0       
        return N-l




citation = [3,0,6,1,5]
print(Solution().h_index(citation))