class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans=float('inf')
        white=0

        for i in range(len(blocks)):
            if blocks[i]=='W':
                white+=1

            if i>=k-1:
                ans=min(ans,white)

                if blocks[i-k+1]=='W':
                    white-=1
        return ans
        