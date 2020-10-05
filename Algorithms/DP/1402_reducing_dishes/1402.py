class Solution:
    def maxSatisfaction(self, satisfaction):
        satsort = sorted(satisfaction)
        
        tmp = 0        
        tot = 0
        while satsort:
            tmp += satsort.pop()
            if tmp < 0:
                break
            tot += tmp
        return tot
        '''
        currmax = 0
        satsort = sorted(satisfaction)
        leng1 = len(satsort)
        
        for nn in range(leng1):
            satpart = satsort[nn:]
            leng2 = leng1 - nn
            time = [ii for ii in range(1, leng2 + 1)]
            
            coeff = []
            for ii in range(leng2):
                coeff.append(satpart[ii] * time[ii])
            cumul = [coeff[0]]
            for ii in range(1, leng2):
                cumul.append(cumul[ii - 1] + coeff[ii])
            for elem in cumul:
                if currmax < elem:
                    currmax = elem
        return currmax
        '''

if __name__ == "__main__":
    ins = [[-1,-8,0,5,-9], [4,3,2], [-1,-4,-5], [-2,5,-1,0,3,-3]]
    sol = Solution()
    for elem in ins:
        print(sol.maxSatisfaction(elem))