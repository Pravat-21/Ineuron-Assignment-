class Solution(object):
    def Sqrt_root(self, x):
        
        low_value = 0
        high_value = x
        middle_value = (low_value + high_value) // 2

        while low_value <= high_value:
            if middle_value * middle_value == x:
                return middle_value
            elif middle_value * middle_value < x:
                low_value = middle_value + 1
            else:
                high_value = middle_value - 1
            middle_value = (low_value + high_value) // 2
        return int(middle_value)
    
if __name__=="__main__":
    sol1=Solution()
    res=sol1.Sqrt_root(80)
    print(res)




