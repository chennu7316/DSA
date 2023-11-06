#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        hashData={}
        hashData[0]=-1
        sumValue=0;
        res=0
        for i in range(n):
            sumValue+=arr[i]
            if sumValue not in hashData:
                hashData[sumValue]=i
            else:
                if res<(i-hashData[sumValue]):
                    res=i-hashData[sumValue]
           
        return res
                
            
