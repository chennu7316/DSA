
class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        hashData={}
        res=[]
        j=0;
        for i in range(N):
            if A[i] in hashData:
                hashData[A[i]]+=1
            else:
                hashData[A[i]]=1
            if i-j+1==K:
                res.append(len(hashData))
                if hashData[A[j]]==1:
                    del hashData[A[j]]
                else:
                    hashData[A[j]]-=1
                j=j+1
        return res
