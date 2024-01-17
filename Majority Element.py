class Solution:
    def majorityElement(self, nums) -> int:
        res = {}
        for i in nums:
            if i not in res:
                res.update({i:1})
            else:
                res.update({i:(res.get(i) + 1)})
        sorted_res = sorted(res.items(), key=lambda x:x[1])
        return sorted_res[-1][0]

def main():
    solution = Solution()
    print(solution.majorityElement([2,2,1,1,1,2,2]))
    
main()