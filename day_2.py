# Link: https://www.hackerrank.com/challenges/list-comprehensions/problem
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = []
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if i+j+k != n:
                    result.append([i,j,k])
    print(result)

# ANOTHER WAY using list comperhension 
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l = [[i,j,k]for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(l)


# Link: https://leetcode.com/problems/build-array-from-permutation/submissions/2158814615/
class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return[nums[nums[i]] for i in range(len(nums))]

# ANOTHER WAY
class Solution:
    def buildArray (self, nums: list[int]) ->list [int]:
        res = []
        for n in nums:
            res.append(nums[n])
            return res

# LINK: 