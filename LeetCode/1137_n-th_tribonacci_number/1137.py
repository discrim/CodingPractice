class Solution2:
    mem = [0, 1, 1]
    def tribonacci(self, n: int) -> int:
        if len(self.mem) > n:
            return self.mem[n]
        
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            val = self.tribonacci(n - 3) \
                + self.tribonacci(n - 2) \
                + self.tribonacci(n - 1)
            self.mem.append(val)
            return val

class Solution:
    record = []
    def tribonacci(self, n: int) -> int:
        if len(self.record) > n:
            return self.record[n]
        
        if n == 0:
            self.record.append(0)
            return 0
        elif n == 1 or n == 2:
            self.record.append(1)
            return 1
        else:
            val = self.tribonacci(n - 3) \
                + self.tribonacci(n - 2) \
                + self.tribonacci(n - 1)
            self.record.append(val)
            return val

if __name__ == "__main__":
    x = Solution2()
    x.tribonacci(30)
    print(x.mem)
    
    y = Solution()
    y.tribonacci(30)
    print(y.record)