class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=float('inf')
        for i in range(len(nums)-k+1):
            m=nums[i+k-1]-nums[i]
            ans=min(m,ans)
        return ans




                