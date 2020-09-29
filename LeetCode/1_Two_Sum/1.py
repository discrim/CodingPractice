class Solution:
    def twoSum(self, nums, target):
        mymap = []
        for ii in range(len(nums)):
            mymap.append((ii, nums[ii]))
        mymap = sorted(mymap, key=lambda xx: xx[1])
        print(mymap)
        ii = 0
        jj = len(nums) - 1
        while (ii < jj):
            print("Now: ", mymap[ii][1], " + ", mymap[jj][1], " ? ", target)
            if mymap[ii][1] + mymap[jj][1] == target:
                return [mymap[ii][0], mymap[jj][0]]
            elif mymap[ii][1] + mymap[jj][1] < target:
                print("Less")
                ii += 1
                continue
            else: # mymap[ii][1] + mymap[jj][1] > target
                print("Greater")
                jj -= 1
                continue
            if mymap[ii + 1][1] - mymap[ii][1] < mymap[jj][1] - mymap[jj - 1][1]:
                ii += 1
            else:
                jj -= 1

if __name__ == "__main__":
    in1 = ([3, 2, 3], 6)
    
    sol = Solution()
    print(sol.twoSum(in1[0], in1[1]))