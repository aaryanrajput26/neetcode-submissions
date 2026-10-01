class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        windowsum=sum(arr[:k])
        count=0

        if windowsum/k>=threshold:
            count+=1

        for i in range(k,len(arr)):
            windowsum+=arr[i]
            windowsum-=arr[i-k]

            if windowsum/k>=threshold:
                count+=1

        return count